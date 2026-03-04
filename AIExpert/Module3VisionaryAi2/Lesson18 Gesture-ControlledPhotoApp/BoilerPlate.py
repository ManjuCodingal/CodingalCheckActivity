# =========================
import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands
TIP = H.HandLandmark
ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP,
}

# =========================
# CONTINUE WITH COMMENTS (BOILERPLATE EXPLANATION)
# =========================

# 1) Setup MediaPipe Hands (detect + track hand landmarks)
#    - hands = H.Hands(min_detection_confidence=..., min_tracking_confidence=...)
#    - draw = mp.solutions.drawing_utils (to draw dots/lines)

# 2) Decide gesture controls
#    - pairs: which finger toggles which 2 filters (middle/ring/pinky)
#    - st: 0/1 toggle state for each finger
#    - cur: currently selected filter

# 3) Thresholds + timers (to avoid accidental triggers)
#    - TT: thumb-to-finger “touch” distance
#    - TP: thumb-index “pinch” distance (capture)
#    - DEB: debounce time for toggles
#    - CAP: cooldown time for captures
#    - la/lc: last toggle/capture time, pinch_on: pinch state flag

# 4) Windows + pause mode
#    - MAIN: live window, POP: captured window
#    - paused=True shows freeze frame until ESC/close

# 5) Create apply(img, filter_name)
#    - Returns filtered image (SEPIA/NEGATIVE/BLUR/GLITCH/EDGE/CARTOON)
#    - If EDGE returns grayscale, convert back to BGR before display/save

# 6) Start webcam
#    - cap = cv2.VideoCapture(0)
#    - if not cap.isOpened(): print error and exit

# 7) Main loop
#    - If paused: show freeze, ESC/close to resume, 'q' to quit
#    - Else: read frame, flip, convert to RGB, run hands.process()

# 8) If hand detected
#    - Draw landmarks
#    - Convert landmark coords to pixel coords for tips using ids

# 9) Pinch to capture (thumb + index close)
#    - If pinch just started AND cooldown passed -> capture=True

# 10) Thumb touch to toggle filter (only when not pinching)
#    - If thumb near middle/ring/pinky AND debounce passed -> toggle cur

# 11) Apply filter + show output
#    - out = apply(img, cur)
#    - If capture: save file, set paused=True, freeze=out.copy(), show POP
#    - cv2.imshow(MAIN, out), press 'q' to quit

# 12) Cleanup
#    - cap.release(), cv2.destroyAllWindows(), hands.close()
