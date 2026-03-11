import cv2
import numpy as np
import matplotlib.pyplot as plt

# import os
# print(os.getcwd(),'FldrIss')  # prints current working directory

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8)) #  # figure is used to create a new figure for displaying the image. figsize=(8, 8) sets the size of the figure to 8 inches in width and 8 inches in height, providing a larger canvas for better visibility  
    if len(image.shape) == 2:  # Grayscale image. The shape of a grayscale image is typically (height, width), which has only two dimensions. If the image has only two dimensions, it is treated as a grayscale image and displayed using a grayscale colormap (cmap='gray').
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# The interactive_edge_detection function allows users to apply different edge detection and filtering techniques to an image. It reads an image from the specified path, converts it to grayscale, and then provides a menu for users to choose from various options such as Sobel Edge Detection, Canny Edge Detection, Laplacian Edge Detection, Gaussian Smoothing, and Median Filtering. The results of the selected operation are displayed using the display_image function.
def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Sobel Edge Detection
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3) # The cv2.Sobel function is used to compute the Sobel edge detection in the x-direction. The parameters are as follows: gray_image is the input grayscale image, 
            # cv2.CV_64F specifies the desired depth of the output image (64-bit floating point). In OpenCV, depth means the data type (precision) used to store each pixel value in the output image. It determines how much memory and accuracy each pixel uses. High precision decimal values can be stored in the output image, which is important for edge detection to capture subtle changes in intensity. 
            # 1 indicates that we want to compute the derivative in the x-direction; This means calculate the change in intensity along the horizontal direction (x-axis). It detects vertical edges in the image. Because when brightness changes left to right, it indicates a vertical boundary.
            # “do not calculate vertical (y-axis) changes in brightness.”. 0 indicates that we do not want to compute the brightness changes in the y-direction,  
            # ksize=3 specifies the size of the Sobel kernel (3x3). ie 3x3 matrixis used(3 rows 3 columns)
            # 1️⃣ What is a Kernel?
# A kernel (also called a filter or mask) is a small matrix of numbers used to process an image.
# It “slides” over the image.
# At each position, it performs mathematical operations on the pixel values underneath.
# This helps detect patterns like edges, blurring, sharpening, etc.
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3) # 0 means ignore left-right changes . 1 → detect top-bottom changes → horizontal edges.  a 3×3 matrix
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
# sobel_x → detects vertical edges
# sobel_y → detects horizontal edges
# cv2.bitwise_or → combines both edge images into one image where all edges are visible.
# 2️⃣ Why astype(np.uint8)?
# Sobel outputs are often float64 (CV_64F) to store negative and large values.
# cv2.bitwise_or requires unsigned 8-bit integers (uint8).
# So we convert:
# sobel_x.astype(np.uint8)
# sobel_y.astype(np.uint8)

# Any edge detected in either (2) image will appear in the result.
# When we write "edges = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))"
# we are using two separate images:
# i. sobel_x → contains vertical edges
# ii. sobel_y → contains horizontal edges


            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            # Canny Edge Detection
            print("Adjust thresholds for Canny (default: 100 and 200)")
# Thresholds tell the Canny algorithm which gradients to consider as edges.
# Canny uses two thresholds: lower_thresh, upper_thresh.
# Pixels with gradient above upper_thresh → always kept as edges
# Pixels with gradient below lower_thresh → ignored
# Pixels between the two → kept if near strong edges 
            lower_thresh = int(input("Enter Lower threshold: "))
            upper_thresh = int(input("Enter Upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)

        elif choice == "3":
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            # cv2.CV_64F → depth of the output image . Laplacian can produce negative values, so we are formating properly to capture them accurately.We can safely store negative and large positive values.

            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))
# np.abs() → takes absolute value → treats negative edges as positive intensity. np is just a short alias for the numpy library in Python.
# .astype(np.uint8) → converts to standard 8-bit image for display. astype() is a NumPy array method. It changes the data type of the array elements to the type you specify.

        elif choice == "4":
            # Gaussian Smoothing
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0) # The last parameter 0 is sigmaX, which is the standard deviation of the Gaussian in the X direction. sigmaX = standard deviation of the Gaussian in the X direction (horizontal).
            # 0 → let OpenCV automatically decide how strong the blur should be based on the kernel size.
            display_image("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            # Median Filtering
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)

        elif choice == "6":
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Provide the path to an image for the activity
# interactive_edge_detection('example.jpg')
interactive_edge_detection('AIExpert/Module2VisionaryAi/Lesson10 EdgeDetection&FilteringWithOpenCV/example.jpg')