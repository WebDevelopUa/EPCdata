# coding=utf-8
# Python скрипт для тестирования времени загрузки в NumPy in Python  данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок
# pandas это высокоуровневая Python библиотека для анализа данных
# https://docs.python.org/2/library/timeit.html
# https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html
# https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
# https://www.geeksforgeeks.org/numpy-python-set-2-advanced/
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.io.genfromtxt.html

# You can install packages via commands such as:
# python -m pip install numpy

from io import StringIO
import numpy as np

# присваиваем переменным имена файлов, которые будем тестировать, передавая в функцию
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'


# создадим функцию для загрузки содержимого файла (.csv) в NumPy с помощью функции recfromtxt()
def read_csv_file(filename):
    # можно использовать аналогичные функции
    # my_data = np.genfromtxt('csv-raw/' + filename,
    # my_data = np.loadtxt('csv-raw/' + filename,
    # my_data = np.recfromcsv('csv-raw/' + filename,
    my_data = np.recfromtxt('csv-raw/' + filename,
                            delimiter=';',
                            # dtype=None,
                            # dtype=float,
                            names={"Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                                   "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"}

                            )

    return my_data


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
