import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_images_from_folder(root_folder):
    images = []
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                img_path = os.path.join(subdir, file)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    images.append(img)
    return images

# Root folder containing your subfolders with images
root_folder = '../../extracted'

# Load all the images from the subfolders
images = load_images_from_folder(root_folder)

# Initialize a cumulative histogram
cumulative_hist = np.zeros(256, dtype=np.float64)

# Loop through each image and accumulate the histograms
for img in images:
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    cumulative_hist += hist.flatten()

# Calculate the average histogram
average_hist = cumulative_hist / len(images)

# Plot the average histogram
plt.figure(figsize=(10, 5))
plt.plot(average_hist, color='blue')
plt.title('Average Pixel Intensity Histogram')
plt.xlabel('Pixel Intensity (Gray Level)')
plt.ylabel('Number of Pixels (Averaged)')
plt.xlim([0, 255])
plt.grid(True)
plt.show()