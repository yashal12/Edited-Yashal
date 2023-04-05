import time

distance = 100


class TaxiStatus:
    def __init__(self):
        self.start_time = None
        self.distance = 0

    def start_ride(self):
        self.start_time = time.time()
        return self.start_time

    def start_distance(self):
        self.distance = distance
        return self.distance

    def pause_ride(self):
        return time.time()

    def resume_ride(self):
        self.start_time += time.time() - self.pause_ride()
        return self.start_time

