# To run code: py -3.10 "C:\Users\vishn\Documents\CodingalCheckActivity\AIExpert\Module3VisionaryAi2\Lesson18 Gesture-ControlledPhotoApp\AcExplained.py"

# 🧩 Summary
# Gestures:
# 🤏 Thumb + Index → Capture photo
# 👍 Thumb + Middle → Toggle SEPIA / NEGATIVE
# 👍 Thumb + Ring → Toggle BLUR / GLITCH
# 👍 Thumb + Pinky → Toggle EDGE / CARTOON

# ⚡ Key Idea
# Everything is based on distance between fingertips in pixels:
# Small distance → gesture detected
# Large distance → no gesture
import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands # H = mp.solutions.hands creates an alias so you don’t repeatedly type the long path mp.solutions.hands
TIP = H.HandLandmark # TIP = H.HandLandmark creates an alias for the landmark enum class that contains all 21 landmark names. HandLandmark is an enum (named index list) that maps landmark names to their internal index positions inside hand.landmark
ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP,
} # ids is a dictionary designed for clean gesture logic: instead of remembering indices, you write ids["thumb"] or ids["index"]
# "thumb", "index", "middle", "ring", "pinky" are just labels you chose for readability; they are not required by MediaPipe. 
# TIP.THUMB_TIP, TIP.INDEX_FINGER_TIP, etc. specifically refer to fingertip landmarks (not knuckles or joints), which are the best points for pinch/touch gestures. This mapping avoids mistakes like accidentally using the wrong joint landmark and makes the code scalable (you can add more landmarks like WRIST later in the same style)

hands = H.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) # H.Hands(...) creates the main MediaPipe Hands object that you call on every frame using hands.process(image_rgb). This object runs two key steps internally:
# (1) detection (finding hands in a frame) and
# (2) tracking (keeping the same hand landmarks stable across frames once a hand is found).

# To initialize MediaPipe’s Hand Detection + Tracking pipeline (hands) and load helper functions (draw) that can draw hand landmarks and connections on the webcam frame.
draw = mp.solutions.drawing_utils
pairs = {"middle":("SEPIA","NEGATIVE"), "ring":("BLUR","GLITCH"), "pinky":("EDGE","CARTOON")} # pairs maps a finger name to a tuple of two filter names, e.g., touching "ring" toggles between "BLUR" and "GLITCH".The keys "middle", "ring", "pinky" are chosen because the thumb can comfortably reach them for “tap” gestures
st = {k:0 for k in pairs}; cur = "SEPIA" # st is the current toggle state of each finger. st = {k:0 for k in pairs} it creates a toggle tracker like {"middle":0,"ring":0,"pinky":0} where 0 means “use the first filter in the pair” and 1 means “use the second”
# current ie, cur = "SEPIA" sets the starting filter so the app has a default effect before any gesture is used

# DEB = 0.6 (seconds) is the debounce window for filter switching; it limits filter changes to at most ~1 every 0.6 seconds even if the thumb stays near a finger across many frames
# CAP = 1.2 (seconds) is the capture cooldown; it prevents saving multiple pictures too quickly (especially if detection flickers)
DEB, CAP, TT, TP = 0.6, 1.2, 30, 20
# TT = 30 (pixels) is the tap threshold for thumb-to-(middle/ring/pinky) proximity; larger = easier to trigger but more accidental triggers
# TP = 20 (pixels) is the pinch threshold for thumb-to-index proximity; smaller than TT because pinch should be more intentional
# la = lc = 0 initializes “last action time” (la) and “last capture time” (lc) so the first gesture can trigger immediately
# pinch_on = False tracks whether a pinch is currently in progress, enabling “capture once per pinch” behavior
la = lc = 0; pinch_on = False
MAIN, POP = "Gesture-Controlled Photo App", "Captured (ESC / Close to resume)" # MAIN is the window title for the live stream; POP (captured image popup window) is the window title for the captured-image preview
paused = False; freeze = None # paused = False starts the app in live mode; when True, the app shows a frozen frame until the user resumes
# freeze = None will later hold a copy of the captured frame (out.copy()) so it stays unchanged while paused
SEPIA_M = np.array([[0.272,0.534,0.131],[0.349,0.686,0.168],[0.393,0.769,0.189]])
# to convert a normal image into a sepia-toned image. Gives an image a warm brown / vintage look . Like old photographs. Matrix with cell value [B, G, R]  # Blue, Green, Red
# We use this in coming lines of code, here its just declared.
 # SEPIA_M is a 3×3 sepia matrix used with cv2.transform; it mixes channels to create warm brown tones efficiently without per-pixel Python loops

