class RiskEngine:
    def __init__(self):
        self.motion_threshold = 60000
        self.extreme_threshold = 200000

    def calculate_risk(self, motion_score, audio_level=0):
        risk = 0

        if motion_score > self.motion_threshold:
            risk += 5

        if motion_score > self.extreme_threshold:
            risk += 5

        return risk
