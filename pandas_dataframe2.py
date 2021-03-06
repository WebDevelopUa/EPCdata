# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame данных с информацией об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок
# pandas это высокоуровневая Python библиотека для анализа данных
# https://jeffdelaney.me/blog/useful-snippets-in-pandas/
# https://docs.python.org/2/library/timeit.html

import pandas as pd

# присваиваем переменной имя файла, с которым будем работать
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'
filename3 = 'household_power_consumption.txt'
output_file1 = 'export_data1.csv'
output_file2 = 'export_data2.csv'


# создадим функцию для загрузки содержимого файла (.csv) в Pandas DataFrame с помощью функции read_csv()
def read_csv_file(filename):
    df = pd.read_csv('csv-raw/' + filename,
                     engine='python',
                     delimiter=';',
                     skiprows=1,
                     # parse_dates=True,
                     index_col=False,
                     header=1,
                     names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                            "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                     )

    return df


# вывод данных файлов в DataFrame
# print read_csv_file(filename1)
# print read_csv_file(filename2)

# создадим функцию для экспорта первых 20 строк даных с DataFrame в новый файл в папке csv
def first_20_rows(input_file, output_file):
    csv_data = read_csv_file(input_file)
    csv_data[:20].to_csv('csv/' + output_file + '.csv',
                         encoding='utf-8',
                         # не выводить в файл .csv индекс таблицы:
                         index=False,
                         # не выводить в файл .csv заголовок таблицы:
                         header=False
                         )


# выполнить скрипт (Run ... )
if __name__ == '__main__':
    import timeit

    print 'Время выполнения функции first_20_rows() для файла filename1=' + filename1
    print timeit.repeat("first_20_rows(filename1, 'output_file1')",
                        setup="from __main__ import first_20_rows, filename1, output_file1",
                        number=1,
                        repeat=3
                        )

    print 'Время выполнения функции first_20_rows() для файла filename2=' + filename2
    print timeit.repeat("first_20_rows(filename2, 'output_file2')",
                        setup="from __main__ import first_20_rows, filename2, output_file2",
                        number=1,
                        repeat=3
                        )
