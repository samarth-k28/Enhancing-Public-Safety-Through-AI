import cv2

class VideoAnalyzer:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.ret, self.prev_frame = self.cap.read()

        if self.ret:
            self.prev_gray = cv2.cvtColor(self.prev_frame, cv2.COLOR_BGR2GRAY)
        else:
            self.prev_gray = None

    def process_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            return None, None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(self.prev_gray, gray)

        blur = cv2.GaussianBlur(diff, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_score = 0

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            motion_score += cv2.contourArea(contour)

        self.prev_gray = gray

        return frame, thresh, motion_score

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
