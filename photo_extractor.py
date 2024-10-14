import os
import shutil

DIRECTORY_NAME = "23-2021_04_07_Coperchi 2"
# Define the base directory containing the numbered folders
base_directory = f"datasets/{DIRECTORY_NAME}"
# Define the destination directory for copied images
destination_directory = f"extracted/{DIRECTORY_NAME}"

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Get all directories in the parent directory
all_folders = [f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))]

# Filter out folders that have numeric names only
numeric_folders = [f for f in all_folders if f.isdigit()]

# Sort the numeric folders if needed (optional)
numeric_folders.sort(key=int)

# Iterate over numbered folders from 1 to 114
for folder in numeric_folders:
    folder_name = str(folder)  # Convert to string to match folder names
    folder_path = os.path.join(base_directory, folder_name, "Snapshots")

    # Check if the Snapshots folder exists
    if os.path.exists(folder_path):
        # Construct the path for the CoatedTop.jpg file
        image_path = os.path.join(folder_path, "CoatedTop.jpeg")

        # Check if the CoatedTop.jpg file exists
        if os.path.isfile(image_path):
            # Define the destination image path with the folder number as the filename
            destination_image_path = os.path.join(destination_directory, f"{folder_name}.jpeg")
            # Copy the image to the new location
            shutil.copy(image_path, destination_image_path)
            print(f"Copied {image_path} to {destination_image_path}.")
        else:
            print(f"File {image_path} does not exist.")
    else:
        print(f"Folder {folder_path} does not exist.")

print("Image copying completed.")
