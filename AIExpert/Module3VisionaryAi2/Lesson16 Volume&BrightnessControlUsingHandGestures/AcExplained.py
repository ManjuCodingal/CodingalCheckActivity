import cv2, mediapipe as mp, numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

# To load all required libraries so the program can capture webcam video, detect hand landmarks, calculate fingertip distance, and control system volume and brightness.
# This activity combines computer vision with real device control, so we need multiple libraries that work together as one pipeline. OpenCV is used to open the webcam, show the live window, and draw the visual guides on the frame. MediaPipe is used as the “hand detector” that finds hands and gives landmark points for fingers. NumPy helps with math operations like measuring distance and mapping values from one range to another smoothly. Pycaw is the library that connects Python to the Windows audio system so we can change the master volume. screen_brightness_control is used to change the screen brightness from Python, which makes the app feel like a real gesture-controlled utility.

# • cv2 captures frames, draws circles/lines, and displays the live output window
# • mediapipe as mp provides the hand tracking model and landmark detection system
# • numpy as np is used for distance calculation and value interpolation
# • AudioUtilities, IAudioEndpointVolume let us access and update the system volume level
# • screen_brightness_control as sbc lets us set brightness in percentage form

# To load MediaPipe’s hand-tracking module, create a ready-to-use hand detector/tracker (hands), enable drawing utilities for visual debugging, and store the landmark IDs for thumb tip and index finger tip for gesture calculations.
Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

# mp.solutions.hands is MediaPipe’s built-in hand tracking package that detects hands and returns 21 landmark points (knuckles, joints, finger tips) for each detected hand. Hands = mp.solutions.hands is just a shortcut variable so you don’t have to repeatedly type mp.solutions.hands. hands = Hands.Hands(...) creates the actual hand-tracking object; it will run detection and tracking on every frame you pass to hands.process(...). The two parameters min_detection_confidence and min_tracking_confidence control how strict the model is: detection confidence is used when the model first finds a hand, and tracking confidence is used when it follows the hand across frames. Setting both to 0.7 makes the system reasonably strict, reducing false detections but still working well in normal lighting. draw = mp.solutions.drawing_utils gives you helper functions like draw.draw_landmarks(...) to draw the hand skeleton on the frame for debugging and user feedback. Finally, TH and IX store the landmark indices for the thumb tip and index finger tip using Hands.HandLandmark, so later you can do things like landmarks[TH] and landmarks[IX] to read those specific points consistently.

# • Hands = mp.solutions.hands creates an alias for the Hands solution module to keep code shorter and cleaner.
# • hands = Hands.Hands(...) initializes the hand detector/tracker used for hands.process(frame_rgb).
# • min_detection_confidence=0.7 sets the minimum confidence threshold to accept an initial hand detection (higher = fewer false positives, but may miss hands in poor lighting).
# • min_tracking_confidence=0.7 sets the minimum confidence threshold to keep tracking landmarks across frames (higher = more stable tracking, but may drop tracking more often if movement is fast).
# • draw = mp.solutions.drawing_utils provides drawing helpers to render landmarks and connections on the frame.
# • Hands.HandLandmark.THUMB_TIP and Hands.HandLandmark.INDEX_FINGER_TIP are fixed landmark IDs (enums) that point to the thumb and index fingertip positions among the 21 landmarks.
# • TH, IX = ... stores those IDs in short variable names so gesture logic (like pinch detection) is easier to write and read.

# Setting up system volume control using Pycaw
try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume) # Interface Audio Endpoint Vol.  QueryInterface(IAudioEndpointVolume) used to supports volume controls like SetMasterVolumeLevel and GetVolumeRange.
    minv, maxv = volctl.GetVolumeRange()[:2] # • minv, maxv = ...[:2] stores only the min and max volume bounds so you can later use np.interp(distance, [...], [minv, maxv]).
except Exception as e:
    print(f"Pycaw error: {e}"); exit()
# This block initializes Windows volume control using Pycaw, which is a Python wrapper around the Windows Core Audio APIs (COM interfaces). The first line chooses the best available way to get the default audio output device: if AudioUtilities has GetDefaultOutputDevice (some Pycaw versions do), it uses that; otherwise it falls back to AudioUtilities.GetSpeakers() (older/common method). Once a device object is obtained, dev.EndpointVolume gives access to the endpoint’s volume interface, but it must be converted into the specific COM interface type you need (IAudioEndpointVolume). That conversion is done using .QueryInterface(IAudioEndpointVolume), which returns volctl, the object that can actually read and set volume. volctl.GetVolumeRange() returns a tuple containing the minimum volume level, maximum volume level, and step size (in decibels). The slice [:2] picks only the first two values—minv and maxv—because those are what you need to map a gesture distance into the supported volume range. If anything fails (missing dependency, COM access error, incompatible Pycaw version, no audio device, permission issue), the code catches the exception, prints a clear error, and exits so the program doesn’t continue in a broken state.

