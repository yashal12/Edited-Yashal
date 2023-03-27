import argparse
import csv
import glob
import os


class Weatherman:


    def parser(self, file):

        list_of_data = []
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            for rows in reader:
                list_of_data.append(rows)

        return list_of_data

    def search_files(self, year):

        folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
        path = '*' + str(year) + '_*txt'  # search for files in directory
        files = glob.glob(folder_path + path)

        return files

    def read_temperature(self, read):

        self.max_column = read['Max TemperatureC']
        self.min_column = read['Min TemperatureC']
        self.humidity_column = read['Max Humidity']

    def constants(self):

        max_temp = 0
        min_temp = 0
        humidity = 0
        date_max_temp = 0
        date_min_temp = 0
        date_humidity = 0

        return max_temp
        return min_temp
        return humidity

    def isEmpty_max(self):

        if self.max_column == '':
            max_column = 0

    def isEmpty_min(self):

        if self.min_column == '':
            min_column = 0

    def isEmpty_humidity(self):

        if self.humidity_column == '':
            humidity_column = 0

    def annual_temperature(self, year):

        files = self.search_files(year)
        length = len(files)
        # max_temp = self.constants()
        # min_temp = self.constants()
        # humidity = self.constants()
        # date_max_temp = self.constants()
        # date_min_temp = self.constants()
        # date_humidity = self.constants()

        for traverse in range(length):
            traverse_files = files[traverse]

            read_files = self.parser(traverse_files)

            for read in read_files:
                max_column = self.read_temperature(read)

                max_temp = self.constants()
                self.isEmpty_max()

                if float(self.max_column) > max_temp:
                    max_temp = float(self.max_column)
                    date_max_temp = read['PKT']

            for read in read_files:
                min_column = self.read_temperature(read)

                min_temp = self.constants()
                self.isEmpty_min()

                if float(self.min_column) > min_temp:
                    min_temp = float(self.min_column)
                    date_min_temp = read['PKT']

            for read in read_files:
                humidity_column = self.read_temperature(read)

                humidity = self.constants()
                self.isEmpty_humidity()

                if float(self.humidity_column) > humidity:
                    humidity = float(self.humidity_column)
                    date_humidity = read['PKT']

        print(f"\n{max_temp} on {date_max_temp}")
        print(f"\n{min_temp} on {date_min_temp}")
        print(f"\n{humidity} on {date_humidity}")

        self.report(max_temp, min_temp, humidity)

    def report(self, max_temp, min_temp, humidity):

        result = []
        result.append(max_temp)
        result.append(min_temp)
        result.append(humidity)

        # print(result)

    def monthly_temperature(self, file):

        self.constants()
        read_files = self.parser(file)
        length = len(read_files)

        for read in read_files:
            self.read_temperature(read)

            self.isEmpty_max()
            self.isEmpty_min()
            self.isEmpty_humidity()
            add_max_temp = self.constants()
            add_min_temp = self.constants()
            add_humidity = self.constants()

            add_max_temp += float(self.max_column)
            add_min_temp += float(self.min_column)
            add_humidity += float(self.humidity_column)

        average_max = add_max_temp / length
        average_min = add_min_temp / length
        average_humidity = add_humidity / length

        print("\nAverage max temperature", average_max)
        print("\nAverage min temperature", average_min)
        print("\nAverage humidity", average_humidity)

        self.report(average_max, average_min, average_humidity)

    def barchart(self, file):

        read_files = self.parser(file)
        row = '+ '
        length = len(read_files)

        for read_length in range(length):
            for read in read_files:
                date = read['PKT']

                max_column = self.read_temperature(read)
                min_column = self.read_temperature(read)
                self.isEmpty_max
                self.isEmpty_min()

                string = int(self.max_column) * row
                string2 = int(self.min_column) * row

        print(f"\n{date} {string} {self.max_column}")
        print(f"\n{date} {string2} {self.min_column}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--year')
    parser.add_argument('--month')
    parser.add_argument('--barchart')
    args = parser.parse_args()

    if args.year:
        year = args.year
        year_call = Weatherman()
        year_call.annual_temperature(year)
    # print(args.year)
    if args.month:
        file = args.month
        # file = '/Users/yashal.imran/Downloads/weatherfiles/Murree_weather_2011_Apr.txt'
        month_call = Weatherman()
        month_call.monthly_temperature(file)
    # print(args.month)
    if args.barchart:
        file = args.barchart
        chart_call = Weatherman()
        chart_call.barchart(file)
    # print(args.barchart)
