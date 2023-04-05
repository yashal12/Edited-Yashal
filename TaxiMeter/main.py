import keyboard

from drivingState import TaxiStatus
from endRide import EndRide


class Input:
    def __init__(self):
        self.current_speed = 0

    def arrow_keys(self, event):
        while True:
            question = str(input("Start Ride?"))
            if question == 'no':
                break
            elif question == 'yes':
                print("Trip started!")
                TaxiStatus().start_ride()

            # global speed_calculator
            if event.name == 'up':
                self.current_speed += 1
                print("Current speed:", self.current_speed, "m/s")
            elif event.name == 'down':
                self.current_speed = max(0, self.current_speed - 1)
                print("Current speed:", self.current_speed, "m/s")
            elif event.name in ('P', 'p'):
                print("Trip paused!")
                TaxiStatus().pause_ride()
            elif event.name in ('R', 'r'):
                print("Trip resumed!")
                TaxiStatus().resume_ride()
            elif event.name in ('E', 'e'):
                print("Trip ended!")
                EndRide().end_ride()

            else:
                print("Invalid keyboard input!")