# • try/except is used because audio device access can fail due to environment issues (device missing, driver issues, COM errors, Pycaw version mismatch).
# • hasattr(AudioUtilities, "GetDefaultOutputDevice") checks whether the installed Pycaw version supports that method; this makes the code more compatible across versions.
# • AudioUtilities.GetDefaultOutputDevice() returns the system default output device (best choice when available).
# • AudioUtilities.GetSpeakers() is a fallback that returns the speakers endpoint in many Pycaw setups.
# • dev.EndpointVolume references the endpoint volume COM object associated with that device.
# • QueryInterface(IAudioEndpointVolume) converts the generic COM object into the specific interface that supports volume controls like SetMasterVolumeLevel and GetVolumeRange.
# • GetVolumeRange() typically returns (min_db, max_db, increment_db); the values are usually in decibels, not 0–100.
# • minv, maxv = ...[:2] stores only the min and max volume bounds so you can later use np.interp(distance, [...], [minv, maxv]).
# • exit() stops execution because without volctl, later volume-setting calls would crash or do nothing.

# To open the default webcam so the program can continuously read live video frames, and to create a resizable OpenCV window (WIN) where the processed camera feed will be displayed.
cap = cv2.VideoCapture(0)
if not cap.isOpened(): print("Error: Webcam not accessible."); exit()
WIN = "Hand Gesture Control"; cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
# cv2.VideoCapture(0) creates a video-capture object linked to camera device index 0, which usually represents the default webcam on the system (built-in laptop camera or the first USB camera). Since camera access can fail due to permissions, driver issues, or the camera being used by another app, cap.isOpened() checks whether OpenCV successfully connected to the webcam. If it returns False, the code prints an error message and exits immediately because the rest of the application depends on receiving frames. Next, WIN = 'Hand Gesture Control' stores the window title in a variable, making it easy to reuse the same name everywhere you call cv2.imshow. cv2.namedWindow(WIN, cv2.WINDOW_NORMAL) creates the display window ahead of time and sets it to WINDOW_NORMAL, which allows manual resizing. This is helpful for gesture apps because you may want to make the preview larger during testing or when presenting.

# • cv2.VideoCapture(0) opens camera device 0 (default webcam); using 1, 2, etc. would try other cameras if available.
# • cap.isOpened() verifies the webcam is actually accessible and ready for frame capture.
# • print(...), exit() stops the program early to avoid errors later when trying to read frames from an unavailable camera.
# • WIN is a reusable window-name constant; OpenCV uses the window name string to identify which window to update.
# • cv2.namedWindow(WIN, cv2.WINDOW_NORMAL) creates a resizable window; without WINDOW_NORMAL, the window may be fixed-size (platform dependent).

# To continuously capture live frames from the webcam, mirror the view for natural interaction, extract frame dimensions for pixel calculations, and run MediaPipe Hands detection/tracking on each frame.
while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1); h, w = img.shape[:2] # • img.shape[:2] extracts (height, width); these values are required for converting landmarks from normalized coordinates to pixels.
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# This is the real-time processing loop of the gesture app. while True keeps the program running until you manually break out (like pressing a quit key) or the camera stops providing frames. cap.read() attempts to grab the latest frame from the webcam. It returns ok (a boolean success flag) and img (the actual frame as a NumPy array). If ok becomes False, it means the camera feed failed or ended, so the loop exits safely using break. Next, cv2.flip(img, 1) mirrors the frame horizontally (flip code 1), making the webcam behave like a mirror—this feels more intuitive for gesture control because your hand movement direction matches what you see on screen. h, w = img.shape[:2] reads the frame height and width so later you can convert MediaPipe’s normalized landmark coordinates (0 to 1) into real pixel coordinates (xw, yh). Finally, cv2.cvtColor(img, cv2.COLOR_BGR2RGB) converts OpenCV’s default BGR image format to RGB because MediaPipe expects RGB input. hands.process(...) runs hand detection and tracking on that RGB frame and returns a result object (res) that may include detected hand landmarks (res.multi_hand_landmarks) and other metadata.

