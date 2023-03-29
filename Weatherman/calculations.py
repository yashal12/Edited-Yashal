import glob

from parser import Parser


class AnnualStatistics:

    def __init__(self, year):
        self.year = year

    def search_files(self):
        folder_path = '/Users/yashal.imran/Downloads/weatherfiles'
        file_path = "*" + str(self.year) + '_*txt'  # search for files in directory
        files = glob.glob(f"{folder_path}/{file_path}")

        return files

    def annual_operations(self):

        store_highest_temperature = store_humidity = 0
        store_lowest_temperature = 500
        files = self.search_files()

        for traverse in range(len(files)):
            traverse_files = files[traverse]

            file_read = Parser(traverse_files).parser()

            for read_data in file_read:
                if float(read_data['Max TemperatureC']) > store_highest_temperature:
                    store_highest_temperature = float(read_data['Max TemperatureC'])
                    date_highest_temperature = read_data['PKT']

                if float(read_data['Min TemperatureC']) < store_lowest_temperature:
                    store_lowest_temperature = float(read_data['Min TemperatureC'])
                    date_lowest_temperature = read_data['PKT']

                if float(read_data['Max Humidity']) > store_humidity:
                    store_humidity = float(read_data['Max Humidity'])
                    date_humidity = read_data['PKT']

        return store_highest_temperature, store_lowest_temperature, store_humidity, date_highest_temperature, date_lowest_temperature, date_humidity

    def print(self, store_highest_temperature, store_lowest_temperature, store_humidity, date_highest_temperature, date_lowest_temperature, date_humidity):
        print(f"\nHighest: {store_highest_temperature} on {date_highest_temperature} \nLowest: {store_lowest_temperature} on {date_lowest_temperature}"
              f"\nHumidity: {store_humidity} on {date_humidity}")


class Month:

    def __init__(self, list_of_file):

        self.list_of_file = list_of_file

    def add_highest_temperature(self):

        store_highest_temperature = 0
        length_of_file = len(self.list_of_file)

        for read_data in self.list_of_file:
            if read_data['Max TemperatureC']:
                store_highest_temperature += float(read_data['Max TemperatureC'])

        return store_highest_temperature, length_of_file

    def highest_average(self, store_highest_temperature, length_of_file):

        average_highest = store_highest_temperature / length_of_file
        print("\nHighest Average: ", average_highest)

        return average_highest

    def add_lowest_temperature(self, length_of_file):

        store_lowest_temperature = 0

        for read_data in self.list_of_file:
            if read_data['Min TemperatureC']:
                store_lowest_temperature += float(read_data['Min TemperatureC'])

        return store_lowest_temperature

    def lowest_average(self, store_lowest_temperature, length_of_file):

        average_lowest = store_lowest_temperature / length_of_file
        print("\nLowest Average:", average_lowest)

        return average_lowest

    def add_humidity(self, length_of_file):

        store_humidity = 0

        for read_data in self.list_of_file:
            if read_data['Max Humidity']:
                store_humidity += float(read_data['Max Humidity'])

        return store_humidity

    def average_humidity(self, store_humidity, length_of_file):

        average_humidity = store_humidity / length_of_file
        print("\nLowest Average:", average_humidity)

        return average_humidity
