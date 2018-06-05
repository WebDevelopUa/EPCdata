# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame данных с информацией об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок

import pandas as pd

# присваиваем переменным имена файлов, с которыми будем работать
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'
output_file1 = 'export_data_cut_one_pd.csv'
output_file2 = 'export_data_task_one_pd.csv'


def read_csv_file_pd(filename):
    df = pd.read_csv('csv-raw/' + filename,
                     engine='python',
                     delimiter=';',
                     skiprows=1,
                     index_col=False,
                     names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                            "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                     )

    # TASK #1 - выбрать все домохозяйства, в которых общая активная потребляемая мощность превышает 5 кВт
    return df[(df['Global_active_power'] > '5') & (df['Global_active_power'] != '?')]


# экспорт даных с DataFrame в новый файл в папке csv
read_csv_file_pd(filename2).to_csv('csv/' + output_file2,
                                   encoding='utf-8',
                                   # не выводить в файл .csv индекс таблицы:
                                   index=False,
                                   # не выводить в файл .csv заголовок таблицы:
                                   header=False
                                   )
