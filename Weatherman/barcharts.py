class Charts:

    def __init__(self, list_of_file):
        self.list_of_file = list_of_file

    def max_temperature_chart(self):
        for read_row in self.list_of_file:
            date_of_temperature = read_row['PKT']

            print(f"\n{date_of_temperature}", end=' ')
            print('\033[31m' + int(read_row['Max TemperatureC']) * '+ ' + '\033[0m', end=' ')
            print(f"{read_row['Max TemperatureC']}")

    def min_temperature_chart(self):
        for read_row in self.list_of_file:
            date_of_temperature = read_row['PKT']

            print(f"\n{date_of_temperature}", end=' ')
            print('\033[34m' + int(read_row['Min TemperatureC']) * '+ ' + '\033[0m', end=' ')
            print(f"{read_row['Min TemperatureC']}")

    def combine_chart(self):
        for read_row in self.list_of_file:
            date_of_temperature = read_row['PKT']

            print(f"\n{date_of_temperature}", end=' ')
            print('\033[31m' + int(read_row['Max TemperatureC']) * '+ ' + '\033[0m', '\033[34m' + int(read_row['Min TemperatureC']) * '+ ' + '\033[0m', end='')
            print(f"{read_row['Max TemperatureC']} {read_row['Min TemperatureC']}")