# • while True creates a continuous loop for real-time video processing.
# • cap.read() returns ok (success) and img (frame); img is typically shape (height, width, 3) in BGR.
# • if not ok: break prevents crashes by stopping when the camera fails to deliver a frame.
# • cv2.flip(img, 1) uses flipCode=1 to mirror the image horizontally for natural gesture experience.
# • img.shape[:2] extracts (height, width); these values are required for converting landmarks from normalized coordinates to pixels.
# • cv2.COLOR_BGR2RGB converts OpenCV’s BGR frame to RGB so MediaPipe’s model processes colors correctly.
# • hands.process(...) returns res, which contains detection/tracking outputs (e.g., landmarks) used later for gesture logic.

# To confirm that MediaPipe detected hands and knows whether each hand is left or right, then loop through each detected hand, read its handedness label ("Left"/"Right"), and draw the hand skeleton on the video frame.
    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
# MediaPipe can return multiple hands in a single frame, and it provides two parallel outputs: multi_hand_landmarks (the actual 21-point landmark coordinates for each hand) and multi_handedness (the classification result that tells you whether the hand is left or right). The condition checks both are present to ensure the code doesn’t crash by trying to read handedness when it’s missing. The for i, hand in enumerate(...) loop gives you i (the hand index) and hand (the landmarks object). The same index i is used to access the matching handedness entry: res.multi_handedness[i]. Inside it, .classification[0].label returns a string like "Left" or "Right" (the top predicted class). This label is essential when you want different actions per hand, such as “right hand controls volume” and “left hand controls brightness.” Finally, draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS) overlays the detected landmarks and their connections onto the OpenCV frame so the user can see what the model is tracking in real time.

# res.multi_hand_landmarks is a list of detected hands, where each hand contains 21 landmarks (wrist, joints, fingertip points).
# res.multi_handedness is a list of classification results aligned by index with multi_hand_landmarks.
# Checking both (and) prevents index errors and makes the loop safer on frames where handedness might not be returned.
# enumerate(res.multi_hand_landmarks) provides i so you can match landmarks with their handedness entry.
# res.multi_handedness[i].classification[0].label reads the top classification label, usually "Left" or "Right".
# classification[0] is used because MediaPipe can return multiple class candidates, but [0] is the most confident one.
# draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS) draws the hand skeleton using predefined landmark connections, improving UX and helping debug tracking accuracy.

# To read MediaPipe's thumb tip and index finger tip landmarks, convert them from normalized coordinates into pixel positions, visualize them on the camera feed, and calculate the real pixel distance between the two fingertips for gesture-based control.
            lm = hand.landmark
            tp = (int(lm[TH].x*w), int(lm[TH].y*h)); ip = (int(lm[IX].x*w), int(lm[IX].y*h)) # tp (thumb position) and ip (index position)  , thumb tip landmark (lm[TH]) and index tip landmark (lm[IX])
            cv2.circle(img, tp, 10, (255,0,0), cv2.FILLED); cv2.circle(img, ip, 10, (255,0,0), cv2.FILLED)
            cv2.line(img, tp, ip, (0,255,0), 3)
            dist = float(np.hypot(ip[0]-tp[0], ip[1]-tp[1])) # hypot stands for “hypotenuse.”
# hand.landmark gives you the list of 21 hand landmarks detected by MediaPipe for that hand. Each landmark has normalized coordinates (x, y) between 0.0 and 1.0, relative to the frame size. tp (thumb position) and ip (index position) are computed by taking the thumb tip landmark (lm[TH]) and index tip landmark (lm[IX]) and converting them into pixel coordinates by multiplying x by frame width w and y by frame height h. The int(...) is used because OpenCV drawing functions expect integer pixel coordinates. The code draws a filled circle on the thumb and index positions (cv2.circle) so the user can clearly see the tracked fingertip points. It also draws a line between them (cv2.line), making the gesture distance visually understandable. Finally, np.hypot(dx, dy) calculates the Euclidean distance between the two points using √(dx² + dy²). Converting it to float ensures it’s a clean numeric value for later interpolation (mapping distance → volume/brightness). This dist is the key signal: closer fingers usually mean lower value, farther fingers mean higher value.

# lm = hand.landmark retrieves the 21 landmark objects for the detected hand.
# TH and IX are landmark IDs for thumb tip and index fingertip (from Hands.HandLandmark).
# lm[TH].x and lm[TH].y are normalized values in the range 0.0 → 1.0, not pixels.
# x * w converts normalized x into pixel x; y * h converts normalized y into pixel y.
# int(...) is required because OpenCV drawing APIs need integer pixel coordinates.
# cv2.circle(img, tp, 10, (255,0,0), cv2.FILLED) draws a filled circle at thumb tip:
# img = frame to draw on
# tp = center (x, y)
# 10 = radius (pixels)
# (255,0,0) = color in BGR (blue)
# cv2.FILLED = filled circle instead of outline
# cv2.line(img, tp, ip, (0,255,0), 3) draws a green line between thumb and index:
# (0,255,0) = green in BGR
# 3 = line thickness (pixels)
# np.hypot(ip[0]-tp[0], ip[1]-tp[1]) computes the Euclidean distance using dx and dy.
# dist is measured in pixels, so camera resolution affects typical distance values (higher resolution → larger pixel distances).

