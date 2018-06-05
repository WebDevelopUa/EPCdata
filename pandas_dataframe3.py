# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame данных с информацией об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок

import pandas as pd

# загрузим файл .csv с помощью функции read_csv() и отформатируем вывод данных
df = pd.read_csv('csv-raw/household_power_consumption.csv',
                 engine='python',
                 delimiter=';',
                 skiprows=1,
                 index_col=False,
                 names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                        "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                 )

# вывод имен столбцов
print list(df.columns.values)

# TASK #1 - выбрать все домохозяйства, в которых общая активная потребляемая мощность превышает 5 кВт
print('\n выбрать все домохозяйства, в которых общая активная потребляемая мощность превышает 5 кВт: \n')
task_one_frame = df[(df['Global_active_power'] > '5') & (df['Global_active_power'] != '?')]

# экспорт даных с DataFrame в новый файл в папке csv
task_one_frame.to_csv('csv/task_one_frame.csv')

# empty data fields ?
task_one_frame_empty = df[(df['Global_active_power'] == '?')]
task_one_frame_empty.to_csv('csv/task_one_frame_empty.csv')

# NAN data fields
task_one_frame_nan = df[(df['Global_active_power'].isnull())]
task_one_frame_nan.to_csv('csv/task_one_frame_nan.csv')

# zero data fields
task_one_frame_zero = df[(df['Global_active_power'] == '0')]
task_one_frame_zero.to_csv('csv/task_one_frame_zero.csv')
