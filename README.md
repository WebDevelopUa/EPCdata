# EPCdata

## 	Electric power consumption Data filter for Individual household





### Data Set Information:
This archive contains 2075259 measurements gathered between December 2006 and November 2010 (47 months).  



#### Download Individual household electric power consumption Data Set: 

https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip



#### *Notes*:  

1) (global_active_power*1000/60 - sub_metering_1 - sub_metering_2 - sub_metering_3) represents the active energy consumed every minute (in watt hour) in the household by electrical equipment not measured in sub-meterings 1, 2 and 3.  

2) The dataset contains some missing values in the measurements (nearly 1,25% of the rows). All calendar timestamps are present in the dataset but for some timestamps, the measurement values are missing: a missing value is represented by the absence of value between two consecutive semi-colon attribute separators. For instance, the dataset shows missing values on April 28, 2007.

### Attribute Information:
1) **date**: Date in format dd/mm/yyyy

2) **time**: time in format hh:mm:ss  

3) **global_active_power**: household global minute-averaged active power (in kilowatt)  

4) **global_reactive_power**: household global minute-averaged reactive power (in kilowatt)  

5) **voltage**: minute-averaged voltage (in volt)  

6) **global_intensity**: household global minute-averaged current intensity (in ampere)  

7) **sub_metering_1**: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).  

8) **sub_metering_2**: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.  

9) **sub_metering_3**: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.


----


### Ход выполнения работы
В ходе выполнения работы необходимо оценить время выполнения поставленной задачи 

* с использованием массивов NumPy (numpy array) 
* и фреймов (Python Pandas - DataFrame)

Для каждой из структур данных нужно выполнить профилирование времени выполнения (использовать **timeit** из одноименного модуля).

Загрузить пакет данных с информацией об основных расходах электрической энергии домохозяйствами, собранные в течение 47 месяцев (12.2006 — 11.2010) можно по ссылке:

https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip

### Перечень атрибутивной информации:
1) **date**: дата измерения в формате dd / mm / yyyy
2) **time**: время в формате hh: mm: ss
3) **global_active_power**: активная мощность, которую потребляет домохозяйство в минуту (усредненно) [кВт]
4) **global_reactive_power**: реактивная мощность, которую потребляет домохозяйство в минуту (усредненно) [кВт]
5) **voltage**: напряжение, усредненная в минуту наблюдения [В]
6) **global_intensity**: усредненная силу тока для домохозяйства [A]
7) **sub_metering_1**: набор потребителей энергии №1 [Вт-часов активной энергии], соответствует кухни, на которой машина для мытья посуды и микроволновка (электрической плиты нет, используется газовая).
8) **sub_metering_2**: набор потребителей энергии №2 [Вт-часов активной энергии], соответствует прачечной, в которой работает стиральная машина, сушилка, холодильных и включен свет.
9) **sub_metering_3**: набор потребителей энергии №3 [Вт-часов активной энергии], соответствует бойлеру и кондиционеру.



Выполнить все задания, используя   **numpy array**, так и **dataframe**, проанализировать временные затраты на выполнение процедур (профилирования времени выполнения), сделать выводы относительно ситуаций, в которых имеет смысл отдать предпочтение той или иной структуре данных. Выводы оформить отчетом с указанным временем выполнения и оценке по 5-балльной шкале удобства выполнения операций отбора).

Также стоит обратить внимание на то, что нужно оставить только те наблюдения, в которых нет пустых наблюдений

 1)	Выбрать все домохозяйства, в которых общая активная потребляемая мощность превышает 5 кВт.

 2) Выбрать все домохозяйства, в которых вольтаж превышает 235 В. 

 3)	Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А, для них обнаружить те, в которых стиральная машина и холодильных потребляют больше, чем бойлер и кондиционер.

 4)	Выбрать случайным образом 500 000 домохозяйств (без повторов элементов выборки), для них вычислить средние величины всех 3-х групп потребления электрической энергии.

 5)	Выбрать те домохозяйства, после 18-00 потребляют более 6 кВт в минуту в среднем, среди отобранных определить те, в которых основное потребление электроэнергии в указанный промежуток времени приходится на стиральную машину, сушилку, холодильник и освещения (группа 2 является крупнейшей) , а затем выбрать каждый третий результат с первой половины и каждый четвертый результат со второй половины.


#### Ссылки:


* https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

* http://pandas.pydata.org/pandas-docs/version/0.15.2/index.html

* https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm


* http://scipy-lectures.github.io/intro/numpy/numpy.html

* https://docs.python.org/2/library/timeit.html

* https://www.programcreek.com/python/example/1834/timeit.Timer

* https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip


