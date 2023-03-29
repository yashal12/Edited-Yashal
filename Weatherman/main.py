import argparse
import calendar
import glob

from barcharts import Charts
from calculations import AnnualStatistics, Month
from parser import Parser
from report import Report


def store_month_year_from_arguments(j):
    month_abbreviations = calendar.month_abbr

    for i, month_ in enumerate(month_abbreviations):
        if i == j:
            return month_


def main():
    if __name__ == '__main__':

        parser = argparse.ArgumentParser()
        parser.add_argument('file')
        parser.add_argument('-a')
        parser.add_argument('-e')
        parser.add_argument('-c')
        args = parser.parse_args()

        if args.a:
            year, month = args.a.split('/')
            month = store_month_year_from_arguments(int(month))
            folder_path = args.file
            file_path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
            file_list = glob.glob(f"{folder_path}/{file_path}")

            for file in file_list:
                parse = Parser(file)
                parsed_file = parse.parser()
                month_object = Month(parsed_file)
                report_object = Report()

                highest_temperature, length_of_file = month_object.add_highest_temperature()
                average_highest = month_object.highest_average(highest_temperature, length_of_file)

                lowest_temperature = month_object.add_lowest_temperature(length_of_file)
                average_lowest = month_object.highest_average(lowest_temperature, length_of_file)

                humidity = month_object.add_humidity(length_of_file)
                average_humidity = month_object.average_humidity(humidity, length_of_file)

                report_object.report(average_highest, average_lowest, average_humidity)

        if args.e:
            year = args.e
            year_object = AnnualStatistics(year)
            report_object = Report()

            highest_temperature, lowest_temperature, humidity, date_highest_temperature, date_lowest_temperature, date_humidity = year_object.annual_operations()
            year_object.print(highest_temperature, lowest_temperature, humidity, date_highest_temperature,
                              date_lowest_temperature, date_humidity)

            report_object.report(highest_temperature, lowest_temperature, humidity)

        if args.c:
            year, month = args.c.split('/')
            month = store_month_year_from_arguments(int(month))
            folder_path = args.file
            file_path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
            file_list = glob.glob(f"{folder_path}/{file_path}")

            for file in file_list:
                parse = Parser(file)
                parsed_file = parse.parser()
                chart = Charts(parsed_file)
                # chart.max_temperature_chart()
                # chart.min_temperature_chart()
                chart.combine_chart()


main()
