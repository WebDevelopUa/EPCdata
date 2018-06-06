# coding=utf-8
# Python скрипт для тестирования времени загрузки в NumPy & Pandas данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)

# 2) Выбрать все домохозяйства, в которых вольтаж превышает 235 В.
# **numpy array**, так и **dataframe**, проанализировать временные затраты на выполнение процедур,
# сделать выводы относительно ситуаций, в которых имеет смысл отдать предпочтение той или иной структуре данных.
# оформить отчетом с указанным временем выполнения и оценке по 5-балльной шкале удобства выполнения операций отбора)

# Отчет #2:
# Время выполнения функции Pandas read_csv_file_pd() для файла household_power_consumption.csv: 11 - 13 секунд (5 балов)
# Время выполнения функции NumPy  read_csv_file_np() для файла household_power_consumption.csv: 57 - 94 секунды (2 бала)
# Предпочтение -> Pandas -> время выполнения операций отбора, экспортируемые отчеты более читабельные

import timeit

filename2 = 'household_power_consumption.csv'

print '\n' + 'Задание #2'
print '\n' + 'Время выполнения функции (Pandas) read_csv_file_pd() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_pd(filename2)",
                    setup="from pandas_dataframe6 import read_csv_file_pd, filename2",
                    number=1,
                    repeat=3
                    )

print '\n' + 'Время выполнения функции (NumPy) read_csv_file_np() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_np(filename2)",
                    setup="from numpy_dataframe6 import read_csv_file_np, filename2",
                    number=1,
                    repeat=3
                    )
