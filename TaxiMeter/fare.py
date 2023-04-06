from totalDistance import DistanceTracker
from waitingTime import Wait

FARE_PER_KM = 3


class RideFare:

    def calculate_ride_fare(self):
        distance_km, distance_m = DistanceTracker().find_distance()
        fare = distance_km * FARE_PER_KM + Wait().calculate_waiting_charge()

        return fare

    def print_fare(self):
        print(f"Fare: {self.calculate_ride_fare()} Rs")
