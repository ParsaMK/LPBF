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

# Use Otsu's method on a normalized histogram to find the threshold
pixel_total = sum(average_hist)
current_max, threshold = 0, 0
sum_total, sum_b, weight_b, weight_f = 0, 0, 0, 0

for i in range(256):
    sum_total += i * average_hist[i]

for i in range(256):
    weight_b += average_hist[i]
    weight_f = pixel_total - weight_b
    if weight_b == 0 or weight_f == 0:
        continue
    sum_b += i * average_hist[i]
    mean_b = sum_b / weight_b
    mean_f = (sum_total - sum_b) / weight_f
    var_between = weight_b * weight_f * (mean_b - mean_f) ** 2

    if var_between > current_max:
        current_max = var_between
        threshold = i

print(f"Otsu's threshold: {threshold}")

# Plot the average histogram with Otsu's threshold
plt.figure(figsize=(10, 5))
plt.plot(average_hist, color='blue')
plt.axvline(x=threshold, color='red', linestyle='--', label=f'Otsu Threshold = {threshold}')
plt.title('Average Pixel Intensity Histogram with Otsu Threshold')
plt.xlabel('Pixel Intensity (Gray Level)')
plt.ylabel('Number of Pixels (Averaged)')
plt.xlim([0, 255])
plt.grid(True)
plt.legend()
plt.show()