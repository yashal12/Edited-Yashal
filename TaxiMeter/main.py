import keyboard

from drivingState import TaxiStatus
from endRide import EndRide
from totalDistance import DistanceTracker
from waitingTime import Wait


def arrow_keys(self, event):
    while True:
        if event.name == 'up':
            DistanceTracker().increase_speed()
        elif event.name == 'down':
            DistanceTracker().decrease_speed()


class Main:
    def key_actions(self):
        question = input("Start Ride? ")
        if question == 'yes':
            print("Trip started!")
            TaxiStatus().start_ride()
        if question == 'no':
            print("No More Trips!")
            return

    def choices(self):
        print("You can use UP Arrow to Increase Speed, Down Arrow to Decrease Speed, E / e to End Ride, P / p to "
              "Pause Ride, R / r to Resume Ride")

        while True:
            TaxiStatus().start_ride()
            choice = input("Enter Your choice: ")
            if choice in ('E', 'e'):
                print("Trip ended!")
                EndRide().end_ride()
                EndRide().taxi_meter()
                EndRide().print()
                break
            elif choice in ('P', 'p'):
                print("Trip paused!")
                TaxiStatus().pause_ride()
            elif choice in ('R', 'r'):
                print("Trip resumed!")
                TaxiStatus().resume_ride()
                Wait().calculate_waiting_time()
            elif choice not in ('E', 'e', 'P', 'p', 'R', 'r'):
                print("Invalid input!")
                return

            DistanceTracker().update_distance()


Main().key_actions()
Main().choices()
keyboard.on_press(arrow_keys)
keyboard.wait()
