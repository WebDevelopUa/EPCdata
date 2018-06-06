# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame данных с информацией об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# и реализации процедур для формирования выборок
# https://gist.github.com/bsweger/e5817488d161f37dcbd2

# TASK #3 - Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А

import pandas as pd

# присваиваем переменным имена файлов, с которыми будем работать
filename1 = 'household_cut.csv'
filename2 = 'household_power_consumption.csv'
output_file1 = 'export_data_cut_3rd_pd.csv'
output_file2 = 'export_data_task_3rd_pd.csv'


def read_csv_file_pd(filename):
    df = pd.read_csv('csv-raw/' + filename,
                     engine='python',
                     encoding='utf-8',
                     # dtype='float64',
                     # dtype=float,
                     delimiter=';',
                     # delimiter=';| ',
                     # sep='\t',
                     # sep='',
                     # sep=';',
                     # delimiter=',|;',
                     # skiprows=1,
                     # header=None,
                     # skipinitialspace=True,
                     # header=1,
                     # index_col=False,
                     names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                            "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                     # converters={ 'Sub_metering_3': int},
                     )

    # TASK #3 - Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А
    return df[(df['Sub_metering_1'] > df['Sub_metering_3'])].query(
        'Global_intensity > "19" and Global_intensity < "20" ')

    # return df[((df['Global_intensity'] > '19') & (df['Global_intensity'] < '20') & (df['Global_intensity'] != '?')) &
    # (df['Sub_metering_3'] < df['Sub_metering_1'])]
    # return df[(df['Sub_metering_1'] > df['Sub_metering_3'])].query('Global_intensity != "?"')
    # return df[((df['Global_intensity'] > '19') & (df['Global_intensity'] < '20'))]
    # return df.apply(pd.to_numeric, errors='ignore').dtypes
    # return df.dtypes
    # return df


# print read_csv_file_pd(filename2)

# экспорт даных с DataFrame в новый файл в папке csv
read_csv_file_pd(filename2).to_csv('csv/' + output_file2,
                                   encoding='utf-8',
                                   # не выводить в файл .csv индекс таблицы:
                                   index=False,
                                   # не выводить в файл .csv заголовок таблицы:
                                   header=False
                                   )
