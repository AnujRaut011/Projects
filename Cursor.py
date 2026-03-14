import cv2
import numpy as np
import pyautogui

# Constants for hand detection
hand_lower = np.array([0, 48, 80], dtype=np.uint8)
hand_upper = np.array([20, 255, 255], dtype=np.uint8)

# Function to detect hand and get its centroid
def detect_hand(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hand_lower, hand_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return cx, cy
    return None

# Main function
def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for intuitive movement
        frame = cv2.flip(frame, 1)
        
        # Detect hand
        hand_pos = detect_hand(frame)
        
        # Move cursor if hand detected
        if hand_pos:
            x, y = hand_pos
            # Scale hand position to screen resolution
            screen_x = int(x * pyautogui.size()[0] / frame.shape[1])
            screen_y = int(y * pyautogui.size()[1] / frame.shape[0])
            # Move cursor
            pyautogui.moveTo(screen_x, screen_y, duration=0)
        
        cv2.imshow("Hand Tracking", frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
