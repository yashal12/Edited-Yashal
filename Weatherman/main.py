import argparse
import calendar
import glob

from barcharts import Charts
from calculations import Statistics
from parser import Parser
from report import Report


class Main:

    def month_year_from_arguments(self, given_month):
        month_abbreviations = calendar.month_abbr

        for index, month_name in enumerate(month_abbreviations):
            if index == given_month:
                return month_name

    def files_list(self, year, folder_path):
        file_path = 'Murree_weather_' + str(year) + '_*txt'  # search for files in directory
        files = glob.glob(f"{folder_path}/{file_path}")

        return files

    def command_line_arguments(self):
        if __name__ == '__main__':
            parser = argparse.ArgumentParser()
            parser.add_argument('file')
            parser.add_argument('-a')
            parser.add_argument('-e')
            parser.add_argument('-c')
            args = parser.parse_args()

            if args.a:
                year, month = args.a.split('/')
                month = self.month_year_from_arguments(int(month))
                folder_path = args.file
                file_path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
                file_list = glob.glob(f"{folder_path}/{file_path}")
                report = Report()

                for file_data in file_list:
                    parse = Parser(file_data)
                    parsed_file = parse.parser()
                    month = Statistics(parsed_file)

                    max_temperature, min_temperature, humidity, length_of_file = month.sum_call()
                    average_highest = month.highest_average(max_temperature, length_of_file)
                    average_lowest = month.lowest_average(min_temperature, length_of_file)
                    average_humidity = month.average_humidity(humidity, length_of_file)
                    month.print(average_highest, average_lowest, average_humidity)

                    report.report(average_highest, average_lowest, average_humidity)

            if args.e:
                year = args.e
                folder_path = args.file
                file = self.files_list(year, folder_path)
                year = Statistics(file)
                report = Report()
                max_temperature, min_temperature, humidity, date_max_temperature, date_min_temperature, date_humidity = year.annual_operations()
                year.print_annual(max_temperature, min_temperature, humidity, date_max_temperature,
                                  date_min_temperature, date_humidity)
                report.report(max_temperature, min_temperature, humidity)

            if args.c:
                year, month = args.c.split('/')
                month = self.month_year_from_arguments(int(month))
                folder_path = args.file
                file_path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
                file_list = glob.glob(f"{folder_path}/{file_path}")

                for file_data in file_list:
                    parse = Parser(file_data)
                    parsed_file = parse.parser()
                    chart = Charts(parsed_file)
                    chart.max_temperature_chart()
                    chart.min_temperature_chart()
                    chart.combine_chart()


main_call = Main()
main_call.command_line_arguments()
