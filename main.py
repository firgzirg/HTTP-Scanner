from PyQt5 import QtCore, QtGui, QtWidgets
from main-ui import *
import sys
import requests
import time as t

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
# classes
class mainData:
    textData = ui.textEdit_2.toPlainText()

def connection():
    get = ui.textEdit.toPlainText() # получение текста
    if get == '':  # если гет == 0 тогда :
        get = 'http://google.ru'
    url = get # стандартный запрос
    try:
        page = requests.get(url)
        if page.status_code == 200:
            a = ' -  Страница найдена.'
        elif page.status_code == 404:
            a = ' - Страница не найдена.'
        elif page.status_code == 403:
            a = ' - Доступ к странице запрещен.'
        elif page.status_code == 301:
            a = ' - Действует постоянный редирект.'
        elif page.status_code == 302:
            a = ' - Действует временный редирект.'
        ui.textEdit_2.setText('STATUS: ' + str(page.status_code) + a)
    except requests.exceptions.MissingSchema:
        ui.textEdit_2.setText('Введите ссылку с протоколом! (http://, https://)')
    except requests.exceptions.ConnectionError:
        ui.textEdit_2.setText('Ошибка подключения! (хост не отвечает, или не существует.)')

class mainFunctions:
    def Scan():
        ui.textEdit_2.setText(mainData.textData1)

    def Clear():
        ui.textEdit_2.setText('')
# funcs

ui.pushButton.clicked.connect(connection)
ui.pushButton_5.clicked.connect(mainFunctions.Clear)
# liberda
sys.exit(app.exec_())
