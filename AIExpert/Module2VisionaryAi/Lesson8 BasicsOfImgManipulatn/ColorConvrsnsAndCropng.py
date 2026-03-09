import cv2
import matplotlib.pyplot as plt # import pyplot for displaying images, pyplot is a module in the matplotlib library that provides a collection of functions for creating static, animated, and interactive visualizations in Python.

image = cv2.imread('example.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb) # Note: OpenCV uses BGR format, so we need to convert it to RGB for displaying with matplotlib
# NOTE:: image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB):- This does not change the colors of the real image, it only reorders the channels so that Matplotlib displays it correctly. SO there will be no visual change between the original example.jpg and the RGB image you display
plt.title("RGB Image")
plt.show()

 # NOTE:: IF WE WANT TO WRONGLY VISUALISE THE IMAGE AS BGR. Colors will look incorrect (e.g., blues and reds will be swapped). Bcz openCV reads the image in BGR format, but matplotlib displays it as if it were in RGB format. So the colors will look incorrect because the blue and red channels are swapped. FOR WRONG IMAGE, use code below:-
# plt.imshow(image)  
# plt.title("Color Swapped Image")
# plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray') # Display the grayscale image, we use cmap='gray' to display it in grayscale. cmap stands for color map, and 'gray' specifies that we want to use a grayscale color map for displaying the image.
plt.title("Grayscale Image")
plt.show()

# Cropping the image
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
cropped_image = image[100:300, 200:400]  # Note: The first index (100:300) specifies the range of rows (height), and the second index (200:400) specifies the range of columns (width). This will give us a cropped image that includes the pixels from row 100 to 299 and column 200 to 399.

# Which is usually used BGR or RGB? 
# OpenCV uses BGR format internally, but matplotlib uses RGB format for displaying images. Therefore, when we read an image using OpenCV and want to display it using matplotlib, we need to convert the color format from BGR to RGB. This is done using the cv2.cvtColor function, which takes the image and the color conversion code (cv2.COLOR_BGR2RGB) as arguments. After this conversion, we can display the image correctly in matplotlib.
# AI models usually use RGB, sometimes grayscale, and rarely BGR (except during preprocessing with OpenCV).
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()

# NOTE:in output y axis, at top starts with 0 and bottom increases (1200), in x axis, at left starts with 0 and right increases. 
# Y axis appears so because:: The Y-axis starts at 0 at the top because images in computer vision use a coordinate system based on arrays (matrix indexing), not the traditional mathematical coordinate system.
# We are working with images using OpenCV and displaying them using Matplotlib, and both follow the image/matrix coordinate convention.