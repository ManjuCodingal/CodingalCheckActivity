# pip install opencv-python - for windows 
# pip3 install opencv-python - for mac

import cv2 # Import the OpenCV library, it contains functions for image processing and computer vision tasks.

# Load the image

image = cv2.imread('dogImage.jpg')
# • cv2.imread() is used to load an image into memory. The path 'example.jpg' points to the image file.
# • image stores the image as a NumPy array. If the image cannot be loaded (e.g., due to incorrect path or file format), image will be None.


# Resize the window to a specific size without resizing the image

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)  # Create a resizable window
# • cv2.namedWindow() creates a window where we can display images. The cv2.WINDOW_NORMAL flag makes the window resizable, allowing the user to adjust the size of the display window independently of the image.

cv2.resizeWindow('Loaded Image', 800, 500)  # Set the window size to 800x500 (width x height)
# • cv2.resizeWindow() changes the size of the window displaying the image. In this case, the window is resized to 800x500 pixels. Note that this does not affect the size of the image itself but only the window in which it is displayed.



# Display the image in the resized window

cv2.imshow('Loaded Image', image)
# • cv2.imshow() displays the image in the created window ('Loaded Image'). It shows the image in its original resolution inside the resized window.
# • The imshow() function takes two arguments: the window name and the image to be displayed.

cv2.waitKey(0)  # Wait for a key press
# • cv2.waitKey(0) pauses the execution of the code until a key is pressed. The 0 means it waits indefinitely until a key press occurs. The key press is not used in this activity, but you could use it to trigger specific actions (like closing the window or saving the image).

cv2.destroyAllWindows()  # Close the window
# • cv2.destroyAllWindows() closes any OpenCV windows that were created. It is essential to release the resources after the image is no longer required.



# Print image properties

print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels
# • The image.shape gives the dimensions of the loaded image. It returns a tuple of three values:
#  Height (number of rows)
#  Width (number of columns)
#  Channels (number of color channels, typically 3 for RGB images)
# Eg: If the image is 600 pixels high, 800 pixels wide, and has 3 color channels (RGB), the output will be (600, 800, 3).