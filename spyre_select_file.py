# coding=utf-8
# Spyre Скрипт, позволяющий выбирать из списка файл для отображения в табличном виде и на гистограмме в веб-браузере
# https://docs.python.org/3.1/library/csv.html

import os
import pandas as pd
from spyre import server


class SpyreSelectFile(server.App):
    # путь к директории с файлами
    path = "csv-raw"

    # заголовок
    title = "Spyre Select File"

    # выпадающий список с файлами из директории path (объявлено выше)
    inputs = [

        # выпадающий список (файлы)
        {
            "type": "dropdown",
            "id": "file",
            "key": 'file',

            "label": "Raw Data",
            "options": [
                {"label": filename, "value": filename} for filename in os.listdir(path)
            ],

            # значение по умолчанию
            "value": "household_cut.csv",
            "action_id": "update_data"
        }
    ]

    # кнопка ("Get Data | Загрузить данные")
    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "Get Data | Загрузить данные"
    }]

    # вкладки
    tabs = ["Table", "Plot", "Info"]

    # выходные данные
    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        },
        {
            "type": "html",
            "id": "custom_html",
            "tab": "Info"
        }

    ]

    #  функция считывания данных из файла (в DataFrame)
    def getData(self, params):
        filename = params["file"]
        df = pd.read_csv("csv-raw/" + filename,
                         delimiter=';',
                         engine='python',
                         index_col=False,
                         header=1,
                         names=["Date", "Time", "Global_active_power", "Global_reactive_power", "Voltage",
                                "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"],
                         )
        return df

    #  функция построения графика
    def getPlot(self, params):
        df = self.getData(params).set_index(['Date'])

        plot_obj = df.plot()
        # plot_obj.set_ylabel("y")
        # plot_obj.set_xlabel("x")
        # plot_obj.set_title("Display of Data for the selected period")
        # plot_obj.grid()
        line_plot = plot_obj.get_figure()
        return line_plot

    # метод стилизации
    def getCustomCSS(self):
        css = (
            "body { background: "
            "linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%) no-repeat fixed; }"
        )
        return css

    #  функция выводит информацию на страницу INFO
    def getHTML(self, params):
        return "<b>О приложении: </b>" \
               "<br/><br/><h1>Создать веб-приложение с использованием модуля Spyre:</h1>" \
               " <ul>" \
               "<li>Загрузить пакет данных с информацией об основных расходах электрической энергии домохозяйствами," \
               " собранные в течение 47 месяцев (12.2006 — 11.2010) можно по <a href='https://archive.ics.uci.edu/ml/" \
               "machine-learning-databases/00235/household_power_consumption.zip'>ссылке.</a></li>" \
               "<li>Выбрать все домохозяйства, в которых общая активная потребляемая мощность превышает 5 кВт.</li>" \
               "<li>Выбрать все домохозяйства, в которых вольтаж превышает 235 В. </li>" \
               "<li>Выбрать все домохозяйства, в которых сила тока лежит в пределах 19-20 А, для них обнаружить те," \
               " в которых стиральная машина и холодильных потребляют больше, чем бойлер и кондиционер.</li>" \
               "<li>Выбрать случайным образом 500 000 домохозяйств (без повторов элементов выборки)," \
               " для них вычислить средние величины всех 3-х групп потребления электрической энергии.</li>" \
               "<li>Выбрать те домохозяйства, после 18-00 потребляют более 6 кВт в минуту в среднем," \
               "Выбрать те домохозяйства, после 18-00 потребляют более 6 кВт в минуту в среднем, " \
               "среди отобранных определить те, в которых основное потребление электроэнергии в указанный" \
               "Выбрать те домохозяйства, после 18-00 потребляют более 6 кВт в минуту в среднем, " \
               "среди отобранных определить те, в которых основное потребление электроэнергии в указанный " \
               "промежуток времени приходится на стиральную машину, сушилку, холодильник и освещения " \
               "(группа 2 является крупнейшей) , а затем выбрать каждый третий результат с первой половины " \
               "и каждый четвертый результат со второй половины.</li>" \
               "<li>Для каждой из структур данных нужно выполнить профилирование времени выполнения" \
               " (использовать <b>timeit</b> из одноименного модуля).</li>" \
               "<li>с использованием массивов <b>NumPy (numpy array) </b></li>" \
               "<li>и фреймов (<b>Python Pandas - DataFrame</b>)</li>" \
               "</ul>" \
               "<p>Выполнить все задания, используя   <b>numpy array</b>, так и <b>dataframe</b>, " \
               "проанализировать временные затраты на выполнение процедур (профилирования времени выполнения)," \
               " сделать выводы относительно ситуаций, в которых имеет смысл отдать предпочтение той или иной" \
               " структуре данных. Выводы оформить отчетом с указанным временем выполнения " \
               "и оценке по 5-балльной шкале удобства выполнения операций отбора)." \
               "</p>"


if __name__ == '__main__':
    app = SpyreSelectFile()

    # запуск приложения http://127.0.0.1:9091
    app.launch(port=9091)
