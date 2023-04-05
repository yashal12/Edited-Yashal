import time
from waitingTime import Wait
from fare import RideFare
from TotalDistance import TaxiDistance
from drivingState import TaxiStatus
from rideTime import RideTime


class EndRide:
    def end_ride(self):
        end_time = time.time()
        start_time = TaxiStatus().start_ride()
        distance = TaxiStatus().start_distance()

        wait = Wait().calculate_waiting_time()
        RideTime().rideTime(end_time, start_time, wait)
        RideFare(distance).calculate_ride_fare()
        TaxiDistance().find_distance()

        return end_time
