import time


class DistanceTracker:
    def __init__(self):
        self.speed = 1
        self.status = "wait"
        self.start_time = time.time()
        self.last_update_time = 0
        self.current_distance = 10

    def increase_speed(self):
        if self.status == "driving":
            self.speed += 3

        return self.speed

    def decrease_speed(self):
        if self.status == "driving" and self.speed > 0:
            self.speed -= 1

        return self.speed

    def find_distance(self):
        distance_km = self.current_distance / 1000
        distance_m = self.current_distance % 1000

        return distance_km, distance_m

    def calculate_time(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time

        return current_time, time_elapsed

    def update_distance(self):
        if self.status == "driving":
            current_time, time_elapsed = self.calculate_time()
            distance_traveled = self.speed * time_elapsed
            self.current_distance += distance_traveled
            self.last_update_time = current_time

    def print(self):
        distance_km, distance_m = self.find_distance()

        print("\nCurrent speed:", self.increase_speed(), "m/s")
        print("Current speed:", self.decrease_speed(), "m/s")
        print(f"Distance: {int(distance_km)} KM {int(distance_m)} Meters")


