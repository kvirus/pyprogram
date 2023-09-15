from googletrans import Translator
import os
import sys
import glob

from translat import *
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def txt_tr(text='Hello', src='en',dest='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text=text,src=src,dest=dest)

        return translation.text
    except Exception as ex:
        return ex

# a11 = ui.textEdit.toPlainText()
# print(a11)

def onclick(): #Получаем такст из первого окна
    print(ui.textEdit.toPlainText()) #Вывод текста в окне 1
    lng_in = 'en'
    lng_out = 'ru'
    print(txt_tr(ui.textEdit.toPlainText(), lng_in, lng_out))
    x1 = txt_tr(text=ui.textEdit.toPlainText(),src='en',dest='ru')
    print(x1)
    ui.textEdit_2.append(x1)

ui.pushButton.clicked.connect(onclick)

print(txt_tr(text='Hello',src='en',dest='ru'))

# txt = 'Hello, how are you'
# lng_in = 'en'
# lng_out = 'ru'
# print(txt_tr(txt,lng_in,lng_out))

sys.exit(app.exec())