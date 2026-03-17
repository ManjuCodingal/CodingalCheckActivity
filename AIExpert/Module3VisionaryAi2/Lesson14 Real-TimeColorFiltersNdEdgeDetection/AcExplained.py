import cv2
import numpy as np

def apply_filter(image, ftype):
    """Apply a filter to the image based on the filter type."""
    img = image.copy()

# An image is a 3D array:
# (height, width, channels)
# Channels in OpenCV are in BGR order (not RGB):
# img[:, :, 0] → Blue channel (index 0)
# img[:, :, 1] → Green channel (index 1)
# img[:, :, 2] → Red channel (index 2)

    if ftype == "red_tint":
        img[:, :, 1] = img[:, :, 0] = 0 # (blueChannel=greenChannel=0) Set blue and Green channels to 0, keeping Red channel intact
    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0 # (blueChannel=redChannel=0) Set Blue and Red channels to 0, keeping Green channel intact
    elif ftype == "blue_tint":
        img[:, :, 1] = img[:, :, 2] = 0 # (greenChannel=redChannel=0) Set Green and Red channels to 0, keeping Blue channel intact
    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        # The cv2.Sobel function is used to compute the Sobel edge detection in the x-direction. The parameters are as follows: gray is the input grayscale image, 
            # cv2.CV_64F specifies the desired depth of the output image (64-bit floating point). In OpenCV, depth means the data type (precision) used to store each pixel value in the output image. It determines how much memory and accuracy each pixel uses. High precision decimal values can be stored in the output image, which is important for edge detection to capture subtle changes in intensity. 
            # 1 indicates that we want to compute the derivative in the x-direction; This means calculate the change in intensity along the horizontal direction (x-axis). It detects vertical edges in the image. Because when brightness changes left to right, it indicates a vertical boundary.
            # “do not calculate vertical (y-axis) changes in brightness.”. 0 indicates that we do not want to compute the brightness changes in the y-direction,  
            # ksize=3 specifies the size of the Sobel kernel (3x3). ie 3x3 matrixis used(3 rows 3 columns)
            # 1️⃣ What is a Kernel?
# A kernel (also called a filter or mask) is a small matrix of numbers used to process an image.
# It “slides” over the image.
# At each position, it performs mathematical operations on the pixel values underneath.
# This helps detect patterns like edges, blurring, sharpening, etc.
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        # 0 means ignore left-right changes . 1 → detect top-bottom changes → horizontal edges.  a 3×3 matrix
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
# sobel x → detects vertical edges
# sobel y → detects horizontal edges
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
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif ftype == "canny":
# Thresholds tell the Canny algorithm which gradients to consider as edges.
# Canny uses two thresholds: lower_thresh, upper_thresh.
# Pixels with gradient above upper_thresh → always kept as edges
# Pixels with gradient below lower_thresh → ignored
# Pixels between the two → kept if near strong edges         
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    elif ftype == "cartoon": # creates a cartoon effect from an image using OpenCV. cartoon-like appearance. 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5) 
        # medianBlur: Removes noise, Keeps edges sharp, preserves edges, removes small unwanted details
        # 5 is the kernel size for the median blur. Replaces each pixel with the median value. A larger kernel size will result in a stronger blurring effect, while a smaller kernel size will preserve more details. In this case, a kernel size of 5 means that a 5x5 neighborhood of pixels will be used to compute the median value for each pixel in the grayscale image. This helps to reduce noise while preserving edges, which is important for creating a cartoon-like effect.
        edges = cv2.adaptiveThreshold( # Detect Edges (Adaptive Threshold). Converts image into black and white edges.
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        ) 
# Pixels become either:
# white (255) → edges
# black (0) → background

# Why "adaptive"?
# Threshold changes based on local area
# Works well under different lighting

# Parameters:
# 9 → neighborhood size (size of the local area used to calculate the threshold. For each pixel, OpenCV looks at a 9 × 9 surrounding area. It calculates the average intensity of those pixels. 👉 That average is used to decide whether the pixel is: black (0) or white (255))
# Must be odd number (3, 5, 7, 9, …)

# 9 → constant subtracted
# 👉 This is a number subtracted from the calculated threshold.
# Threshold = (mean of neighborhood) - C
# Why Subtract C?
# 👉 It helps control how strict the edge detection is.

# 👉 Result: bold cartoon-like outlines
        color = cv2.bilateralFilter(image, 9, 300, 300)
        # 👉 Smooths colors but keeps edges.Bilateral filter → smooth + keeps edges ✅
        # 9 → neighborhood size
        # 300, 300 → color & space smoothing strength
        # 👉 Result: flat, paint-like colors
        img = cv2.bitwise_and(color, color, mask=edges) # Combine Edges + Color

# Original Image
#       ↓
# Grayscale → simplify (Simplify image)
#       ↓
# Median Blur → remove noise
#       ↓
# Adaptive Threshold → detect edges
#       ↓
# Bilateral Filter → smooth colors
#       ↓
# Combine(Bitwise AND) → cartoon effect 🎨        
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    ftype = "original"
    print("Keys: r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t=Cartoon, q=Quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break
        out = apply_filter(frame, ftype)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            # waitKey(1) waits for 1 millisecond for a key press. If the 'r' key is pressed, it sets ftype to "red_tint", which will apply the red tint filter to the video feed.
# & 0xFF ensures we only get the last 8 bits of the key value, which matches the ASCII code. 
            # ord('r') This converts the character 'r' into its ASCII value. 
            ftype = "red_tint"
        elif key == ord('g'):
            ftype = "green_tint"
        elif key == ord('b'):
            ftype = "blue_tint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('t'):
            ftype = "cartoon"
        elif key == ord('q'):
            break
    # Release the webcam capture and close the window (if any open window)    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__": # Every Python file has a special built-in variable called __name__. We use this for: runs when the file is executed directly. When a Python file is run directly, __name__ is set to "__main__"
    main()
