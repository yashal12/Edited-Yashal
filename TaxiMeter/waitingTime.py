import time

from drivingState import TaxiStatus


class Wait:
    def __init__(self):
        self.rate_per_minute = 2
        self.wait_start_time = TaxiStatus().pause_ride()
        self.wait_end_time = 0
        self.wait_time = 0

    def calculate_waiting_time(self):
        self.wait_end_time = time.time()
        self.wait_time += self.wait_end_time - self.wait_start_time

        return self.wait_time/60

    def calculate_waiting_charge(self):
        return self.calculate_waiting_time() * self.rate_per_minute
