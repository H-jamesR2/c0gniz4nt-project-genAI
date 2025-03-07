import zipfile
import os
from PIL import Image
import numpy as np
import shutil

# Define paths
zip_file_path = "intro-to-genAI_projectDATA/abstract-art_greg115_archive.zip"  # Update this
extracted_dir = "abstract_art_dataset"
processed_dir = "processed_abstract_art"

# Step 1: Extract ZIP
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extracted_dir)

print(f"Dataset extracted to: {extracted_dir}")

# Step 2: Preprocess Images
target_size = (128, 128)  # Resize to 128x128 (adjust as needed)

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for subdir, _, files in os.walk(extracted_dir):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(subdir, file)
            img = Image.open(img_path).convert("RGB")  # Ensure RGB format
            img = img.resize(target_size)  # Resize
            
            # Convert to numpy array and normalize [-1, 1]
            img_array = np.array(img).astype(np.float32) / 127.5 - 1

            # Save processed image
            processed_img_path = os.path.join(processed_dir, file)
            img = Image.fromarray(((img_array + 1) * 127.5).astype(np.uint8))  # Convert back for saving
            img.save(processed_img_path)

print(f"Processed images saved in: {processed_dir}")

# Optional: Delete the original extracted dataset to save space
shutil.rmtree(extracted_dir)
print("Original extracted dataset deleted to save space.")
