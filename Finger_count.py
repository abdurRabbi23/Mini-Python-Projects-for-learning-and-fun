import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

# Initialize the video capture
cap = cv2.VideoCapture(0)  # to capture video from the default camera (index 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

# Initialize Mediapipe drawing and hand solutions
mp_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

# Initialize the HandDetector from cvzone
detector = HandDetector(detectionCon=0.7, maxHands=2)  # adjust detection confidence and max hands as needed

# Loop to continuously capture frames
while True:
    success, frame = cap.read()  # Returns a boolean success flag and the frame
    if success:
        # Convert the frame to RGB for mediapipe processing
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)

        # Detect hands using cvzone's HandDetector
        hands, img = detector.findHands(frame, flipType=False)

        # If hands are detected, count the fingers
        if hands:
            lmList = hands[0]["lmList"]  # Landmark list of the first detected hand
            fingerUp = detector.fingersUp(hands[0])  # Determine which fingers are up
            print("Fingers Up:", fingerUp)

            if fingerUp == [1, 0, 0, 0, 0]:
                cv2.putText(frame, 'Finger count: 0', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [1, 1, 0, 0, 0]:
                cv2.putText(frame, 'Finger count: 1', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [1, 1, 1, 0, 0]:
                cv2.putText(frame, 'Finger count: 2', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [1, 1, 1, 1, 0]:
                cv2.putText(frame, 'Finger count: 3', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [1, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger count: 4', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [0, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger count: 5', (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (204, 0, 0), 3, cv2.LINE_AA)
            elif fingerUp == [0, 0, 1, 0, 0] or [1, 0, 1, 0, 0]:
                cv2.putText(frame, "F**k BALLON D'OR", (20, 460),
                            cv2.FONT_HERSHEY_COMPLEX, 2,
                            (255, 0, 0), 3, cv2.LINE_AA)
                6
        # Draw Mediapipe landmarks on
        cv2.imshow("Hand Detections and Gestures", frame)
        if cv2.waitKey(1) == ord('q'):  # delay 1 sec and enter the next line
            break

# Release resources
cap.release()
cv2.destroyAllWindows()