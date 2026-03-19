import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Hand Tracking Started! Press 'q' to quit.")

def detect_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 18]
    extended = 0

    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
        extended += 1

    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
            extended += 1

    if extended >= 4:
        return "Open"
    elif extended <= 1:
        return "Closed Fist"
    else:
        return "Partial"

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1) # 1 means you're flipping the image horizontally. 
# 0 → Flip vertically (upside down)
# 1 → Flip horizontally (mirror image), 1 creates a mirror effect, which is commonly used in webcam apps so movements feel natural (like looking in a mirror)
# -1 → Flip both vertically and horizontally
    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    gesture = "No hand detected"

    if results.multi_hand_landmarks and results.multi_handedness:
# 🔹 multi_hand_landmarks
# This contains the detected hand keypoints (landmarks). For each hand, it gives 21 points (like fingertips, joints, wrist). Each point has x, y, z coordinates. 👉 Example: index finger tip, thumb tip, wrist, etc.
# So:
# If no hands are detected → None
# If hands are detected → a list of landmarks for each hand

# 🔹 multi_handedness
# This tells you whether each detected hand is:
# "Left" ✋
# "Right" 🤚 

# So:
# If no hands → None
# If hands detected → a list with handedness info for each hand

# 🔹 Why use both in the if condition?
# if results.multi_hand_landmarks and results.multi_handedness:
# This ensures:
# ✔ Hands are detected
# ✔ AND you also know which hand is left/right

# 🔹 Simple analogy
# multi_hand_landmarks → “Where are the fingers?”
# multi_handedness → “Is it left or right hand?”

        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks): # enumerate() → gives: idx → index (0, 1) 0=right; 1= left
# 👉 If 2 hands are detected:
# idx = 0 → first hand
# idx = 1 → second hand
            hand_label = results.multi_handedness[idx].classification[0].label # multi_handedness[idx] classification[0].label → gives: "Left" or "Right"
            gesture = detect_gesture(hand_landmarks) # Detect gesture
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
# Draws:
# 21 key points (dots)
# Lines connecting them (hand skeleton)
# mp_hands.HAND_CONNECTIONS → defines how points are connected

            fingertip_ids = [4, 8, 12, 16, 20]

            for tip_id in fingertip_ids:
                lm = hand_landmarks.landmark[tip_id] # lm stands for landmark
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)
                cv2.putText(frame, str(tip_id), (x - 5, y - 15), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2) # 0.5 → Font scale (size of text), 2 → Thickness

            wrist = hand_landmarks.landmark[0]
            wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)
            cv2.putText(frame, f"{hand_label} Hand", (wrist_x - 40, wrist_y + 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    status_color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 30), # 0, 165, 255 ? orange?
               cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

    cv2.imshow("Hand Gesture Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()