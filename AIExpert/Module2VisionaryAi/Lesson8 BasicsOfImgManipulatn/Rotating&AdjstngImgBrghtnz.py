import cv2
import numpy as np
import matplotlib.pyplot as plt

# Why displaying in matplotlib?
# Pros:
# Can embed images inline in Jupyter notebooks, Google Colab, or scripts
# Supports subplots (display multiple images side by side)
# Can display grayscale images with colormap easily
# Fine control over titles, axes, labels, colorbars, etc.

# Who sees the plot?
# Matplotlib produces plots that are displayed on your screen, in a notebook, or in a figure.
# Humans use it to understand the data — check images, verify preprocessing, or debug. Verify image reading, Inspect preprocessing steps:- Cropping, resizing, rotating, grayscale conversion, brightness adjustments

image = cv2.imread('example.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # since we are using matplotlib to display, we need to convert the image from BGR to RGB

# Rotate the image by 45 degrees around its center
(h, w) = image.shape[:2]  # h is height, w is width of the image. This line extracts the height and width of the image. [:2] means we are only interested in the first two values of the shape, which correspond to the height and width. The shape of an image is typically represented as (height, width, channels), where channels represent the color channels (e.g., 3 for RGB). By using [:2], we ignore the channels and only get the height and width.
center = (w//2, h//2) # This is used to find the geometric center of the image, which is important when you want to rotate the image around its center.
M = cv2.getRotationMatrix2D(center, 45, 1.0)    # rotate by 45 degrees
# 1 is the scale factor (1.0 means no scaling). If you want to make the image larger or smaller while rotating, you can adjust this value. For example, 0.5 would make the image half its original size, and 2.0 would double its size.
rotated = cv2.warpAffine(image, M, (w, h)) # It returns the transformed image.
# src → source image (the one you want to transform)
# M → 2×3 transformation matrix (rotation, scaling, translation)
# dsize → output image size (width, height)
# It returns the transformed image.

# Why it’s called warpAffine
# Affine transformation = any combination of:
# Rotation
# Translation (moving the image)
# Scaling (resizing)
# Shearing (slanting)

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
# Smaller number (e.g., 20) → less brightening
# Larger number (e.g., 100) → more brightening
brighter = cv2.add(image, brightness_matrix)
# np.ones(image.shape) → creates a matrix of ones with the same shape as your image (height, width, channels)
# dtype="uint8" → pixel values are 8-bit integers (0–255)
# * 50 → multiplies every value by 50

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()