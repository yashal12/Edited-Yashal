import argparse
import calendar
import glob

from barcharts import WeatherCharts
from calculations import WeatherStatistics
from parser import WeatherDataParser
from report import WeatherReportGenerator


class WeatherDataAnalyzer:

    def get_month_abbreviation(self, month_number):
        if month_number < 1 or month_number > 12:
            raise ValueError("Invalid month number")

        return calendar.month_abbr[month_number]

    def get_files_by_year(self, year, folder_path):
        file_pattern = f"Murree_weather_{year}_*.txt"
        file_paths = glob.glob(f"{folder_path}/{file_pattern}")

        return file_paths

    def process_command_line_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('file')
        parser.add_argument('-a')
        parser.add_argument('-e')
        parser.add_argument('-c')
        args = parser.parse_args()

        if args.a:
            year, month = args.a.split('/')
            month = self.get_month_abbreviation(int(month))
            folder_path = args.file
            file_pattern = f"Murree_weather_{year}_{month}.txt"
            file_list = glob.glob(f"{folder_path}/{file_pattern}")
            weather_report = WeatherReportGenerator()

            for file_data in file_list:
                parse = WeatherDataParser(file_data)
                parsed_file = parse.parse_weather_data()
                month = WeatherStatistics(parsed_file)

                max_temperature = month.compute_sum('Max TemperatureC')
                min_temperature = month.compute_sum('Min TemperatureC')
                humidity = month.compute_sum('Max Humidity')
                average_highest = month.compute_average(max_temperature)
                average_lowest = month.compute_average(min_temperature)
                average_humidity = month.compute_average(humidity)

                weather_report.print_monthly_report(average_highest, average_lowest, average_humidity)
                weather_report.generate_report(average_highest, average_lowest, average_humidity)

        if args.e:
            year = args.e
            folder_path = args.file
            file = self.get_files_by_year(year, folder_path)
            year = WeatherStatistics(file)
            weather_report = WeatherReportGenerator()
            max_temperature, min_temperature, humidity, date_max_temperature, date_min_temperature, date_humidity = year.annual_statistics()

            weather_report.print_annual_report(max_temperature, min_temperature, humidity, date_max_temperature,
                                               date_min_temperature,
                                               date_humidity)
            weather_report.generate_report(max_temperature, min_temperature, humidity)

        if args.c:
            year, month = args.c.split('/')
            month = self.get_month_abbreviation(int(month))
            folder_path = args.file
            file_pattern = f"Murree_weather_{year}_{month}.txt"
            file_list = glob.glob(f"{folder_path}/{file_pattern}")

            for file_data in file_list:
                parse = WeatherDataParser(file_data)
                parsed_file = parse.parse_weather_data()
                chart = WeatherCharts(parsed_file)
                print("\n\t\t\t\t Highest Temperature")
                chart.max_temperature_chart()
                print("\n\t\t\t\t Lowest Temperature")
                chart.min_temperature_chart()
                print("\n\t\t\t\t Combine Chart")
                chart.combine_chart()


weather_analyzer = WeatherDataAnalyzer()
weather_analyzer.process_command_line_arguments()
