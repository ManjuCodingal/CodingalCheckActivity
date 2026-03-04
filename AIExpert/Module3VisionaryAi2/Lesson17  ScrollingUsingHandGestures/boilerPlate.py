#############################################
# GESTURE-BASED SCROLL CONTROL - PSEUDO CODE
#############################################

# ---------------------------------------------------
# STEP 1: Import required libraries
#   - Library for capturing video from webcam
#   - Library for time management (FPS, delays)
#   - Library for controlling scroll on the system
#   - Library for hand tracking and gesture detection
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 2: Initialize hand tracking model
#   - Set maximum number of hands to detect (e.g., 1)
#   - Set minimum detection confidence (e.g., 0.7)
#   - Prepare utility for drawing hand landmarks
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 3: Define configuration values
#   - SCROLL_SPEED = how much to scroll per gesture
#   - SCROLL_DELAY = how many seconds to wait between scroll actions
#   - CAM_WIDTH, CAM_HEIGHT = resolution of the camera feed
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 4: Create gesture detection function
#   - Input: landmarks of detected hand + handedness (Left/Right hand)
#   - Process:
#       1. Check which fingers are extended
#          - Compare fingertip landmark with its lower joint
#          - If fingertip is above joint => finger extended
#       2. Check thumb position (different for Left vs Right hand)
#       3. Count how many fingers are extended
#   - Output:
#       - If all 5 fingers extended => return "scroll_up"
#       - If 0 fingers extended => return "scroll_down"
#       - Otherwise => return "none"
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 5: Setup webcam capture
#   - Open webcam stream
#   - Set frame width and height
#   - Initialize variables for scroll timing and FPS tracking
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 6: Main loop
#   - While webcam is open:
#       1. Capture a frame from the webcam
#       2. Convert frame to correct format (RGB)
#       3. Flip image horizontally for mirror effect
#       4. Run hand detection on the frame
#       5. If a hand is detected:
#           a. Get hand landmarks and handedness (Left/Right)
#           b. Call gesture detection function
#           c. Draw detected landmarks on the frame
#           d. If enough time has passed since last scroll:
#               i. If gesture = scroll_up => perform system scroll up
#               ii. If gesture = scroll_down => perform system scroll down
#               iii. Update last scroll time
#       6. Calculate FPS (frames per second)
#       7. Overlay FPS, handedness, and gesture info on the frame
#       8. Show frame in a window
#       9. If user presses quit key (e.g., 'q'), break loop
# ---------------------------------------------------

# ---------------------------------------------------
# STEP 7: Cleanup
#   - Release webcam resource
#   - Close any display windows
# ---------------------------------------------------
