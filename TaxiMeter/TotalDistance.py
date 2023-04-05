import time

from main import Input


class TaxiDistance:
    def __init__(self):
        self.start_time = time.time()
        self.current_time = self.start_time
        self.current_distance = 0
        self.current_speed = Input().current_speed

    def find_distance(self):
        time_elapsed = time.time() - self.current_time
        distance_travelled = self.current_speed * time_elapsed
        self.current_distance += distance_travelled
        self.current_time += time_elapsed
        print("Distance:", round((self.current_distance - self.start_distance) / 1000, 2), "KM")

