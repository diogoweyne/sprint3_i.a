import time

class Performance:
    def __init__(self):
        self.last_time = time.time()

    def fps(self):
        now = time.time()
        fps = 1 / (now - self.last_time)
        self.last_time = now
        return round(fps, 2)
