# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame данных с информацией об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок
# pandas это высокоуровневая Python библиотека для анализа данных
# https://jeffdelaney.me/blog/useful-snippets-in-pandas/
# https://docs.python.org/2/library/timeit.html

import pandas as pd


# создадим функцию для загрузки содержимого файла (.csv) в Pandas DataFrame с помощью функции read_csv()
def read_csv_file():
    # присваиваем переменной имя файла, с которым будем работать
    filename1 = 'household_cut.csv'
    filename2 = 'household_power_consumption.csv'
    filename3 = 'household_power_consumption.txt'

    # указать имя файла из вышеуказанных
    df = pd.read_csv('csv-raw/' + filename1,
                     engine='python',
                     delimiter=';',
                     skiprows=1,
                     index_col=False,
                     header=1,
                     names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                            "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                     )

    return df


# создадим функцию для экспорта первых 20 строк даных с DataFrame в новый файл в папке csv
def first_20_rows():
    csv_data = read_csv_file()
    csv_data[:20].to_csv('csv/export_data2.csv')


# выполнить скрипт (Run ... )
if __name__ == '__main__':
    first_20_rows()
