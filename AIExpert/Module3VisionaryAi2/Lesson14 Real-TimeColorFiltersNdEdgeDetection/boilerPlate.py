# Import cv2 for image/video processing and numpy for numerical operations.

# Define a function "apply_filter" with parameters "image" and "ftype":
#   - Make a copy of the input image.
#   - Check "ftype" and apply the corresponding filter:
#       * "red_tint": Zero out the green and blue channels.
#       * "green_tint": Zero out the blue and red channels.
#       * "blue_tint": Zero out the green and red channels.
#       * "sobel":
#             - Convert image to grayscale.
#             - Compute Sobel gradients in x and y directions.
#             - Combine these gradients using a bitwise OR.
#             - Convert the result back to a BGR image.
#       * "canny":
#             - Convert image to grayscale.
#             - Apply Canny edge detection.
#             - Convert the edge image to BGR.
#       * "cartoon":
#             - Convert image to grayscale and apply median blur.
#             - Use adaptive thresholding to detect edges.
#             - Smooth the original image using a bilateral filter.
#             - Combine the edge mask with the smoothed image.
#   - Return the processed image.

# Define the main function:
#   - Open the webcam using cv2.VideoCapture(0).
#   - If the camera fails to open, print an error and exit.
#   - Set a default filter type ("original").
#   - Print key instructions for selecting filters:
#         r: Red Tint, g: Green Tint, b: Blue Tint, s: Sobel, c: Canny, t: Cartoon, q: Quit.
#   - Start a loop to process frames:
#         * Capture a frame from the webcam.
#         * If the frame is not captured, print an error and exit the loop.
#         * Apply the current filter to the frame by calling "apply_filter".
#         * Display the filtered frame.
#         * Wait for a key press (with a short delay).
#         * Change the filter type based on the key pressed:
#               - Update to the corresponding filter if a valid key is pressed.
#               - Break the loop if 'q' is pressed.
#   - Release the webcam and close all OpenCV windows.

# Call the main function when the script is executed.
