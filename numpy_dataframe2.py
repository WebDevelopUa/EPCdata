# coding=utf-8
# Python скрипт для загрузки в NumPy DataFrame данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок

# You can install packages via commands such as:
# python -m pip install numpy

from io import StringIO
import numpy as np

# присваиваем переменным имена файлов, которые будем тестировать, передавая в функцию
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'
output_file1 = 'export_data_cut_one_np'
output_file2 = 'export_data_task_one_np'


# создадим функцию для загрузки содержимого файла (.csv) в NumPy с помощью функции recfromtxt()
# можно использовать аналогичные функции: genfromtxt(), loadtxt(), recfromcsv()
def read_csv_file_np(filename):
    my_data = np.recfromtxt('csv-raw/' + filename,
                            delimiter=';',
                            # dtype=None,
                            # dtype=float,
                            names={"Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                                   "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"}

                            )

    return my_data


# вывод данных файлов в DataFrame
print(read_csv_file_np(filename2))
