import cv2

# Load pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # load the Haar Cascade XML file for frontal face detection from OpenCV's data directory.
# data is a module (folder reference) inside OpenCV.
# It contains paths to built-in datasets and files that come with OpenCV.
# This gives the directory path where OpenCV stores Haar Cascade XML files.
# So cv2.data simply helps Python find OpenCV’s internal data files.

# haarcascades is a folder inside the OpenCV data directory.
# This folder contains pre-trained Haar Cascade models used for detecting objects.

# Examples of files inside it:
# haarcascade_frontalface_default.xml
# haarcascade_eye.xml
# haarcascade_smile.xml
# haarcascade_fullbody.xml
# haarcascade_upperbody.xml

# Initialize video capture (use webcam)
cap = cv2.VideoCapture(0) # start video capture from the default webcam (index 0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read() # cap is a video capture object created using OpenCV (in line 21). cap is used to access the camera or video file.
    # read() is a method of the video capture object. read() captures a single frame from the video source (webcam in this case) and returns two values:ret and frame.
# ret:
# ret means return value (a boolean).
# True → frame was successfully captured
# False → frame was not captured (camera problem or video ended)

# frame:
# frame is the actual image captured from the camera.
# It is stored as a NumPy array (image matrix).


# if frame capture was unsuccessful, print an error message and break the loop
    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert frame to grayscale (face detection works better in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # face_cascade is a pre-trained classifier used to detect faces. It uses the Haar Cascade Classifier method to detect faces in the image.
# detectMultiScale()
# This function detects objects (faces) at different sizes in the image.

#✅ scaleFactor = 1.1 ( zooming out the image repeatedly to find faces of different sizes.)
# This controls how much the image size is reduced at each step.
# 1.1 means the image size is reduced by 10% each time.
# Smaller values → more accurate but slower.
# Larger values → faster but may miss faces.

# Recommended range
# scaleFactor = 1.1 to 1.3 ✅

# | Value          | Effect                                              |
# | -------------- | --------------------------------------------------- |
# | **1.05 – 1.1** | Very accurate, detects small faces well, **slower** |
# | **1.1 – 1.2**  | Balanced, **good accuracy and speed**               |
# | **1.3 – 1.4**  | Faster detection, may **miss small faces**          |


#✅ minNeighbors = 5
# This controls how many nearby detections are required to confirm a face.
# Higher value → fewer false detections
# Lower value → detects more faces but may include false ones

# minNeighbors = 3 → detects more faces, may include false ones
# minNeighbors = 5 → balanced detection
# minNeighbors = 8 → strict, fewer faces, very few false positives

# Example:
# 3 → more detections (less strict)
# 5 → balanced
# 8 → very strict

# minSize = (30, 30)
# This sets the minimum size of the face to detect.
# (30,30) means the smallest detectable face is 30×30 pixels.
# Smaller faces will be ignored.

    # Draw rectangles around faces
    for (x, y, w, h) in faces: # faces contains the coordinates of detected faces
# | Variable | Meaning                                             |
# | -------- | --------------------------------------------------- |
# | **x**    | X-coordinate of the **top-left corner** of the face |
# | **y**    | Y-coordinate of the **top-left corner** of the face |
# | **w**    | **Width** of the face rectangle                     |
# | **h**    | **Height** of the face rectangle                    |

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Parameters:        
# frame → the image where the rectangle is drawn
# (x, y) → top-left corner of the rectangle
# (x + w, y + h) → bottom-right corner
# (255, 0, 0) → rectangle color (blue in BGR format)
# 2 → thickness of the rectangle

# Visual idea
# (x,y) -------------------
#   |                      |
#   |        FACE          |  h (height)
#   |                      |
#   ------------------------
#          w (width)

# x,y → starting position
# w → width of face
# h → height of face


    # Display the count of faces
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'People Count: {len(faces)}', (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA) # (10, 30) is the position of the text on the frame (10 pixels from the left and 30 pixels from the top). font is the font style used for the text. 1 is the font scale (size of the text). (255, 0, 0) is the color of the text (blue in BGR format). 2 is the thickness of the text. cv2.LINE_AA is the line type (anti-aliased for smoother text).
 
    # Display the frame with face detection and people count
    cv2.imshow('Face Tracking and Counting', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # waitKey(1) waits for 1 millisecond for a key press. If the 'q' key is pressed, it breaks the loop and exits the program.
# & 0xFF ensures we only get the last 8 bits of the key value, which matches the ASCII code.   
#  ord('q') This converts the character 'q' into its ASCII value. 

# ✔ For your face detection webcam program, cv2.waitKey(1) is the correct choice because the video must keep updating frame by frame.
# Why 1 is used
# 1 millisecond is used because the program is running in a video loop (webcam frames).
# Reasons:
# It makes the video run smoothly
# Frames update very fast
# Still allows the program to detect a key press  
# The camera keeps giving a new frame every time cap.read() is called. The waitKey(1) just gives the program a tiny break between frames and lets OpenCV handle the GUI and keyboard input.  So web can detect multiple images and also detect key presses without freezing the video.

# Using cv2.waitKey(0):: ERROR 🚫
# cv2.waitKey(0)
# Waits forever until a key is pressed.
# Program pauses on the current frame.
# Video does not move forward until you press a key.
# Output: You see only the first frame (or current frame) frozen until key press.

# Release the webcam capture and close the window (if any open window)
cap.release()
cv2.destroyAllWindows()