# coding=utf-8
# Python скрипт для тестирования времени загрузки в NumPy & Pandas данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)

import timeit

# import pandas as pd
# import numpy as np
# from pandas_dataframe5 import read_csv_file_pd
# from pandas_dataframe5 import filename2

filename2 = 'household_power_consumption.csv'

print 'Время выполнения функции read_csv_file_pd() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_pd(filename2)",
                    setup="from pandas_dataframe5 import read_csv_file_pd, filename2",
                    number=1,
                    repeat=3
                    )

print 'Время выполнения функции read_csv_file_np() для файла filename2=' + filename2
print timeit.repeat("read_csv_file_np(filename2)",
                    setup="from numpy_dataframe5 import read_csv_file_np, filename2",
                    number=1,
                    repeat=3
                    )