def apply(img, t):
# img is a NumPy image array from OpenCV in BGR format, typically shaped (height, width, 3).
# t is the active filter name string that selects which branch runs ("SEPIA", "NEGATIVE", "BLUR", "GLITCH", "EDGE", "CARTOON").
# Sepia is a brownish color tone used to make images look old and vintage
# A negative image is when all colors are inverted (opposite colors). Light becomes dark, Dark becomes light, Colors become their opposites
    if t == "SEPIA": return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8) # cv2.transform(img, SEPIA_M) applies a 3×3 color matrix; np.clip(..., 0, 255) prevents overflow/underflow; astype(np.uint8) restores standard image dtype.
    if t == "NEGATIVE": return cv2.bitwise_not(img) # cv2.bitwise_not(img) produces a negative effect by inverting pixel values.
    if t == "BLUR": return cv2.GaussianBlur(img, (15, 15), 0) # cv2.GaussianBlur(img, (15, 15), 0) uses an odd kernel size to control blur strength; sigma 0 tells OpenCV to auto-pick the sigma value. (15, 15) is the kernel size
    # 0 = sigma (blur intensity). OpenCV automatically calculates it based on kernel size
    if t == "GLITCH":
        # img.shape[:2] 👉 It takes only the first two values. 3rd value is number of color channels (usually 3)- this is ignored
        h,w = img.shape[:2]; r,g,b = img[:,:,2], img[:,:,1], img[:,:,0] # img[:,:,2] → Red channel ; img[:,:,1] → Green channel; img[:,:,0] → Blue channel
        # This shifted red and blue separately
# Before splitting
# Blue = 100
# Green = 150
# Red = 200

# After splitting:
# r = 200
# g = 150
# b = 100
        return cv2.merge([np.roll(b, -int(0.02*w), 1), g, np.roll(r, int(0.04*w), 1)]) # np.roll(channel, shift, axis=1) shifts pixels horizontally; shifts are computed from w to make the glitch scale with image size.
    # Shifting color channels, Then merging them back
    # b → blue channel, np.roll(...) → shifts pixels, -int(0.02*w) → shift left, 1 → horizontal direction, 👉 Blue moves slightly left
    if t == "EDGE": return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160) # cv2.Canny(gray, 80, 160) uses lower/upper thresholds where 80 helps include weaker edges and 160 confirms strong edges.
    if t == "CARTOON":
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        e = cv2.adaptiveThreshold(cv2.medianBlur(g, 7), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2) 
        # Means a 7×7 neighborhood, Used to remove noise. 255 is the maximum pixel value
        # 9: is Size of area used to calculate threshold, Means 9×9 pixel region
# 2 ? 👉 It is a constant subtracted from mean, 👉 2 = fine adjustment for better edges

        # cv2.medianBlur(g, 7) reduces noise before edge masking; 7 must be odd and larger values smooth more. cv2.adaptiveThreshold(..., 255, ..., 9, 2) creates a binary edge mask using local neighborhoods; 9 controls neighborhood size and 2 controls strictness.
        c = cv2.bilateralFilter(img, 9, 75, 75) # this line is for the cartoon effect. 
        # 9 is Size of the pixel neighborhood. 75 → SigmaColor, ie how much colors can mix. 75 → SigmaSpace ie How far pixels influence each other. For smoothing
        return cv2.bitwise_and(c, c, mask=e) # cv2.bilateralFilter(img, 9, 75, 75) smooths colors while preserving edges; larger sigma values increase smoothing. cv2.bitwise_and(c, c, mask=e) applies the edge mask onto the smoothed color image to produce the cartoon look.
    return img

cap = cv2.VideoCapture(0)
if not cap.isOpened(): print("Error: Could not access the webcam."); exit()
cv2.namedWindow(MAIN, cv2.WINDOW_NORMAL) #cv2.namedWindow creates a window with the name in MAIN (eg: "gesture-Controlled Photo App").  cv2.WINDOW_NORMAL makes window resizable for comfort viewing

