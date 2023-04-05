import time
from drivingState import TaxiStatus


class Wait:
    def __init__(self):
        self.waiting_time = 0
        self.waiting_rate_per_minute = 2
        self.start_time = TaxiStatus().start_ride()
        self.pause_time = TaxiStatus().pause_ride

    def calculate_waiting_time(self):
        if self.start_time is None:
            print("Error: trip has not started yet!")
            return

        if self.pause_time is None:
            print("Error: trip has not been paused yet!")
            return

        self.waiting_time += self.pause_time - self.start_time

        return self.waiting_time

    def calculate_waiting_charge(self):
        return self.calculate_waiting_time() * self.waiting_rate_per_minute

