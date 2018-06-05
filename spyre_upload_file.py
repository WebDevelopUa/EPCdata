# coding=utf-8
# Spyre Скрипт, загружающий .csv файл для отображения в табличном виде и гистограмме в веб-браузере
# Spyre - Web Application framework for Python - фреймворк веб-приложений (Python)

# Требования для запуска приложения:
# Python, cherrypy, jinja2, pandas, matplotlib
# pip install dataspyre

# http://127.0.0.1:9090

import pandas as pd
from spyre import server

server.include_df_index = True


class SpyreUploadFile(server.App):
    # заголовок
    title = "Spyre Upload .txt file with EPC Data"

    # кнопки (для загрузки файла, загрузки данных)
    controls = [
        {
            "type": "upload",
            "id": "ubutton"
        },
        {
            "type": "button",
            "id": "update_data",
            "label": "Get Data (Press n-times)"
        }

    ]

    inputs = [{
        "type": 'text',
        "label": 'Information!',
        "value": 'Check rows quantity with origin',
        "key": 'title',
        "action_id": "refresh",

    }]

    # вкладки (для таблицы, графика, инфо)
    tabs = ["Table", "Plot", "Info"]

    # выходные данные (для таблицы, графика, инфо)
    outputs = [
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": False
        },
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot",
            "on_page_load": False
        },
        {
            "type": "html",
            "id": "custom_html",
            "tab": "Info"
        }

    ]

    # метод __init__() – конструктор объектов класса
    # self – ссылка на сам только что созданный объект
    # def - инструкция, с помощью которой определяется функция
    # функция в python - объект, принимающий аргументы и возвращающий значение
    # return - инструкция указывающая на то, что нужно вернуть значение
    def __init__(self):
        self.upload_data = None
        self.upload_file = None

    # функция загружает файл .csv, метод read() читает весь файл целиком
    def storeUpload(self, file):
        self.upload_file = file
        self.upload_data = file.read()

    # функция загружает данные из файла .csv в DataFrame
    def getData(self, params):
        df = None
        if self.upload_file is not None:
            self.upload_file.seek(0)

            # https://docs.python.org/2/library/csv.html
            df = pd.read_csv(self.upload_file,
                             # delimiter=';',
                             # delimiter=',',
                             # delimiter='; |, |\*|\n',
                             delimiter=';|,',
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
        plot_obj.set_ylabel("y")
        plot_obj.set_xlabel("x")
        plot_obj.set_title("Display of Data for the selected period")
        # plot_obj.grid()
        line_plot = plot_obj.get_figure()
        return line_plot

    #  функция CSS стилизации страницы в веб-браузере (задается фон)
    def getCustomCSS(self):
        css = (
            "body {  "
            "width: 100wh;"
            "height: 90vh;"
            "color: #29298c;"
            "background: linear-gradient(-45deg, #23D5AB, #23A6D5, #ece71b, #36caa4);"
            "background-size: 400% 400%;"
            "-webkit-animation: Gradient 15s ease infinite;"
            "-moz-animation: Gradient 15s ease infinite;"
            "animation: Gradient 15s ease infinite;"
            "}"
            "@-webkit-keyframes Gradient {"
            "	0% {"
            "		background-position: 0% 50%"
            "	}"
            "	50% {"
            "		background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"
            "@-moz-keyframes Gradient {"
            "0% {"
            "background-position: 0% 50%"
            "}"
            "50% {"
            "background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"
            "@keyframes Gradient {"
            "0% {"
            "background-position: 0% 50%"
            "}"
            "	50% {"
            "background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"

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
    app = SpyreUploadFile()

    # запуск приложения http://127.0.0.1:9090
    app.launch(port=9090)
