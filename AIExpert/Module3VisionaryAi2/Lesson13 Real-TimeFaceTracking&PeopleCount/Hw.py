import cv2
import matplotlib.pyplot as plt
import numpy as np


image = cv2.imread('example.jpg')


imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(imageRGB)
plt.title("Original Image")
plt.show()


croppedImage = image[100:400, 250:450]

croppedImageRGB = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)

plt.imshow(croppedImageRGB)
plt.title("Cropped Image")
plt.show()


(h, w) = image.shape[:2]

center = (w//2, h//2)

rotationMatrix = cv2.getRotationMatrix2D(center, 120, 1.0)

rotatedImage = cv2.warpAffine(image, rotationMatrix, (w, h))

rotatedRGB = cv2.cvtColor(rotatedImage, cv2.COLOR_BGR2RGB)

plt.imshow(rotatedRGB)
plt.title("Rotated Image (90 degrees)")
plt.show()


brightnessMatrix = np.ones(image.shape, dtype="uint8") * 90

brighterImage = cv2.add(image, brightnessMatrix)

brighterRGB = cv2.cvtColor(brighterImage, cv2.COLOR_BGR2RGB)

plt.imshow(brighterRGB)
plt.title("Brighter Image")
plt.show()