while True:
    if paused: # freeze on capture + resume
        # paused is a control flag that switches the app from “live camera mode” to “preview/freeze mode.”
        cv2.imshow(MAIN, freeze) # cv2.imshow(MAIN, freeze) displays the saved frozen frame instead of a new webcam frame
        k = cv2.waitKey(50) & 0xFF # cv2.waitKey(50) pauses for ~50ms and captures keyboard input; the value controls responsiveness vs CPU load. & 0xFF keeps only the lowest 8 bits of the key code, improving cross-platform key handling.
        if k == ord("q"): break # ord("q") converts the character q to its ASCII code so you can compare it with waitKey output.
        if k == 27: # k == 27 checks for the ESC key (27 is ESC keycode).
            paused = False; pinch_on = False # pinch_on = False is reset to prevent immediate re-capture when returning to live mode (gesture state cleanup).
            try: cv2.destroyWindow(POP) # cv2.destroyWindow(POP) closes the popup preview window; wrapped in try/except to avoid crashing if already closed.
            except: pass
            continue # continue skips the rest of the loop so the app stays paused and does not read/process live frames.
        try:
            if cv2.getWindowProperty(POP, cv2.WND_PROP_VISIBLE) <= 0: paused = False; pinch_on = False # cv2.getWindowProperty(POP, cv2.WND_PROP_VISIBLE) detects whether the popup is still open; <= 0 means closed/hidden.
        except cv2.error:
            paused = False; pinch_on = False
        continue

    ok, img = cap.read() # cap.read() returns (ok, img) where ok is a success flag and img is the frame image as a NumPy array.
    if not ok: break
    img = cv2.flip(img, 1); h, w = img.shape[:2] # cv2.flip(img, 1) uses flipCode=1 to mirror horizontally (more natural gesture interaction). img.shape[:2] returns (height, width); this is needed for converting normalized landmarks to pixels.
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # converts OpenCV’s BGR frame to RGB because MediaPipe’s model is trained/expected on RGB. hands.process(...) runs detection + tracking and returns a result object (res) that can include landmarks and handedness.
    now = time.time(); capture = False # time.time() gives a floating-point timestamp (seconds since epoch), used for debounce/cooldowns. capture = False resets the capture request each frame so a photo saves only when a new gesture triggers it.

    if res.multi_hand_landmarks: # runs only when MediaPipe successfully detects at least one hand in the current frame.
        hand = res.multi_hand_landmarks[0]; draw.draw_landmarks(img, hand, H.HAND_CONNECTIONS) # hand = res.multi_hand_landmarks[0] selects the first detected hand (simple approach; avoids handling multiple hands at once). draw.draw_landmarks(img, hand, H.HAND_CONNECTIONS) draws landmark points and the connection lines (hand skeleton) for debugging and better UX.
        lm = hand.landmark; tips = {k:(int(lm[v].x*w), int(lm[v].y*h)) for k,v in ids.items()} # lm = hand.landmark is the list of 21 landmarks; each landmark has normalized coordinates x, y in the range 0.0 → 1.0.
        tx,ty = tips["thumb"]; ix,iy = tips["index"] # tips = {k:(int(lm[v].xw), int(lm[v].yh)) for k,v in ids.items()} converts normalized fingertip coordinates into pixel positions using frame width w and height h; ids supplies which landmark index belongs to which finger tip.
        # tx, ty = tips["thumb"]; ix, iy = tips["index"] extracts thumb and index fingertip pixel coordinates for pinch detection.

# lm[v].x and lm[v].y → normalized values (0 → 1)
# Multiply by w and h → convert to pixel coordinates
# Result:: tips = {
#   "thumb": (x, y),
#   "index": (x, y),
#   "middle": (x, y),
#   ...
# }

# 👍 Get thumb & index positions
# tx,ty = tips["thumb"]
# ix,iy = tips["index"]

        pinch = abs(tx-ix) < TP and abs(ty-iy) < TP # pinch = abs(tx-ix) < TP and abs(ty-iy) < TP defines pinch as “thumb and index are within TP pixels horizontally and vertically”; smaller TP makes pinch stricter and reduces accidental captures.

# 🤏 Detect “pinch” (capture gesture)
# pinch = abs(tx-ix) < TP and abs(ty-iy) < TP
# Meaning:
# Check if thumb and index are close enough
# TP = threshold (like 20 pixels)
# Logic:
# If horizontal distance < TP
# AND vertical distance < TP
# → fingers are touching → pinch = True

        if pinch and not pinch_on and now-lc > CAP: pinch_on = True; capture = True; lc = now # if pinch and not pinch_on and now-lc > CAP: ensures capture happens only once per pinch and only after a cooldown; CAP is in seconds, and lc stores the previous capture time.capture = True; lc = now
        # pinch_on = True locks the pinch state so keeping fingers together doesn’t spam captures across multiple frames.
        # capture = True signals the outer loop to save the image this frame.
        # lc = now updates last capture time so cooldown can be enforced next time.
# pinch → fingers touching
# not pinch_on → prevents repeated triggering
# now - lc > CAP → cooldown (e.g. 1.2 sec)

# Action:
# pinch_on = True
# capture = True
# lc = now
# 👉 So one pinch = one photo

