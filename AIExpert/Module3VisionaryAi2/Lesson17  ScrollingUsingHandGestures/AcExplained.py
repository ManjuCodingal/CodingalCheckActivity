# To check output open and close hand (show backside of hand to camera, closed fist= scroll down, open fist= scroll up)

# Why  back of hand shown to camera in output checking?
# if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
#     fingers.append(1)
# This logic assumes the back of the hand is facing the camera
# If you show the palm:
# Thumb and finger positions may flip horizontally
# The y-coordinates can behave differently
# Gesture detection may fail or give wrong results

import cv2, time, pyautogui # TIme is used in Scroll delay control. time.time() gives the current time (in seconds)
# if (time.time() - last_scroll) > SCROLL_DELAY:
# - This ensures scrolling happens only once every 1 second
# Prevents too fast / uncontrollable scrolling
# 👉 Without this:  page would scroll very fast and uncontrollably

# pyautogui:: To control your computer (mouse/scroll) using code
# CRUX of pyautogui::  if gesture == "scroll_up": pyautogui.scroll(SCROLL_SPEED) # Scrolls up → positive value; Scrolls down → negative value;; elif gesture == "scroll_down": pyautogui.scroll(-SCROLL_SPEED)
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Configurations 
SCROLL_SPEED = 300 # Controls how much the page scrolls in one action. pyautogui.scroll(300)   # scroll up ; pyautogui.scroll(-300)  # scroll down. Bigger number → faster / longer scroll; Smaller number → slower / smoother scroll. 50 → slow scrolling 🐢, 300 → medium (your current) ⚖️, 1000 → very fast ⚡
SCROLL_DELAY = 1 # Time gap (in seconds) between scroll actions. 0.2 → very fast scrolling. 1 → controlled (your current). 2 → slower response
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness): # landmarks → hand points detected by MediaPipe. handedness → tells if hand is "Right" or "Left"
    fingers = [] # Empty list to store which fingers are open. If a finger is open → store 1
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP] # Stores IDs of finger tips. These are constants from MediaPipe. Used to check if fingers are open or closed
   
    # Check fingers (except thumb)
    for tip in tips: # Loop through each finger tip
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y: # tip - 2 refers to the joint just below the fingertip. (Difference between tip and joint below tip)
# | Part            | Landmark Index |
# | --------------- | -------------- |
# | Tip             | 8              |
# | Joint below tip | 6              |

            fingers.append(1) # Compares tip position with a lower joint
# tip → fingertip
# tip - 2 → joint below it
# 👉 If tip is higher (smaller y) → finger is open
# If finger is open → add 1 to list

# ✅ If finger is OPEN: Tip is above the joint # So: tip.y < joint.y  ✔️
# ❌ If finger is CLOSED: Tip is below the joint # So: tip.y > joint.y  ❌

    # Check thumb
    # Gets thumb tip and thumb joint positions
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1) # Thumb moves sideways, not up/down. So we check x-coordinate instead of y
# Logic:
# Right hand → thumb open if tip is to the right
# Left hand → thumb open if tip is to the left. If thumb is open → add 1
   
    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if len(fingers) == 0 else "none"
# ✅ sum(fingers) == 5::  All 5 fingers open ✋ → "scroll_up"
# ✅ len(fingers) == 0:: No fingers open (fist ✊) → "scroll_down"
# ❌ Otherwise:: Some fingers open → "none"

cap = cv2.VideoCapture(0) # represents webcam
cap.set(3, CAM_WIDTH) # Setting camera resolution +. 
# | Number | Meaning         |
# | ------ | --------------- |
# | `3`    | Frame width 📏  |
# | `4`    | Frame height 📐 | 👉 This makes your camera capture video at 640 × 480 resolution. Controls video quality, Affects performance (FPS)
cap.set(4, CAM_HEIGHT)
last_scroll = p_time = 0 # Initializes two variables at once. Both are set to 0
# 🖱️ last_scroll
# Stores the last time scrolling happened
# Used to control scroll delay Eg:: if (time.time() - last_scroll) > SCROLL_DELAY:

# 🎥 p_time (previous time)
# Stores the previous frame time
# Used to calculate FPS Eg:: fps = 1 / (time.time() - p_time)

print("Gesture Scroll Control Active\nOpen palm: Scroll Up\nFist: Scroll Down\nPress 'q' to exit")

while cap.isOpened(): # Runs continuously while the camera is open. Keeps your program live (real-time processing)
    success, img = cap.read() # success → True if frame captured; img → the image (frame from webcam)
    if not success: break # If camera fails → stop the loop

    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1) # Convert and flip image. Color conversion: OpenCV uses BGR, MediaPipe needs RGB. Flip image:: 1 → horizontal flip (mirror effect). Makes it feel natural (like looking in a mirror)

    # ✋ Detect hands
    results = hands.process(img) # Sends image to MediaPipe
# Detects:
# Hand landmarks
# Hand type (left/right)
    gesture, handedness = "none", "Unknown" # If no hand is detected: Gesture = none and Hand = unknown
   
# 🖐️ Check if hands detected
    if results.multi_hand_landmarks: # Runs only if at least one hand is found
        # Loop through detected hands. hand → landmarks (positions of fingers); handedness_info → tells left or right hand
        for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness): 
            handedness = handedness_info.classification[0].label # Extracts "Left" or "Right"
            gesture = detect_gesture(hand, handedness) # Returns: "scroll_up", "scroll_down", "none"
            mp_drawing.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS) # Draws points and lines on the hand, Helps you see tracking visually

# makes hand gestures control the screen
            if (time.time() - last_scroll) > SCROLL_DELAY:  # Ensures scrolling happens once every 1 second. Prevents continuous rapid scrolling. Makes control stable
                if gesture == "scroll_up": pyautogui.scroll(SCROLL_SPEED) # Scrolls up → positive value; Scrolls down → negative value
                elif gesture == "scroll_down": pyautogui.scroll(-SCROLL_SPEED)
                last_scroll = time.time() # Updates last scroll time

    fps = 1/(time.time()-p_time) if (time.time()-p_time) > 0 else 0 # Only calculate FPS if time > 0, otherwise return 0
    # fps (Frames Per Second), Measures how fast your camera is processing frames. Helps monitor performance
    # 1 / (time per frame)-> If one frame takes 0.05 seconds, FPS = 1 / 0.05 = 20
    p_time = time.time() # Updates previous time for next calculation
    cv2.putText(img, f"FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}", (10,30), # 📝 Display text on screen. Shows: FPS, Hand (Left/Right), Gesture
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    cv2.imshow("Gesture Control", cv2.cvtColor(img, cv2.COLOR_RGB2BGR)) # Displays video feed, Converts back to BGR for OpenCV display
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

