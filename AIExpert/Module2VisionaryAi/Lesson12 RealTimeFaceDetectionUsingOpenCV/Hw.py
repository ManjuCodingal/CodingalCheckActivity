import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Loading Haarcascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load emotion model
model = load_model("emotion_model.hdf5")

emotion_labels = ["Angry", "Happy", "Sad", "Surprise", "Neutral"]

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error! Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error! Failed to capture image")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        # face crop 
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48,48))
        face = face / 255.0
        face = np.reshape(face, (1,48,48,1))

        pred = model.predict(face)
        emotion = emotion_labels[np.argmax(pred)]

        cv2.putText(frame, emotion, (x, y-10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f"People count: {len(faces)} ", (10,30), font, 1, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow("Face Tracking and Counting", frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2

# # Load Haarcascade for face detection
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Initialize webcam
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error! Could not open webcam")
#     exit()

# print("Press 'q' to quit")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error! Failed to capture frame")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30)
#     )

#     # Draw rectangles around faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     # Display people count
#     font = cv2.FONT_HERSHEY_COMPLEX
#     cv2.putText(frame, f"People count: {len(faces)}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

#     # Show the frame
#     cv2.imshow("Face Detection and Counting", frame)

#     # Press 'q' to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()