import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    # BGR format: Blue=0 index, Green=1 index, Red=2 index

    # In NumPy, : is called a slice operator. It means “take all elements along this axis”.
    
    if filter_type == "red_tint":
        # Remove blue and green channels for red tint
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 0] = 0  # Blue channel to 0
    elif filter_type == "blue_tint":
        # Remove red and green channels for blue tint
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "green_tint":
        # Remove blue and red channels for green tint
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "increase_red":
        # Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)  # Increase red channel
        # Only Red channel increases:
        # Red: 200 + 50 → 250 (capped at 255). Green and Blue channels remain unchanged at 150 and 100, respectively.
        # [Blue, Green, Red] = [100, 150, 250]. The pixel becomes more red.
        # instead of 50, cannot give 100, can give only upto 55 because it will exceed the maximum value of 255 for a color channel. cv2.add() will handle this by capping(removing) the value at 255, preventing overflow and ensuring that the resulting pixel values remain valid. Each color channel (Blue, Green, Red) can only have values from 0 to 255.
        # 0 → no intensity, 255 → full intensity
    elif filter_type == "decrease_blue":
        # Decrease the intensity of the blue channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)  # Decrease blue channel
        # Only Blue channel decreases. Green and Red channels remain unchanged at 150 and 200, respectively.
        # cv2.subtract(Blue, 50): subtract 50 or any value like 50000, subtraction will occur till final value is 0; Final value cannot go below 0..
        # If too high value is subtracted, Too high → image may look unnaturally red/yellow because blue is gone.
    return filtered_image

# Load the image
image_path = 'example.jpg'  # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"  # Default filter type

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")

    while True:
        # Apply the selected filter
        filtered_image = apply_color_filter(image, filter_type)
        # Display the filtered image
        cv2.imshow("Filtered Image", filtered_image) # In OpenCV, the image is always stored in BGR format
        # Wait for key press
        key = cv2.waitKey(0)& 0xFF  # waits indefinitely for a key press, allows continuous checking of keys. We are calling user input from output image window.

# NOTE:: key = input("Enter filter key: ").strip().lower() ALSO OTHER MANY LINES MAY NEED CHANGE. like  if key == 'r' etc # This line is for terminal input, but here in this code we are calling user input from output window, so we are using cv2.waitKey() instead of input().

        # argument is time in milliseconds to wait: 0 → wait indefinitely until a key is pressed ; 1000 → wait 1 second. Here 0 waits indefinitely.It returns the ASCII code of the key pressed.
        # cv2.waitKey() returns a 32-bit integer (on some systems) which contains the key code in the lowest byte. Doing & 0xFF keeps only the lowest 8 bits, which correspond to the ASCII key code.

        # Map key presses to filters
        if key == ord('r'): # ord() is a built-in function that returns the ASCII (or Unicode) code of a character.
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")

cv2.destroyAllWindows()