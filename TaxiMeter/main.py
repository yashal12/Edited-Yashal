import keyboard

from calculations import Calculations
from calls import Taxi
from drivingState import TaxiRide
from print import RideSummaryPrinter


class TaxiController:
    def manage_trip(self):
        question = input("Start Ride? ")
        if question == 'yes':
            print("Trip started!")
            TaxiRide().start()
        if question == 'no':
            print("No More Trips!")
            return

    def display_controls(self):
        print("You can use UP Arrow to Increase Speed, Down Arrow to Decrease Speed, E / e to End Ride, P / p to "
              "Pause Ride, R / r to Resume Ride")

    def get_user_choice(self):
        while True:
            TaxiRide().start()
            choice = input("Enter Your choice: ")
            if choice in ('E', 'e'):
                print("Trip ended!")
                TaxiRide().end()
                Taxi().calculate_taxi_meter()
                RideSummaryPrinter().print_ride_summary()
                break
            elif choice in ('P', 'p'):
                print("Trip paused!")
                TaxiRide().pause()
            elif choice in ('R', 'r'):
                print("Trip resumed!")
                TaxiRide().resume()
                Calculations().calculate_waiting_time()
            elif choice not in ('E', 'e', 'P', 'p', 'R', 'r'):
                print("Invalid input!")
                return
            Calculations().update_distance()


def handle_arrow_keys(self, event):
    while True:
        if event.name == 'up':
            Calculations().increase_speed()
        elif event.name == 'down':
            Calculations().decrease_speed()


TaxiController().manage_trip()
TaxiController().get_user_choice()
keyboard.on_press(handle_arrow_keys)
keyboard.wait()
