# coding=utf-8
# Python скрипт для тестирования времени загрузки в Pandas DataFrame данных с информации об основных расходах
# электрической энергии домохозяйствами, собранных в течение 47 месяцев (12.2006 — 11.2010)
# https://docs.python.org/2/library/timeit.html
# http://wesmckinney.com/blog/a-new-high-performance-memory-efficient-file-parser-engine-for-pandas/

import time
import pandas as pd
# this module provides access to the garbage collector for reference cycles
import gc

_filenames = {
    'filename1': 'csv-raw/household_cut.csv',
    'filename2': 'csv-raw/household_power_consumption.csv',
    'filename3': 'csv-raw/household_power_consumption.txt'
}

_delimiters = {
    'empty': ' '
}


def pandas_timings(exclude=()):
    result = {}
    for name, path in _filenames.iteritems():
        if name in exclude:
            continue

        print name

        delim = _delimiters.get(name, ';')

        start = time.time()
        table = pd.read_csv(path,
                            engine='python',
                            delimiter=';',
                            skiprows=1,
                            index_col=False,
                            header=1,
                            names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                                   "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                            )
        end = time.time()

        result[name] = end - start

        print '%s took %.2f sec' % (name, result[name])

        table = None
        # do a full collection right now
        gc.collect()

    return result


results = {
    'pandas': pandas_timings()
}

results = pd.DataFrame(results)

print results
