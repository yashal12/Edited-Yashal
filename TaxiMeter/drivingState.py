import time


class TaxiRide:
    def __init__(self):
        self.start_time = None
        self.wait_start_time = 0
        self.status = "wait"

    def start(self):
        self.status = "driving"
        self.start_time = time.time()

        return self.start_time

    def pause(self):
        if self.status == "driving":
            self.status = "wait"
            self.wait_start_time = time.time()

        return self.wait_start_time

    def resume(self):
        if self.status == "wait":
            self.status = "driving"

    def end(self):
        self.status = "end"
        end_time = time.time()

        return end_time
