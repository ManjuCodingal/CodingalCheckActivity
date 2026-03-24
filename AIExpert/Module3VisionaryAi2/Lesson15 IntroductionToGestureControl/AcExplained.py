# To run code: py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\AIExpert\Module3VisionaryAi2\Lesson15 IntroductionToGestureControl\AcExplained.py"

# Hand area detection
import cv2
import numpy as np

# Set up webcam capture
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read() # Takes live video from your webcam

    if not ret:
        print("Error: Failed to capture image.")
        break


    # Convert to HSV for color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # HSV is better for detecting colors (like skin). Makes it easier to filter out skin colors regardless of brightness or lighting.
# HSV is a color model used in image processing. It represents colors in terms of:
# H – Hue → the type of color (red, green, blue…)
# S – Saturation → the intensity or purity of the color
# V – Value → the brightness of the color

    # Define the range for skin color in HSV. It is used for detecting skin color in HSV color space.
    lower_skin = np.array([0, 20, 70], dtype=np.uint8) # minimum values of Hue, Saturation, and Value

# | Value | What it represents                                                            |
# | ----- | ----------------------------------------------------------------------------- |
# | 0     | **Hue (H)** – the color itself (here: red-ish tone for skin)                  |
# | 20    | **Saturation (S)** – color intensity/purity (low=less vivid, high=more vivid) |
# | 70    | **Value (V)** – brightness of the color (low=darker, high=brighter)           |
# So [0, 20, 70] = minimum HSV values for detecting skin color.

# 1️⃣ What is Hue? Hue is like “color identity” without brightness or intensity.
# Hue (H) in HSV represents the type of color. 
# 0   → Red (Here hue for lower_skin is 0, ie red)
# 20  → slightly orange (Here hue for upper_skin is 20, ie slightly orange)
# 60  → Yellow
# 90 → Green
# 120 → Cyan
# 150 → Blue
# 179 → Back to Red

# dtype = “data type” of array elements
# np.uint8 = 8-bit unsigned integer → numbers from 0 to 255

    upper_skin = np.array([20, 255, 255], dtype=np.uint8) # maximum values of Hue, Saturation, and Value

    # So any pixel in the frame with HSV values between lower_skin and upper_skin will be considered skin.
# Pixels between [0,20,70] and [20,255,255] → detected as skin

    # Create a mask to detect skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
# Creates a binary mask:
# White → skin pixels
# Black → non-skin

    # Apply the mask to the frame. Shows only skin-colored areas
    result = cv2.bitwise_and(frame, frame, mask=mask) # cv2.bitwise_and(src1, src2, mask=None)
# src1 = original image
# src2 = original image again
# Mask = white for hand, black for everything else

# White=hand, Black=background
    # Find contours (hand shape) in the masked image
#     ✔ Detects shapes (blobs) in the mask
# 👉 Largest blob = likely your hand

# A contour is a curve joining all the continuous points along the boundary of an object with the same color or intensity.
# In simple words: it’s the outline or shape of an object in an image.
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # cv2.findContours(image, mode, method)
# Why _ is used ? because we don’t need hierarchy in this case.

# cv2.RETR_EXTERNAL:: Retrieves only the outermost contours. Ignores holes or inner contours. Useful for hand detection.
# cv2.CHAIN_APPROX_SIMPLE:: Compresses contour points to save memory. Only stores end points of straight lines, not every pixel.

    # If contours are found, draw them
    if contours:
        max_contour = max(contours, key=cv2.contourArea)  # Get largest contour. max() finds the largest item in a list. key is a function applied to each item to determine its "size".
        if cv2.contourArea(max_contour) > 500:  # Ignore small contours
# | Blob        | Area (pixels) |
# | ----------- | ----          |
# | Finger tip  | 200           |
# | Hand        | 1500          |
# | Small noise | 30            |

            # Draw the bounding box around the detected hand
            x, y, w, h = cv2.boundingRect(max_contour)
# 1️⃣ What cv2.boundingRect() does
# This function draws the smallest upright rectangle that fully contains a contour.
# Think of it as boxing the hand in a rectangle.
# cv2.boundingRect(contour) returns 4 numbers:
# | Variable | Meaning                                                  |
# | -------- | -------------------------------------------------------- |
# | `x`      | x-coordinate of the **top-left corner** of the rectangle |
# | `y`      | y-coordinate of the **top-left corner** of the rectangle |
# | `w`      | **width** of the rectangle                               |
# | `h`      | **height** of the rectangle                              |

# (x, y) = top-left corner of the bounding box
# (w, h) = size of the rectangle
# The bottom-right corner = (x + w, y + h)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Get the center of the hand for further tracking or interaction
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Red dot at center of hand in detection. 5 is Radius of the circle in pixels. last value is Thickness of the circle border. -1 means fill the circle completely

    # Display the original and result frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Filtered Frame', result)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 📺 Output :: Basic hand detection and tracking (by color)
# You see:
# Webcam feed
# Green box around hand
# Red dot at center
# Filtered skin image