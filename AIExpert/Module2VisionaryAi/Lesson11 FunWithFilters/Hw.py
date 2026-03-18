import cv2
import numpy as np


def apply_color_filter(image, filter_type, intensity):
    """Apply the specified color filter to the image."""

    filtered_image = image.copy()

    # BGR format: Blue=0, Green=1, Red=2

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity)

    return filtered_image


# Load the image
image_path = 'example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")

else:

    filter_type = "original"
    intensity = 50   # default intensity

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("+ - Increase Intensity")
    print("- - Decrease Intensity")
    print("q - Quit")

    while True:

        filtered_image = apply_color_filter(image, filter_type, intensity)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"

        elif key == ord('b'):
            filter_type = "blue_tint"

        elif key == ord('g'):
            filter_type = "green_tint"

        elif key == ord('i'):
            filter_type = "increase_red"

        elif key == ord('d'):
            filter_type = "decrease_blue"

        # Increase intensity
        elif key == ord('+'):
            intensity += 10
            print("Intensity Increased:", intensity)

        # Decrease intensity
        elif key == ord('-'):
            intensity = max(0, intensity - 10)
            print("Intensity Decreased:", intensity)

        elif key == ord('q'):
            print("Exiting...")
            break

        else:
            print("Invalid key!")

cv2.destroyAllWindows()