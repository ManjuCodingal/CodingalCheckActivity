import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image_path = 'example.jpg'  # User-provided image path
image = cv2.imread(image_path)

# Convert BGR to RGB for correct color display with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape # _ is for the number of color channels, which we don't need to use directly here

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rect1_width, rect1_height = 150, 150 # 150x150 pixels rectangle
top_left1 = (20, 20)  # Fixed 20 pixels padding from top and left edges
# top left gives the starting point of the rectangle, and we add the width and height to it to get the bottom-right corner. This way, we can easily define the rectangle's position and size based on its top-left corner and dimensions.

bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height) # Calculate bottom-right corner coordinates based on top-left and dimensions. top_left1[0] + rect1_width gives the x-coordinate of the bottom-right corner, and top_left1[1] + rect1_height gives the y-coordinate of the bottom-right corner. This way, we ensure that the rectangle is drawn with the specified width and height starting from the defined top-left corner.
# 0 in top_left1[0] means the x-coordinate of the top-left corner is 0, indicating it's aligned with the left edge of the image.
#  1 in top_left1[1] means the y-coordinate of the top-left corner is 0, indicating it's aligned with the top edge of the image. This means the rectangle will start from the very top-left corner of the image, with a small padding of 20 pixels to ensure it doesn't touch the edges directly.

cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)  # Yellow rectangle. Draws a yellow rectangle on the image using the specified top-left and bottom-right coordinates, with a thickness of 3 pixels. 0 is the blue channel, 255 is the green channel, and 255 is the red channel, resulting in yellow color. To give green color, we can set the blue and red channels to 0 and the green channel to 255, resulting in (0, 255, 0) for green.
# image_rgb is the target image on which the rectangle will be drawn. top_left1 and bottom_right1 are the coordinates of the top-left and bottom-right corners of the rectangle, respectively. (0, 255, 255) specifies the color of the rectangle in BGR format (yellow), and 3 is the thickness of the rectangle's border in pixels.

# Rectangle 2: Bottom-right corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)  # 20 pixels padding. The top-left corner of the second rectangle is calculated by subtracting the rectangle's width and height from the image's width and height, respectively, and then adding a 20-pixel padding to ensure it doesn't touch the edges of the image. This way, the rectangle will be positioned in the bottom-right corner of the image with a consistent margin from the edges.
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height) # Similar to the first rectangle, we calculate the bottom-right corner of the second rectangle by adding its width and height to its top-left corner coordinates. This ensures that the second rectangle is drawn with the specified dimensions starting from its defined top-left corner.
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)  # Magenta rectangle. (0,0,0) is black, (255,255,255) is white, (255,0,0) is blue, (0,255,0) is green, and (0,0,255) is red. To create magenta color, we can set the blue and red channels to 255 and the green channel to 0, resulting in (255, 0, 255) for magenta.

# Step 3: Draw Circles at the Centers of Both Rectangles
center1_x = top_left1[0] + rect1_width // 2 # Calculate the x-coordinate of the center of the first rectangle by adding half of its width to the x-coordinate of its top-left corner. This gives us the horizontal center point of the rectangle.
center1_y = top_left1[1] + rect1_height // 2 # Calculate the y-coordinate of the center of the first rectangle by adding half of its height to the y-coordinate of its top-left corner. This gives us the vertical center point of the rectangle.
center2_x = top_left2[0] + rect2_width // 2 # Calculate the x-coordinate of the center of the second rectangle by adding half of its width to the x-coordinate of its top-left corner. This gives us the horizontal center point of the second rectangle.
center2_y = top_left2[1] + rect2_height // 2 # Calculate the y-coordinate of the center of the second rectangle by adding half of its height to the y-coordinate of its top-left corner. This gives us the vertical center point of the second rectangle.
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)  # Filled green circle. 
# -1 indicates that the circle should be filled. (0, 255, 0) specifies the color of the circle in BGR format (green). 
# 15 is the radius of the circle. The circle is drawn at the center of the first rectangle with a radius of 15 pixels.
cv2.circle(image_rgb, (center2_x, center2_y), 15, (0, 255, 0), -1)  # Filled red circle

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3) # Green line connecting centers. Draws a green line between the centers of the two rectangles with a thickness of 3 pixels. The line starts at the center of the first rectangle (center1_x, center1_y) and ends at the center of the second rectangle (center2_x, center2_y).

