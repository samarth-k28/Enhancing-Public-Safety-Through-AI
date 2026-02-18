import cv2
import numpy as np

video_path = "test_video.mp4"

cap = cv2.VideoCapture(video_path)

ret, prev_frame = cap.read()
if not ret:
    print("Error reading video")
    exit()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

motion_history = []
alert_counter = 0
alert_display_timer = 0
BASE_THRESHOLD = 1000
EXTREME_THRESHOLD = 9000
CONFIRMATION_FRAMES = 4
ALERT_DISPLAY_FRAMES = 180
while True:
    ret, frame = cap.read()
    if not ret:
        print("Video Ended")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(prev_gray, gray)
    blur = cv2.GaussianBlur(diff, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

    motion_score = cv2.countNonZero(thresh)

    motion_history.append(motion_score)
    if len(motion_history) > 20:
        motion_history.pop(0)

    risk = 0

    if motion_score > BASE_THRESHOLD:
        risk = 5

    if motion_score > EXTREME_THRESHOLD:
        risk = 10

    # Confirmation logic
    if risk >= 5:
        alert_counter += 1
    else:
        alert_counter = 0

    if alert_counter >= CONFIRMATION_FRAMES:
        alert_display_timer = ALERT_DISPLAY_FRAMES

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 800:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show alert with delay vanish
    if alert_display_timer > 0:
        cv2.putText(frame, "ALERT!", (50, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        alert_display_timer -= 1

    cv2.imshow("AI Public Safety System", frame)

    prev_gray = gray

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
