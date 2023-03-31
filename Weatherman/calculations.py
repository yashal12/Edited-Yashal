import glob

from parser import WeatherDataParser


class WeatherStatistics:

    def __init__(self, list_of_file):
        self.list_of_file = list_of_file

    def annual_statistics(self):
        max_temperature = humidity = 0
        min_temperature = 500
        file_read = self.list_of_file
        file_count = len(file_read)

        for file_num in range(file_count):
            current_file = file_read[file_num]
            file_data = WeatherDataParser(current_file).parse_weather_data()

            for read_data in file_data:
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

    # Monthly Statistics

    def compute_sum(self, col):
        temperature_sum = sum(float(read_data[col]) for read_data in self.list_of_file)
        return temperature_sum

    def compute_average(self, temperature):
        file_count = len(self.list_of_file)
        average = temperature / file_count
        return round(average)
