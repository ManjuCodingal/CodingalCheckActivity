# 1) Imports
# - cv2 for webcam + drawing
# - mediapipe for hand tracking
# - numpy for distance + interpolation
# - pycaw for system volume control (Windows)
# - screen_brightness_control for brightness control

# 2) Setup MediaPipe Hands
# - Hands = mp.solutions.hands
# - hands = Hands.Hands(min_detection_confidence=..., min_tracking_confidence=...)
# - draw = mp.solutions.drawing_utils
# - TH, IX = landmark IDs for THUMB_TIP and INDEX_FINGER_TIP

# 3) Setup Volume Controller (Pycaw)
# - Get default output device (or speakers fallback)
# - Get EndpointVolume interface
# - Read min/max volume range
# - Wrap in try/except and exit on failure

# 4) Setup Webcam
# - cap = cv2.VideoCapture(0)
# - Validate cap.isOpened(), else exit

# 5) Create Window
# - WIN = "Hand Gesture Control"
# - cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

# 6) Main Loop (while True)
# - Read frame: ok, img = cap.read()
# - Break if not ok
# - Flip image for selfie view: img = cv2.flip(img, 1)
# - Get h, w from img.shape
# - Convert to RGB and run MediaPipe: res = hands.process(...)

# 7) Hand Detection Check
# - if res.multi_hand_landmarks and res.multi_handedness:

# 8) For each detected hand
# - label = handedness label ("Left" / "Right")
# - draw landmarks on frame
# - Extract thumb tip and index tip pixel positions using lm[TH], lm[IX]
# - Draw circles + line between thumb and index
# - Compute distance between those two points (np.hypot)

# 9) Gesture Mapping (important note)
# - Because the frame is flipped:
#   label == "Left"  -> real RIGHT hand -> VOLUME
#   label == "Right" -> real LEFT hand  -> BRIGHTNESS

# 10) Volume Control Block (real RIGHT hand)
# - Map distance -> volume range using np.interp
# - Set system volume via volctl.SetMasterVolumeLevel(...)
# - Draw volume bar + % text on left side

# 11) Brightness Control Block (real LEFT hand)
# - Map distance -> 0..100 brightness using np.interp
# - sbc.set_brightness(int_value)
# - Draw brightness bar + % text on right side

# 12) Display Frame
# - cv2.imshow(WIN, img)

# 13) Exit Controls
# - Read key with cv2.waitKey(1)
# - Exit if ESC or 'q'
# - Also exit if user clicks window close (X) using cv2.getWindowProperty

# 14) Cleanup
# - cap.release()
# - cv2.destroyAllWindows()
