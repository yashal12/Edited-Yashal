import argparse
import calendar
import csv
import glob
import os


class Parser:


    def __init__(self, file):

        self.file = file

    def parser(self):

        list_of_data = []
        with open(self.file, 'r') as file_name:
            reader = csv.DictReader(file_name)

            for rows in reader:
                list_of_data.append(rows)

        return list_of_data


class Month:


    def __init__(self, list_of_file):

        self.list_of_file = list_of_file

    def compute_sum(self):

        max_temp = min_temp = max_humidity = 0
        length = len(self.list_of_file)

        for row in self.list_of_file:
            if row['Max TemperatureC']:
                max_temp += float(row['Max TemperatureC'])

            if row['Min TemperatureC']:
                min_temp += float(row['Min TemperatureC'])

            if row['Max Humidity']:
                max_humidity += float(row['Max Humidity'])

        return max_temp, min_temp, max_humidity, length

    def compute_average(self, max_temp, min_temp, max_humidity, length):

        average_max = max_temp / length
        average_min = min_temp / length
        average_humidity = max_humidity / length

        print("\nHighest Average: ", average_max)
        print("\nLowest Average:", average_min)
        print("\nAverage mean humidity: ", average_humidity)

        self.report(average_max, average_min, average_humidity)

    def report(self, average_max, average_min, average_humidity):

        result = []
        result.append(average_max)
        result.append(average_min)
        result.append(average_humidity)


class Annual:


    def __init__(self, year):

        self.year = year

    def annual_temperature(self):

        max_temp = max_humidity = 0
        min_temp = 500
        path = '/Users/yashal.imran/Downloads/weatherfiles'
        format_file = "*" + str(self.year) + '_*txt'  # search for files in directory
        files = glob.glob(f"{path}/{format_file}")

        for traverse in range(len(files)):
            traverse_files = files[traverse]

            read = Parser(traverse_files).parser()

            for x in read:
                if float(x['Max TemperatureC']) > max_temp:

                    max_temp = float(x['Max TemperatureC'])
                    date_max_temp = x['PKT']

                if float(x['Min TemperatureC']) < min_temp:
                    min_temp = float(x['Min TemperatureC'])
                    date_min_temp = x['PKT']

                if float(x['Max Humidity']) > max_humidity:
                    max_humidity = float(x['Max Humidity'])
                    date_humidity = x['PKT']

        print(f"\nHighest: {max_temp} on {date_max_temp}")
        print(f"\nLowest: {min_temp} on {date_min_temp}")
        print(f"\nHumidity: {max_humidity} on {date_humidity}")

        self.report(max_temp, min_temp, max_humidity)

    def report(self, max_temp, min_temp, max_humidity):

        result = []
        result.append(max_temp)
        result.append(min_temp)
        result.append(max_humidity)


class Charts:


    def __init__(self, list_of_file):

        self.list_of_file = list_of_file

    def finding_max_min_temperature(self):

        max_column = min_column = 0

        for read in self.list_of_file:
            if float(read['Max TemperatureC']) > max_column:

                max_column = float(read['Max TemperatureC'])
                date_max_temp = read['PKT']

            if float(read['Min TemperatureC']) > min_column:
                min_column = float(read['Min TemperatureC'])
                date_min_temp = read['PKT']

        return max_column, min_column, date_max_temp, date_min_temp

    def charts(self):

        row = '+ '

        max_column, min_column, date_max_temp, date_min_temp = self.finding_max_min_temperature()
        string = '\033[31m' + int(max_column) * row + '\033[0m'  # Use red color for string
        print(f"\n{date_max_temp} {string} {max_column}")

        string2 = '\033[34m' + int(min_column) * row + '\033[0m'  # Use blue color for string2
        print(f"\n{date_min_temp} {string2} {min_column}")

def extract_filenames(j):

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
            month = extract_filenames(int(month))
            folder = args.file
            path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
            file_list = glob.glob(f"{folder}/{path}")

            for file in file_list:
                parse = Parser(file)

                parsed_file = parse.parser()
                monthly_temp = Month(parsed_file)
                max_temp, min_temp, max_humidity, length = monthly_temp.compute_sum()
                monthly_temp.compute_average(max_temp, min_temp, max_humidity, length)

        if args.e:
            year = args.e
            year_obj = Annual(year)
            year_obj.annual_temperature()

        if args.c:
            year, month = args.c.split('/')
            month = extract_filenames(int(month))
            folder = args.file
            path = 'Murree_weather_' + str(year) + '_' + str(month) + '.txt'
            file_list = glob.glob(f"{folder}/{path}")

            for file in file_list:
                parse = Parser(file)

                parsed_file = parse.parser()
                chart = Charts(parsed_file)
                chart.charts()


main()
