import time

from drivingState import TaxiStatus
from waitingTime import Wait


class RideFare:
    def __init__(self, start_distance):
        self.distance = start_distance
        self.distance_rate = 3
        self.start_time = TaxiStatus().start_ride()

    def calculate_ride_fare(self):
        distance_charge = self.distance * self.distance_rate
        fare = distance_charge + Wait().calculate_waiting_charge()

        return fare
