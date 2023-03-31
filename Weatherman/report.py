from calculations import WeatherStatistics


class WeatherReportGenerator:
    def __init__(self):
        self.result = None

    def generate_report(self, max_temperature, min_temperature, humidity):
        result = [max_temperature, min_temperature, humidity]

    def print_annual_report(self, max_temperature, min_temperature, humidity, date_max_temperature, date_min_temperature,
                     date_humidity):
        print(
            f"\nHighest: {max_temperature}C on {date_max_temperature} \nLowest: {min_temperature}C on {date_min_temperature}"
            f"\nHumidity: {humidity} on {date_humidity}")

    def print_monthly_report(self, average_highest, average_lowest, average_humidity):
        print(
            f"\nHighest Average: {average_highest}C \nLowest Average: {average_lowest}C \nLowest Average: {average_humidity}")
