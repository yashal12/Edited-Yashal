import glob
import matplotlib.pyplot as plt
import os
import pandas as pd
class Weatherman:
    def parser():
        global final_df, df
        final_df = pd.DataFrame()
        folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
        # Get a list of all files in the folder with extensions .tsv, .txt, and .xlsx
        files = glob.glob(os.path.join(folder_path, "*.tsv")) + \
                glob.glob(os.path.join(folder_path, "*.txt")) + \
                glob.glob(os.path.join(folder_path, "*.xlsx"))

        for file in files:  # Loop through each file in the list and read it using pandas
            if file.endswith(".tsv"):

                df = pd.read_csv(file, delimiter="\t", )
                final_df = pd.concat([final_df, df], ignore_index=True)

                # print_all_rows = pd.set_option('display.max_rows', None)
                # print(print_all_rows)
                # print_all_cols = pd.set_option('display.max_columns', None)
                # print(print_all_cols)

            elif file.endswith(".txt"):  # Read TXT file using pandas
                df = pd.read_csv(file)
                final_df = pd.concat([final_df, df], ignore_index=True)

            elif file.endswith(".xlsx"):
                df = pd.read_excel(file)
                final_df = pd.concat([final_df, df], ignore_index=True)

        final_df.shape
        print(final_df)

    def yearwise_temperature():
        folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
        year = input('Enter the year of interest: ')
        path = '*' + str(year) + '_*.*'
        files = glob.glob(folder_path + '/' + path)

        final_df['PKT'] = pd.to_datetime(df['PKT'])  #convert a column in a DataFrame to a pandas datetime format.
        final_df['PKT'] = final_df['PKT'].dt.year

        max_temp = final_df.groupby('PKT')['Max TemperatureC'].max().reset_index()
        print(max_temp)

        min_temp = final_df.groupby('PKT')['Min TemperatureC'].min().reset_index()
        print(min_temp)

        humidity = final_df.groupby('PKT')['Max Humidity'].max().reset_index()
        print(humidity)

    def month_wise_temperature():
        folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
        month = str(input('Enter the month of interest: '))
        path = '*' + str(month) + '_*.*'
        files = glob.glob(folder_path + '/' + path)

        for i in files:
            final_df['PKT'] = pd.to_datetime(df['PKT'])
            final_df['PKT'] = final_df['PKT'].dt.month

            max_highest_temp = final_df.groupby('PKT')['Mean TemperatureC'].max().reset_index()
            avg_max_mean_temp = max_highest_temp.mean()

            min_lowest_temp = final_df.groupby('PKT')['Mean TemperatureC'].min().reset_index()
            avg_min_mean_temp = min_lowest_temp.mean()

            avg_mean_humidity = final_df.groupby('PKT')['Mean Humidity'].mean().reset_index()


        print('\nmean_highest_temp\n', avg_max_mean_temp)
        print("avg_min_mean_temp", avg_min_mean_temp)
        print("avg_mean_humidity", avg_mean_humidity)

    def charts():
        month = int(input("Enter month: "))
        folder_path = '/Users/yashal.imran/Downloads/weatherfiles/'
        month = int(input("Enter month: "))
        path = '*' + str(month) + '_*.*'
        files = glob.glob(folder_path + '/' + path)

        for i in files:
            if final_df['PKT'] == month:

                max_temp = final_df['Max TemperatureC'].plot.barh(color=red)
                print(max_temp)

                min_temp = final_df['Min TemperatureC'].plot.barh(color=red)
                print(min_temp)

obj = Weatherman
obj.parser()
obj.yearwise_temperature()
obj.month_wise_temperature()
obj.charts()