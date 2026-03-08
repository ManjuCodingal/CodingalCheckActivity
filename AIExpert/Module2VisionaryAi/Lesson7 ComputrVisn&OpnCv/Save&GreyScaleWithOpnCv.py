import cv2
# • import cv2: This imports the OpenCV library, which is essential for image processing tasks such as loading, displaying, transforming, and saving images. OpenCV (Open Source Computer Vision) is a widely used library in computer vision applications.


# Load the image

image = cv2.imread('dogImage.jpg')
# • cv2.imread('example.jpg'):
# ○ Function: Reads an image from the specified file path.
# ○ Arguments: 'example.jpg' is the path to the image you want to load. It could be a relative or absolute path.
# ○ Returns: The loaded image in the form of a NumPy array (a matrix representing the image's pixel values).
# ○ Default Behavior: By default, OpenCV loads the image in BGR (Blue, Green, Red) format, not RGB.



# Convert the image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# • cv2.cvtColor(image, cv2.COLOR_BGR2GRAY):
# ○ Function: Converts an image from one color space to another. Here, it converts the BGR image to grayscale.
# ○ Arguments:
# ▪ image: The image you want to convert, which is currently in BGR format.
# ▪ cv2.COLOR_BGR2GRAY: This is a constant used by OpenCV to specify that you want to convert from BGR to grayscale. The conversion results in a 2D matrix where each pixel represents the intensity of light (i.e., brightness) rather than color.
# ○ Returns: A 2D NumPy array representing the grayscale image, where the pixel values range from 0 (black) to 255 (white).

# Resize the grayscale image to 224x224

resized_image = cv2.resize(gray_image, (224, 224))
# Function: cv2.resize(image, (width, height)) resizes the input image to the specified width and height. In this case, the grayscale image is resized to 224 pixels in width and 224 pixels in height.  
# 224x224 is the target size.
# gray_image is the image to be resized, it is the grayscale version of the original image.
# Returns a resized image in the form of a NumPy array with dimensions (224, 224) for the grayscale image. The pixel values are still in the range of 0 to 255, representing the intensity of light in the resized image.

# Display the resized grayscale image in a single window

cv2.imshow('Processed Image', resized_image)
# Functiion displays an image in a window. The first argument 'Processed Image' is the name of the window, and the second argument resized_image is the image to be displayed.
# Behaviour: Opens a window titled 'Processed Image' and shows the resized grayscale image. The image will be displayed in its original resolution (224x224) within the window. The window will remain open until a key is pressed.

# Wait for a key press

key = cv2.waitKey(0)  # Wait indefinitely for a key press
#  Waits for a key event indefinitely (0 means wait forever). When a key is pressed, it returns the ASCII value of the key. This allows you to capture user input and perform actions based on which key was pressed.


# Check if the "S" key was pressed (ASCII for 'S' is 83)

if key == ord('s'):

    # Save the processed image when "S" is pressed
    # ord is a built-in Python function that returns the ASCII value of a character, which is useful for comparing key presses in OpenCV applications.
#  ord('s') converts the character 's' to its corresponding ASCII value (which is 115). The if statement checks if the key pressed by the user matches this value, indicating that the "S" key was pressed. If the condition is true, the code inside the if block will execute, allowing you to save the processed image when the "S" key is pressed. 
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
# Saves the processed image to the specified file path. The first argument 'grayscale_resized_image.jpg' is the name of the file where the image will be saved, and the second argument resized_image is the image data to be saved. The image will be saved in JPEG format with the name 'grayscale_resized_image.jpg' in the current working directory.
    print("Image saved as grayscale_resized_image.jpg")

else:

    print("Image not saved")



# Close the window

cv2.destroyAllWindows()



# Print processed image properties

print(f"Processed Image Dimensions: {resized_image.shape}")