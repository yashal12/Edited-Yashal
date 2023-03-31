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

                average_highest = month.compute_average('Max TemperatureC')
                average_lowest = month.compute_average('Min TemperatureC')
                average_humidity = month.compute_average('Max Humidity')

                weather_report.print_monthly_report(average_highest, average_lowest, average_humidity)

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

        if args.c:
            year, month = args.c.split('/')
            month = self.get_month_abbreviation(int(month))
            folder_path = args.file
            file_pattern = f"Murree_weather_{year}_{month}.txt"
            file_list = glob.glob(f"{folder_path}/{file_pattern}")
            print(file_list)

            for file_data in file_list:
                parse = WeatherDataParser(file_data)
                parsed_file = parse.parse_weather_data()
                chart = WeatherCharts(parsed_file)
                chart.max_temperature_chart()
                chart.min_temperature_chart()
                chart.combine_chart()


weather_analyzer = WeatherDataAnalyzer()
weather_analyzer.process_command_line_arguments()
