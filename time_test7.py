# coding=utf-8
# Python скрипт для тестирования времени загрузки в NumPy & Pandas данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)

# 3) Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А,
# для них обнаружить те, в которых стиральная машина и холодильных потребляют больше, чем бойлер и кондиционер.
# **numpy array**, так и **dataframe**, проанализировать временные затраты на выполнение процедур,
# сделать выводы относительно ситуаций, в которых имеет смысл отдать предпочтение той или иной структуре данных.
# оформить отчетом с указанным временем выполнения и оценке по 5-балльной шкале удобства выполнения операций отбора)

# Отчет #3:
# Время выполнения функции Pandas read_csv_file_pd() для файла household_power_consumption.csv: 14 - 16 секунд (5 балов)
# Время выполнения функции NumPy  read_csv_file_np() для файла household_power_consumption.csv: 69 - 72 секунды (2 бала)
# Ошибки -> Pandas -> выдает значения Global_intensity 2.000 ... 2.600 ... 2.800, при заданом фильтре:
# return df[((df['Global_intensity'] > '19') & (df['Global_intensity'] < '20'))] или
# return df.query('Global_intensity > "19" and Global_intensity < "20" ')
# Ошибки -> NumPy -> выдает значения Global_intensity 2.000 ... 2.600 ... 2.800,
# а также, (Sub_metering_1) '2.000' < (Sub_metering_3) '17.000', попадает в таблицу при заданом фильтре:
# np_data[(np_data[:, 5] > '19') & (np_data[:, 5] < '20') & (np_data[:, 5] != '?') & (np_data[:, 8] < np_data[:, 6])]

import timeit

filename2 = 'household_power_consumption.csv'

print '\n' + 'Задание #3'
print '\n' + 'Время выполнения функции (Pandas) read_csv_file_pd() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_pd(filename2)",
                    setup="from pandas_dataframe7 import read_csv_file_pd, filename2",
                    number=1,
                    repeat=3
                    )

print '\n' + 'Время выполнения функции (NumPy) read_csv_file_np() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_np(filename2)",
                    setup="from numpy_dataframe7 import read_csv_file_np, filename2",
                    number=1,
                    repeat=3
                    )
