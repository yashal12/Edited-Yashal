import csv
import glob
import os

result = []

def parser(file):

    list_of_data = []
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        for rows in reader:
            list_of_data.append(rows)
            print(list_of_data)

    return list_of_data

def yearwise_temperature(year):

    folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
    path = '*' + str(year) + '_*txt'  # search for files in directory
    files = glob.glob(folder_path + path)
    length = len(files)

    max_file = 0
    max_temp = 0
    min_file = 0
    min_temp = 0
    humidity_file = 0
    humidity = 0
    date_max_temp = 0
    date_min_temp = 0
    date_humidity = 0

    for traverse in range(length):
        traverse_files = files[traverse]

        read_files = parser(traverse_files)

        for read in read_files:
            max_file = read['Max TemperatureC']

            if max_file == '':
                max_file = 0
            if float(max_file) > max_temp:
                max_temp = float(max_file)
                date_max_temp = read['PKT']

        for read in read_files:
            min_file = read['Min TemperatureC']

            if min_file == '':
                min_file = 0
            if float(min_file) > min_temp:
                min_temp = float(min_file)
                date_min_temp = read['PKT']

        for read in read_files:
            humidity_file = read['Max Humidity']

            if humidity_file == '':
                humidity_file = 0
            if float(humidity_file) > humidity:
                humidity = float(humidity_file)
                date_humidity = read['PKT']

    print(f"\n{max_temp} on {date_max_temp}")
    print(f"\n{min_temp} on {date_min_temp}")
    print(f"\n{humidity} on {date_humidity}")

    result.append(max_temp)
    result.append(min_temp)
    result.append(humidity)

def monthwise_temperature(file):

    add_max_temp = add_min_temp = add_humidity = 0
    read_files = parser(file)
    length = len(parser(file))

    for read in read_files:
        max_file = read['Max TemperatureC']

        min_file = read['Min TemperatureC']
        humidity_file = read['Max Humidity']

        if max_file == '' or min_file == '' or humidity_file == '':
            max_file = 0
            min_file = 0
            humidity_file = 0
        else:
            add_max_temp += float(max_file)
            add_min_temp += float(min_file)
            add_humidity += float(humidity_file)

    average_max = add_max_temp / length
    average_min = add_min_temp / length
    average_humidity = add_humidity / length

    print("\nAverage max temperature", average_max)
    print("\nAverage min temperature", average_min)
    print("\nAverage humidity", average_humidity)

    result.append(average_max)
    result.append(average_min)
    result.append(average_humidity)

def charts(file):

    read_files = parser(file)
    row = '+ '
    string = 0
    string2 = 0
    max_temp = 0
    max_temp = 0
    length = len(read_files)

    for read_length in range(length):
        for read in read_files:
            date = read['PKT']

            max_temp = read['Max TemperatureC']
            min_temp = read['Min TemperatureC']
            if max_temp == '':
                max_temp = 0
            if min_temp == '':
                min_temp = 0

            string = int(max_temp) * row
            string2 = int(min_temp) * row

    print(f"\n{date} {string} {max_temp}")
    print(f"\n{date} {string2} {min_temp}")


file_path = '/Users/yashal.imran/Downloads/weatherfiles/Murree_weather_2011_Apr.txt'
parser(file_path)
yearwise_temperature('2015')
monthwise_temperature(file_path)
charts(file_path)