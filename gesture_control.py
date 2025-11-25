import cv2
import mediapipe as mp
import pyautogui
import os
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils


def finger_up(landmarks, finger_tip, finger_dip):
    return landmarks[finger_tip].y < landmarks[finger_dip].y

def detect_gesture(landmarks):
   
    thumb = finger_up(landmarks, 4, 3)
    index = finger_up(landmarks, 8, 7)
    middle = finger_up(landmarks, 12, 11)

    # Gestures
    if thumb and not index and not middle:
        return "THUMBS_UP"

    if not thumb and not index and not middle:
        return "FIST"

    if not thumb and index and middle:
        return "SCROLL_UP"

    if not thumb and index and not middle:
        return "CLICK"

    if not thumb and not index and middle:
        return "SCROLL_DOWN"

    if thumb and index and middle:
        return "PAUSE_PLAY"

    return None


def execute_action(gesture):
    print("Detected:", gesture)

    if gesture == "THUMBS_UP":
        os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

    if gesture == "FIST":
        os.system("osascript -e 'tell application \"Music\" to next track'")

    if gesture == "PAUSE_PLAY":
        os.system("osascript -e 'tell application \"Music\" to playpause'")

    if gesture == "SCROLL_UP":
        pyautogui.scroll(400)

    if gesture == "SCROLL_DOWN":
        pyautogui.scroll(-400)

    if gesture == "CLICK":
        pyautogui.click()


cap = cv2.VideoCapture(0)
last_action_time = time.time()

print(" Gesture Control Started! Use your hand in front of the webcam.")

while True:
    success, frame = cap.read()
    if not success:
        continue

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            landmarks = handLms.landmark
            gesture = detect_gesture(landmarks)

            if gesture and (time.time() - last_action_time > 0.8):
                execute_action(gesture)
                last_action_time = time.time()

    cv2.imshow("Mac Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
