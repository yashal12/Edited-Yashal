import time

from constant import FARE_PER_KM, RATE_PER_MINUTE
from drivingState import TaxiRide


class Calculations:
    def __init__(self):
        self.speed = 20
        self.status = "wait"
        self.last_update_time = 0
        self.current_distance = 10
        self.wait_start_time = TaxiRide().pause()
        self.start_time = time.time()
        self.wait_end_time = 0
        self.wait_time = 0

    def calculate_waiting_time(self):
        self.wait_end_time = time.time()
        self.wait_time += self.wait_end_time - self.wait_start_time

        return self.wait_time / 60

    def calculate_waiting_charge(self):
        return self.calculate_waiting_time() * RATE_PER_MINUTE

    def get_ride_duration(self, end_time, start_time, wait):
        return end_time - start_time - wait

    def increase_speed(self):
        if self.status == "driving":
            self.speed += 3

        return self.speed

    def decrease_speed(self):
        if self.status == "driving" and self.speed > 0:
            self.speed -= 1

        return self.speed

    def find_distance(self):
        distance_km = self.current_distance / 1000
        distance_m = self.current_distance % 1000

        return distance_km, distance_m

    def update_distance(self):
        if self.status == "driving":
            current_time = time.time()
            time_elapsed = current_time - self.last_update_time
            distance_traveled = self.speed * time_elapsed
            self.current_distance += distance_traveled
            self.last_update_time = current_time

    def calculate_ride_fare(self):
        distance_km, distance_m = self.find_distance()
        distance_charge = distance_km * FARE_PER_KM
        fare = distance_charge + self.calculate_waiting_charge()

        return fare