# 🔄 Reset pinch state
        if not pinch and pinch_on: pinch_on = False # if not pinch and pinch_on: pinch_on = False resets the lock when pinch is released, enabling the next pinch to work. When fingers separate → reset. Allows next capture later

        # Detect filter-change gesture (filter changes only happen when NOT pinching)
        if not pinch: # if not pinch: prevents filter switching while pinching, avoiding two actions triggering at the same time. 
            # Check thumb touching other fingers
            t = next((k for k in pairs if abs(tx-tips[k][0]) < TT and abs(ty-tips[k][1]) < TT), None) # t = next((k for k in pairs if abs(tx-tips[k][0]) < TT and abs(ty-tips[k][1]) < TT), None) checks thumb proximity to target fingertips (middle/ring/pinky) and returns the first match; TT is the touch threshold in pixels.
# Loops through:
# middle
# ring
# pinky
# Checks thumb close to that finger? If yes → returns that finger name (t) ; If none match → t = None

# Toggle filters
# t → a finger was touched;; now - la > DEB → debounce delay (avoid rapid switching)
# st[t]
# Keeps track of toggle state (0 or 1)
# cur = pairs[t][st[t]]
# Selects current filter
# st[t] ^= 1
# Flips 0 ↔ 1 (toggle)
# Example Flow:
# Touch thumb + middle:
# First time → SEPIA
# Next time → NEGATIVE
# Next → SEPIA again
            if t and now-la > DEB: cur = pairs[t][st[t]]; st[t] ^= 1;  la = now; print("Filter:", cur) # if t and now-la > DEB: applies debounce for filter changes; DEB is in seconds and la stores last filter-change time. 
            # cur = pairs[t][st[t]] selects the filter from the pair (index 0 or 1) based on the toggle state for that finger.
            # st[t] ^= 1 flips the toggle state between 0 and 1 so the next touch of the same finger switches to the other filter.
# la = now updates last action time so debounce is enforced for future filter changes.
# print("Filter:", cur) logs the filter change so the user can confirm the action even if they miss it visually.
    out = apply(img, cur) # out is the final frame that will be shown in the window and used for saving a photo.
    # apply(img, cur) picks the correct transformation based on cur and returns the processed image.
    # Takes original image; Applies selected filter; Stores result in out

    # cur is a string like "SEPIA", "BLUR", "EDGE", etc., representing the active filter.
    # The EDGE filter uses cv2.Canny, which returns a single-channel (grayscale) image instead of (h, w, 3).
    if cur == "EDGE": out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR) # cv2.cvtColor(out, cv2.COLOR_GRAY2BGR) converts (h, w) into (h, w, 3) by duplicating the grayscale channel into B, G, and R. This conversion keeps the pipeline consistent so text overlays (cv2.putText), saving (cv2.imwrite), and window display behave reliably across all filters.

    if capture: # capture is a per-frame flag that becomes True only when the pinch/cooldown logic triggers a valid photo capture.
        # f"picture_{int(now)}.jpg" creates a timestamp-based filename; int(now) removes decimals and helps keep filenames unique.
        # .jpg saves storage efficiently, but it is lossy; using .png would preserve quality at larger file size.
        # cv2.imwrite(name, out) saves the image to the current working directory; out is what gets saved (already filtered).
        # print("Saved:", name) provides immediate confirmation and shows the exact filename created.
        name = f"picture_{int(now)}.jpg"; cv2.imwrite(name, out); print("Saved:", name)
        paused, freeze = True, out.copy(); cv2.imshow(POP, freeze) # paused = True switches the main loop into pause mode so no new frames are processed until the user resumes.
        # freeze = out.copy() stores a stable snapshot; .copy() ensures the frozen image won’t be modified by later operations.
        # cv2.imshow(POP, freeze) displays the captured snapshot in a popup preview window titled by POP.

    cv2.imshow(MAIN, out) # cv2.imshow(MAIN, out) displays the frame in a window titled by MAIN; out is the final filtered frame.
    if cv2.waitKey(1) & 0xFF == ord("q"): break # cv2.waitKey(1) is required for window refresh and keyboard input; 1 controls how long the program waits per loop iteration. & 0xFF keeps only the lowest 8 bits of the key code, improving cross-platform reliability. ord("q") converts the character q into its ASCII key code for comparison. break exits the loop cleanly when the user wants to quit.

cap.release(); cv2.destroyAllWindows(); hands.close() # cap.release() releases the webcam hardware handle so it’s not locked after the program ends. cv2.destroyAllWindows() closes all OpenCV windows to avoid hanging UI processes. hands.close() properly shuts down the MediaPipe Hands pipeline and frees model/tracking resources.