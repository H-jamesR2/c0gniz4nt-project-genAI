import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.utils as vutils
import numpy as np
import os
from tqdm import tqdm
from torch.utils.data import DataLoader
from PIL import Image

# Device configuration
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")  # Apple M1/M2 GPU acceleration

# Hyperparameters
image_size = 128
batch_size = 32
latent_dim = 100
num_epochs = 20  # Start small, increase if needed
lr = 0.0002
beta1 = 0.5  # Adam optimizer parameter

# Path to processed images
dataset_path = "processed_abstract_art"

# Transformations
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Normalize to [-1, 1]
])

# Load dataset
dataset = datasets.ImageFolder(root=dataset_path, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Define Generator
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, 512, 4, 1, 0, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(True),
            nn.ConvTranspose2d(512, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(True),
            nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            nn.ConvTranspose2d(128, 3, 4, 2, 1, bias=False),
            nn.Tanh()  # Output in range [-1,1]
        )

    def forward(self, x):
        return self.model(x)

# Define Discriminator
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 128, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(128, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(256, 512, 4, 2, 1, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(512, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()  # Output probability
        )

    def forward(self, x):
        return self.model(x)

# Initialize models
G = Generator().to(device)
D = Discriminator().to(device)

# Loss & Optimizers
criterion = nn.BCELoss()
optimizer_G = optim.Adam(G.parameters(), lr=lr, betas=(beta1, 0.999))
optimizer_D = optim.Adam(D.parameters(), lr=lr, betas=(beta1, 0.999))

# Training Loop
fixed_noise = torch.randn(16, latent_dim, 1, 1, device=device)  # For generating sample images

for epoch in range(num_epochs):
    for i, (real_images, _) in enumerate(tqdm(dataloader)):
        real_images = real_images.to(device)
        batch_size = real_images.size(0)

        # Create labels
        real_labels = torch.ones(batch_size, 1, device=device)
        fake_labels = torch.zeros(batch_size, 1, device=device)

        # Train Discriminator
        optimizer_D.zero_grad()
        outputs = D(real_images).view(-1, 1)
        loss_real = criterion(outputs, real_labels)

        noise = torch.randn(batch_size, latent_dim, 1, 1, device=device)
        fake_images = G(noise)
        outputs = D(fake_images.detach()).view(-1, 1)
        loss_fake = criterion(outputs, fake_labels)

        loss_D = loss_real + loss_fake
        loss_D.backward()
        optimizer_D.step()

        # Train Generator
        optimizer_G.zero_grad()
        outputs = D(fake_images).view(-1, 1)
        loss_G = criterion(outputs, real_labels)
        loss_G.backward()
        optimizer_G.step()

    # Save sample generated images
    if (epoch + 1) % 5 == 0:
        vutils.save_image(G(fixed_noise).detach(),
                          f"generated_samples/epoch_{epoch+1}.png",
                          normalize=True)

    print(f"Epoch [{epoch+1}/{num_epochs}] - Loss_D: {loss_D.item():.4f}, Loss_G: {loss_G.item():.4f}")

# Save model checkpoints
torch.save(G.state_dict(), "generator.pth")
torch.save(D.state_dict(), "discriminator.pth")

print("Training complete. Models saved.")
