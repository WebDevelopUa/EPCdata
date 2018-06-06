# coding=utf-8
# Python скрипт для загрузки в NumPy DataFrame данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок

# TASK #3 - Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А

import numpy as np
import csv

# присваиваем переменным имена файлов, которые будем тестировать, передавая в функцию
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'
output_file1 = 'export_data_cut_3rd_np.csv'
output_file2 = 'export_data_task_3rd_np.csv'


# создадим функцию для загрузки содержимого файла (.csv) в NumPy с помощью функции recfromtxt()
# можно использовать аналогичные функции: genfromtxt(), loadtxt(), recfromcsv()
def read_csv_file_np(filename):
    np_data = np.genfromtxt('csv-raw/' + filename,
                            delimiter=';',
                            # encoding='utf-8',
                            dtype=None,
                            # dtype=float,
                            # skip_header=1,

                            )

    # TASK #3 - Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А
    # выдод данных [ряд, столбец] c 0 позиции (: - все данные рядов, определенного столбца)
    return np_data[
        (np_data[:, 5] > '19') & (np_data[:, 5] < '20') & (np_data[:, 5] != '?') & (np_data[:, 8] < np_data[:, 6])
        ]


# экспорт даных в новый файл в папке csv
with open('csv/' + output_file2, 'wb') as new_file:
    wr = csv.writer(new_file,
                    delimiter=';',
                    quotechar='\n',
                    quoting=csv.QUOTE_MINIMAL
                    )
    wr.writerow(read_csv_file_np(filename2))
