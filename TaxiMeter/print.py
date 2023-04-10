from calculations import Calculations
from calls import Taxi


class RideSummaryPrinter:
    def print_ride_summary(self):
        wait, ride, fare, distance_km, distance_m = Taxi().calculate_taxi_meter()

        print(f"\nRide Time: {ride} Seconds")
        print(f"Waiting Time: {wait} Minutes")
        print(f"Fare: {fare} Rs")
        print("Current speed:", Calculations().increase_speed(), "m/s")
        print("Current speed:", Calculations().decrease_speed(), "m/s")
        print(f"Distance: {int(distance_km)} KM {int(distance_m)} Meters")
