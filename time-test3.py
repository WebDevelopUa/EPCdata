# coding=utf-8
# Python скрипт для тестирования времени загрузки в Pandas DataFrame данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок
# pandas это высокоуровневая Python библиотека для анализа данных
# https://docs.python.org/2/library/timeit.html
# http://xahlee.info/python/python_timing_functions_timeit.html

import pandas as pd

# присваиваем переменным имена файлов, которые будем тестировать, передавая в функцию
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'


# создадим функцию для загрузки содержимого файла (.csv) в Pandas DataFrame с помощью функции read_csv()
def read_csv_file(filename):
    # указать имя файла из вышеуказанных
    df = pd.read_csv('csv-raw/' + filename,
                     engine='python',
                     delimiter=';',
                     skiprows=1,
                     index_col=False,
                     header=1,
                     names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                            "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                     )

    return df


# вывод данных файлов в DataFrame
# print(read_csv_file(filename1))
# print(read_csv_file(filename2))


# выполнить скрипт (Run ... )
if __name__ == '__main__':
    import timeit

    print 'Время выполнения функции read_csv_file() для файла filename1=' + filename1
    print timeit.repeat("read_csv_file(filename1)", setup="from __main__ import read_csv_file, filename1",
                        number=1, repeat=3)

    print 'Время выполнения функции read_csv_file() для файла filename2=' + filename2
    print timeit.repeat("read_csv_file(filename2)", setup="from __main__ import read_csv_file, filename2",
                        number=1, repeat=3)
