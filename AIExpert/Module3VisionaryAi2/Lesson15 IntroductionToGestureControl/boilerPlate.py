"""
Hand Gesture Detection (Boilerplate for Students)
Goal: Detect simple gestures using MediaPipe Hands + OpenCV

Time plan (25 mins):
1) Run the starter and confirm webcam + landmarks work (5 mins)
2) Add gesture logic in detect_gesture() (10 mins)
3) Display gesture + fingertip dots (7 mins)
4) Extra challenge: show Left/Right label and change colors (3 mins)
"""

import cv2
import mediapipe as mp

# ---------- 1) Setup MediaPipe ----------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# NOTE: Keep these values as given for stable tracking
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------- 2) Start Webcam ----------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    raise SystemExit

print("Hand Tracking Started! Press 'q' to quit.")

# ---------- 3) Helper: Gesture Detector ----------
def detect_gesture(hand_landmarks):
    """
    TASK: Return one of these strings:
    - "Open"
    - "Closed Fist"
    - "Partial"

    Hint:
    - Thumb tip id = 4
    - Index tip id = 8
    - Middle tip id = 12
    - Ring tip id = 16
    - Pinky tip id = 20

    Use these lists to compare tip positions with lower joints.
    """
    landmarks = hand_landmarks.landmark

    tip_ids = [4, 8, 12, 16, 20]     # fingertips
    pip_ids = [2, 6, 10, 14, 18]     # near-fingertip joints (good for open/close check)

    # TODO 1: Count how many fingers are "extended"
    extended = 0

    # Thumb check (x-axis)
    # TODO 2: If thumb tip is far enough from thumb joint in X direction, count as extended
    # Example logic:
    # if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
    #     extended += 1

    # Other 4 fingers check (y-axis)
    # TODO 3: For index to pinky:
    # If fingertip is ABOVE its joint (smaller y), it’s extended
    # for i in range(1, 5):
    #     if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
    #         extended += 1

    # TODO 4: Decide gesture based on extended count
    # If extended >= 4 -> "Open"
    # If extended <= 1 -> "Closed Fist"
    # Else -> "Partial"

    return "Partial"  # <- replace this with your final return

# ---------- 4) Main Loop ----------
while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip for mirror view
    frame = cv2.flip(frame,
