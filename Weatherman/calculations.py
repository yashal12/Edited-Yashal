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

        max_temperature, date_max_temperature = max(
            ((float(read_data['Max TemperatureC']), read_data['PKT']) for current_file in self.list_of_file
             for read_data in WeatherDataParser(current_file).parse_weather_data()))

        min_temperature, date_min_temperature = min(
            ((float(read_data['Min TemperatureC']), read_data['PKT']) for current_file in self.list_of_file
             for read_data in WeatherDataParser(current_file).parse_weather_data()))

        humidity, date_humidity = max(
            ((float(read_data['Max Humidity']), read_data['PKT']) for current_file in self.list_of_file
             for read_data in WeatherDataParser(current_file).parse_weather_data()))

        return round(max_temperature), round(min_temperature), round(humidity), date_max_temperature, date_min_temperature, date_humidity

    # Monthly Statistics

    def compute_sum(self, col):
        return sum(float(read_data[col]) for read_data in self.list_of_file)

    def compute_average(self, col):
        file_count = len(self.list_of_file)
        temperature = self.compute_sum(col)
        average = temperature / file_count

        return round(average)