# To use the detected hand label to decide when to control system volume, then convert the thumb–index fingertip distance into a valid volume level, apply it to the computer, and show a live volume bar with percentage on the screen.
            if label == "Left":  # real RIGHT hand -> volume (frame is flipped)
                v = np.interp(dist, [30,300], [minv,maxv])
                try: volctl.SetMasterVolumeLevel(v, None)
                except Exception as e: print(f"Volume error: {e}")
                bar = int(np.interp(dist, [30,300], [400,150])); pct = int(np.interp(dist, [30,300], [0,100]))
                cv2.rectangle(img, (50,150), (85,400), (255,0,0), 2); cv2.rectangle(img, (50,bar), (85,400), (255,0,0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
# This block runs only when MediaPipe says the current detected hand is "Left". Because the camera frame is flipped like a mirror (cv2.flip(img, 1)), the hand label can appear swapped from what the user expects on screen. That is why the comment says real RIGHT hand controls volume even though the label reads "Left". Once the correct hand is identified, the code takes the distance between thumb tip and index tip and maps it to a volume range using np.interp. It then sets the system volume using Pycaw. To make the control easy to understand visually, it also draws a vertical bar and prints the volume percentage, so students can see the output even if they cannot clearly hear the change.

# if label == "Left": checks the handedness label from MediaPipe and enters the volume-control logic for this hand
# # real RIGHT hand -> volume (frame is flipped) explains that mirroring the frame can flip how the label looks relative to the user’s view
# v = np.interp(dist, [30,300], [minv,maxv]) maps finger distance from the input range 30 to 300 pixels into the device’s real volume range minv to maxv
# [30,300] is the distance calibration range where 30 = fingers close (low volume) and 300 = fingers far (high volume)
# [minv,maxv] is the system volume range returned by GetVolumeRange() (usually a decibel-based range, not 0–100)
# volctl.SetMasterVolumeLevel(v, None) applies the new volume value to the system’s master volume
# None is passed because we don’t need an extra “event context” object for this change
# try/except is used so the program doesn’t crash if volume setting fails on a device or permission issue occurs
# bar = int(np.interp(dist, [30,300], [400,150])) converts distance into a y-position for the bar fill so the bar moves up/down smoothly
# [400,150] is reversed on purpose so bigger distance makes the bar rise upward (more volume looks higher)
# pct = int(np.interp(dist, [30,300], [0,100])) converts distance into a simple percentage value to display on screen
# cv2.rectangle(img, (50,150), (85,400), (255,0,0), 2) draws the outer outline of the volume bar on the left side
# (50,150) is the top-left corner and (85,400) is the bottom-right corner of the bar outline
# (255,0,0) is the BGR color (blue) and 2 is the border thickness
# cv2.rectangle(img, (50,bar), (85,400), (255,0,0), cv2.FILLED) draws the filled part of the bar from the changing bar position down to the bottom
# cv2.FILLED means the rectangle is fully filled, not just an outline
# cv2.putText(img, f'{pct}%', (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3) shows the volume percent text below the bar
# (40,450) is the position of the text, 1 is the font size scale, and 3 is the thickness so it stays readable on video

# To control screen brightness using the other hand, by mapping the thumb–index fingertip distance into a 0–100 brightness percentage, applying it to the system, and showing a live brightness bar on the right side of the webcam window.
            elif label == "Right":  # real LEFT hand -> brightness
                b = int(np.interp(dist, [30,300], [0,100]))
                try: sbc.set_brightness(b)
                except Exception as e: print(f"Brightness error: {e}")
                bar = int(np.interp(dist, [30,300], [400,150])); x1, x2 = w-85, w-50
                cv2.rectangle(img, (x1,150), (x2,400), (0,255,0), 2); cv2.rectangle(img, (x1,bar), (x2,400), (0,255,0), cv2.FILLED)
                cv2.putText(img, f"{b}%", (w-110,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
# This block runs when MediaPipe labels the detected hand as "Right". Because the webcam frame is flipped like a mirror, the label can look swapped to the user, so the comment explains that the real LEFT hand is used for brightness control even though the label says "Right". The code takes the distance between thumb tip and index tip, converts it into a brightness percentage using interpolation, and then applies it using screen_brightness_control. Just like the volume section, it draws a vertical bar and displays the brightness percentage so the user gets clear visual feedback while testing the gesture.

# elif label == "Right": checks for the other hand label and enters brightness-control logic for this hand
# # real LEFT hand -> brightness notes that because the frame is flipped, the apparent left/right label can be reversed on screen
# b = int(np.interp(dist, [30,300], [0,100])) maps the distance range 30 to 300 pixels into brightness range 0 to 100 percent
# [30,300] is used as the “gesture distance range” where 30 = fingers close (low brightness) and 300 = fingers far (high brightness)
# [0,100] is the brightness percentage scale used by most brightness APIs
# int(...) is used because brightness is best passed as a whole number percentage
# try: sbc.set_brightness(b) applies the brightness change to the system using the brightness control library
# except ... prevents the program from crashing if the device doesn’t support software brightness control or permissions fail
# bar = int(np.interp(dist, [30,300], [400,150])) converts distance into a y-position for the bar fill so the bar rises as brightness increases
# [400,150] is reversed to make higher brightness look like a higher bar level visually
# x1, x2 = w-85, w-50 calculates the x-coordinates of the brightness bar near the right edge of the frame
# Using w (frame width) makes the bar always stay at the right side even if resolution changes
# cv2.rectangle(img, (x1,150), (x2,400), (0,255,0), 2) draws the outline of the brightness bar on the right side
# (x1,150) is top-left and (x2,400) is bottom-right of the outline rectangle
# (0,255,0) is green in BGR, which helps visually separate brightness from the blue volume bar
# 2 is the thickness of the outline border
# cv2.rectangle(img, (x1,bar), (x2,400), (0,255,0), cv2.FILLED) draws the filled portion of the bar from bar down to the bottom
# cv2.FILLED makes the rectangle fully filled so the level is clearly visible
# cv2.putText(img, f'{b}%', (w-110,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3) displays the brightness percentage text below the bar
# (w-110,450) positions the text near the right side, 1 sets the font size, and 3 sets thickness for readability

# To display the live webcam output, check for exit actions (keyboard or window close), safely stop the loop when needed, and properly release the webcam and close all OpenCV windows so the system resources are not locked.
    cv2.imshow(WIN, img)
    k = cv2.waitKey(1) & 0xFF
    if k in (27, ord("q")): break
    try:
        if cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1: break
    except cv2.error:
        break

cap.release(); cv2.destroyAllWindows()
# This section is the “end of loop control + clean exit” part of the program. Every frame that gets processed (with landmarks, bars, and text) must be shown on the screen using cv2.imshow. At the same time, the program must keep listening for user input so it can quit smoothly. cv2.waitKey(1) checks the keyboard very quickly (1 millisecond delay) so the video stays smooth and responsive. The & 0xFF part is used to correctly interpret the key code across different systems. The code supports two exit methods: pressing ESC or pressing q. It also supports a third exit method: if the user clicks the close button on the OpenCV window, the loop should stop instead of crashing. Finally, when the loop ends, the webcam is released and all windows are destroyed so the webcam can be used again by other apps.

# cv2.imshow(WIN, img) shows the current processed frame in the window named WIN so the user sees live output
# WIN is the window title string you created earlier, and img is the latest frame with drawings and UI
# k = cv2.waitKey(1) & 0xFF waits for 1 millisecond, captures a key press if any, and normalizes the key code to the last 8 bits
# cv2.waitKey(1) keeps the loop fast so the webcam feed looks smooth and does not freeze
# & 0xFF helps ensure the key value is read correctly on different platforms and Python/OpenCV builds
# if k in (27, ord('q')): break exits the loop if the user presses ESC or q
# 27 is the ASCII code for the ESC key
# ord('q') converts the character q into its ASCII key code so it can be compared with k
# try: starts a safe block because window property checks can throw errors depending on the OS and OpenCV version
# cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) checks whether the window is still visible on the screen
# cv2.WND_PROP_VISIBLE is the specific flag that tells OpenCV to return the visibility status of that window
# if ... < 1: break means if the window is closed or not visible, the loop stops cleanly instead of continuing in the background
# except cv2.error: break handles the case where OpenCV throws an error (for example, if the window was already destroyed), and then exits safely
# cap.release() releases the webcam device so it is not locked after the program ends
# cv2.destroyAllWindows() closes all OpenCV windows that were created, preventing leftover windows or stuck processes