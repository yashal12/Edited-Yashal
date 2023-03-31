import csv


class WeatherDataParser:

    def __init__(self, file_to_read):
        self.file_to_read = file_to_read

    def parse_weather_data(self):
        list_of_data = []
        with open(self.file_to_read, 'r') as file_name:
            files_dictionary = csv.DictReader(file_name)

            for rows in files_dictionary:
                if rows['Max TemperatureC'] == ' ' or rows['Min TemperatureC'] == ' ' or rows['Max Humidity'] == ' ':
                    rows['Max TemperatureC'] = rows['Min TemperatureC'] = rows['Max Humidity'] = 0
                list_of_data.append(rows)

        return list_of_data

