import time

DISTANCE = 100


class TaxiStatus:
    def __init__(self):
        self.start_time = None
        self.wait_start_time = 0
        self.status = "wait"

    def start_ride(self):
        self.status = "driving"
        self.start_time = time.time()

        return self.start_time

    def pause_ride(self):
        if self.status == "driving":
            self.status = "wait"
            self.wait_start_time = time.time()

        return self.wait_start_time

    def resume_ride(self):
        if self.status == "wait":
            self.status = "driving"
