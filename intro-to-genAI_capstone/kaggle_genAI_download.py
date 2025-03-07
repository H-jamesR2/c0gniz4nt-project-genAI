import kagglehub

# Download latest version
# download abstract art DATASET for genAI applications
path = kagglehub.dataset_download("greg115/abstract-art")

print("Path to dataset files:", path)