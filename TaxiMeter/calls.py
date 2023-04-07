from calculations import Calculations
from drivingState import TaxiRide


class Taxi:
    def calculate_taxi_meter(self):
        start_time = TaxiRide().start()
        wait = Calculations().calculate_waiting_time()
        fare = Calculations().calculate_ride_fare()
        ride = Calculations().get_ride_duration(TaxiRide().end(), start_time, wait)
        distance_km, distance_m = Calculations().find_distance()

        return wait, ride, fare, distance_km, distance_m
