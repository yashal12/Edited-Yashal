import glob

from parser import Parser


class Statistics:

    def __init__(self, list_of_file):
        self.list_of_file = list_of_file

    def annual_operations(self):
        max_temperature = humidity = 0
        min_temperature = 500
        file_read = self.list_of_file
        length = len(file_read)

        for traverse in range(length):
            traverse_files = file_read[traverse]
            read_files = Parser(traverse_files).parser()

            for read_data in read_files:
                if float(read_data['Max TemperatureC']) > max_temperature:
                    max_temperature = float(read_data['Max TemperatureC'])
                    date_max_temperature = read_data['PKT']

                if float(read_data['Min TemperatureC']) < min_temperature:
                    min_temperature = float(read_data['Min TemperatureC'])
                    date_min_temperature = read_data['PKT']

                if float(read_data['Max Humidity']) > humidity:
                    humidity = float(read_data['Max Humidity'])
                    date_humidity = read_data['PKT']

        return max_temperature, min_temperature, humidity, date_max_temperature, date_min_temperature, date_humidity

    def print_annual(self, max_temperature, min_temperature, humidity, date_max_temperature, date_min_temperature, date_humidity):
        print(f"\nHighest: {max_temperature} on {date_max_temperature} \nLowest: {min_temperature} on {date_min_temperature}"
              f"\nHumidity: {humidity} on {date_humidity}")

    # Monthly Statistics

    def return_sum(self, col):
        temperature = sum(float(read_data[col]) for read_data in self.list_of_file)

        return temperature

    def sum_call(self):
        length_of_file = len(self.list_of_file)
        max_temperature = self.return_sum('Max TemperatureC')
        min_temperature = self.return_sum('Min TemperatureC')
        humidity = self.return_sum('Max Humidity')

        return max_temperature, min_temperature, humidity, length_of_file

    def highest_average(self, max_temperature, length_of_file):
        average_highest = max_temperature / length_of_file


        return average_highest

    def lowest_average(self, min_temperature, length_of_file):
        average_lowest = min_temperature / length_of_file

        return average_lowest

    def average_humidity(self, humidity, length_of_file):
        average_humidity = humidity / length_of_file

        return average_humidity

    def print(self, average_highest, average_lowest, average_humidity):
        print("\nHighest Average: ", average_highest)
        print("\nLowest Average:", average_lowest)
        print("\nLowest Average:", average_humidity)
