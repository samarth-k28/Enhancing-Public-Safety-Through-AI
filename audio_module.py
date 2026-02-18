import sounddevice as sd
import numpy as np

class AudioAnalyzer:
    def __init__(self):
        self.volume = 0

    def callback(self, indata, frames, time, status):
        self.volume = np.linalg.norm(indata)

    def start_stream(self):
        self.stream = sd.InputStream(callback=self.callback)
        self.stream.start()

    def get_audio_level(self):
        return self.volume