# Step 5: Add Text Labels for Regions and Centers
font = cv2.FONT_HERSHEY_SIMPLEX # Font type for text annotations. cv2.FONT_HERSHEY_SIMPLEX is a predefined font in OpenCV that provides a simple and clear style for text annotations. It is commonly used for labeling images due to its readability and clean appearance.
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA) # Label for Region 1. Adds the text "Region 1" above the first rectangle. The position of the text is determined by the top-left corner of the rectangle (top_left1) with a vertical offset of 10 pixels to ensure it is placed above the rectangle. The font size is set to 0.7, the color is white (255, 255, 255), and the thickness of the text is 2 pixels. cv2.LINE_AA is used for anti-aliased line type, which makes the text smoother and more visually appealing.
# Anti aliasing is a technique used to smooth out jagged edges in digital images, especially when drawing lines or text. By using cv2.LINE_AA, the text will appear smoother and less pixelated, enhancing the overall visual quality of the annotations on the image.
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1_x - 40, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA) # -40 and +40 are used to position the text label "Center 1" slightly below and to the left of the center point of the first rectangle.
# -40 is used to move the text 40 pixels to the left of the center point, and +40 is used to move the text 40 pixels down from the center point. 
# This ensures that the label does not overlap with the circle drawn at the center and remains clearly visible. The font size is set to 0.6, the color is green (0, 255, 0), and the thickness of the text is 2 pixels.
cv2.putText(image_rgb, 'Center 2', (center2_x - 40, center2_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

# Step 6: Add Bi-Directional Arrow Representing Height
arrow_start = (width - 50, 20)  # Start near the top-right. width -50 to give some padding from the right edge and 20 for padding from the top edge. This sets the starting point of the arrow near the top-right corner of the image, ensuring it is clearly visible and does not touch the edges of the image.
arrow_end = (width - 50, height - 20)  # End near the bottom-right
# height -20 to give some padding from the bottom edge. This sets the ending point of the arrow near the bottom-right corner of the image, creating a vertical arrow that represents the height of the image. The arrow will span from near the top-right corner to near the bottom-right corner, visually indicating the height dimension of the image.

# Draw arrows in both directions
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)  # Downward arrow.
# arrow_start is the starting point of the arrow, and arrow_end is the ending point. (255, 255, 0) specifies the color of the arrow in BGR format (yellow). Order is important here, as it determines the direction of the arrow. Direction is from arrow_start to arrow_end, which means the arrow will point downward. T
# 3 is the thickness of the arrow line, and tipLength=0.05 specifies the length of the arrowhead as a fraction of the total arrow length. This draws a downward arrow from the starting point (near the top-right corner) to the ending point (near the bottom-right corner) in yellow color (255, 255, 0).
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)  # Upward arrow. Arrow direction is reversed by swapping arrow_start and arrow_end, which means the arrow will point upward. This draws an upward arrow from the ending point (near the bottom-right corner) to the starting point (near the top-right corner) in yellow color (255, 255, 0). Together with the downward arrow, this creates a bi-directional arrow indicating height.

# Annotate the height value
height_label_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2) # Position the height label to the left of the arrow and vertically centered between the start and end points. arrow_start[0] - 150 moves the label 150 pixels to the left of the starting point of the arrow, ensuring it is placed to the left of the arrow. (arrow_start[1] + arrow_end[1]) // 2 calculates the vertical center between the starting and ending points of the arrow, positioning the label in the middle of the arrow's height.
cv2.putText(image_rgb, f'Height: {height}px', height_label_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA) # height_label_position is the position where the height label will be placed, which we calculated in the previous step.
# The text of the label is formatted to include the height value of the image in pixels (height). The font size is set to 0.8, the color is yellow (255, 255, 0), and the thickness of the text is 2 pixels. This adds a clear annotation indicating the height of the image next to the bi-directional arrow. Line type cv2.LINE_AA is used for anti-aliased text, which makes the label smoother and more visually appealing.

# Step 7: Display the Annotated Image
plt.figure(figsize=(12, 8)) # figure is used to create a new figure for displaying the image. figsize=(12, 8) sets the size of the figure to 12 inches in width and 8 inches in height, providing a larger canvas for better visibility of the annotated image.
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Bi-Directional Height Arrow')
plt.axis('off') # axis('off') is used to hide the axes and ticks around the image, providing a cleaner and more focused display of the annotated image. This ensures that the viewer's attention is drawn to the annotations and the image itself without any distractions from the axes.
plt.show()