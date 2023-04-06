import time

from drivingState import TaxiStatus
from fare import RideFare
from rideTime import RideTime
from totalDistance import DistanceTracker
from waitingTime import Wait


class EndRide:
    def __init__(self):
        self.status = "wait"

    def end_ride(self):
        self.status = "end"
        end_time = time.time()

        return end_time

    def taxi_meter(self):
        start_time = TaxiStatus().start_ride()
        wait = Wait().calculate_waiting_time()
        RideFare().calculate_ride_fare()
        DistanceTracker().find_distance()
        ride = RideTime().ride_time(self.end_ride(), start_time, wait)

        return wait, ride

    def print(self):
        wait, ride = self.taxi_meter()
        DistanceTracker().print()
        RideFare().print_fare()

        print(f"Ride Time: {ride} Seconds")
        print(f"Waiting Time: {wait} Minutes")