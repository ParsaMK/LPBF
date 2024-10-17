import cv2
import os
import numpy as np

def crop_circle(image_path, center, radius, output_path):
    img = cv2.imread(image_path)

    # Create a mask with the same dimensions as the image
    mask = np.zeros_like(img)

    # Draw a filled circle on the mask
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # Create a new image filled with the neutral color (gray)
    # neutral_color = (128, 128, 128)  # Gray
    neutral_color = (0, 0, 0)  # Black
    circular_cutout = np.full_like(img, neutral_color)

    # Apply the mask to fill in the circular region
    circular_cutout[mask[..., 0] == 255] = img[mask[..., 0] == 255]

    # Save the resulting image
    cv2.imwrite(output_path, circular_cutout)

def process_images(input_folder, output_folder, center, radius):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add more formats if needed
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Create circular cutout and save it
            crop_circle(image_path, center, radius, output_path)

# Example usage
input_folder = '../../extracted/13-coperchio_2021_03_24'  # Replace with your input folder path
output_folder = './circular'  # Replace with your output folder path
center = (1547, 1553)  # Your specified center
radius = 1500  # Your specified radius

process_images(input_folder, output_folder, center, radius)
