import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Finger tip landmark IDs
tip_ids = [4, 8, 12, 16, 20]

def get_finger_status(hand_landmarks):
    fingers = []

    # Thumb (special case: x comparison)
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers (y comparison)
    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def classify_gesture(fingers):
    total = sum(fingers)

    if total == 0:
        return "Closed Fist"
    elif total == 5:
        return "Open Hand"
    else:
        return "Partial"


# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Mirror image
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            fingers = get_finger_status(handLms)
            gesture = classify_gesture(fingers)

            # Display gesture
            cv2.putText(img, gesture, (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 255, 0), 3)

            # Debug: show finger status
            cv2.putText(img, f"Fingers: {fingers}", (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 0, 0), 2)

    cv2.imshow("Gesture Detection", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
# mp_draw = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not access the webcam.")
#     exit()

# print("Hand Tracking Started! Press 'q' to quit.")

# def detect_gesture(hand_landmarks):
#     landmarks = hand_landmarks.landmark
#     tip_ids = [4, 8, 12, 16, 20]
#     pip_ids = [2, 6, 10, 14, 18]
#     extended = 0

#     if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
#         extended += 1

#     for i in range(1, 5):
#         if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
#             extended += 1

#     if extended >= 4:
#         return "Open"
#     elif extended <= 1:
#         return "Closed Fist"
#     else:
#         return "Partial"

# while True:
#     success, frame = cap.read()
#     if not success:
#         break

#     frame = cv2.flip(frame, 1)
#     h, w, _ = frame.shape
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(frame_rgb)
#     gesture = "No hand detected"

#     if results.multi_hand_landmarks and results.multi_handedness:
#         for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
#             hand_label = results.multi_handedness[idx].classification[0].label
#             gesture = detect_gesture(hand_landmarks)
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             fingertip_ids = [4, 8, 12, 16, 20]
#             for tip_id in fingertip_ids:
#                 lm = hand_landmarks.landmark[tip_id]
#                 x, y = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)
#                 cv2.putText(frame, str(tip_id), (x - 5, y - 15),
#                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

#             wrist = hand_landmarks.landmark[0]
#             wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)
#             cv2.putText(frame, f"{hand_label} Hand", (wrist_x - 40, wrist_y + 30),
#                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

#     status_color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
#     cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
#                cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

#     cv2.imshow("Hand Gesture Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()