import os
import sys
import glob

from tracker import *
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import *


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def onclick(): #Кнопка удаления. Подбор файлов и рекурсивное удаление их
    #print(ui.plainTextEdit.toPlainText())
    x = ui.plainTextEdit.toPlainText()
    y = x.split('\n')
    for name in y:
        print(name)
        txt = ui.pathEdit.displayText()  # отображение текста в строке
        dir = txt + '\**\*' + name + "*.bak"  # собираем название файла с путем
        print(dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        print("найденные:", all)
        for i in all:
            os.remove(i)

ui.pushButton.clicked.connect(onclick) #Вызов функции удаления

def path(): #Диалоговое окно вызова директории
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    dialog.exec()
    global file_path_pstools
    file_path_pstools = dialog.selectedFiles()[0]
    ui.pathEdit.setText(file_path_pstools)
    print(file_path_pstools)

ui.pushButton5.clicked.connect(path)

def podbor(): # функция подбора файлов и вывода их в окно
    x = ui.plainTextEdit.toPlainText() #Получение текста из окна 1
    y = x.split('\n')
    for name in y:
        print(name)
        txt1 = ui.pathEdit.displayText()  # отображение текста в строке
        txt = txt1.replace('/', "\\")
        dir = txt + "\**\*" + name + "*.bak"  # собираем название файла с путем
        print(dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        print(all)
        for x in all:
            ui.plainTextEdit_2.appendPlainText(x) #помещение текста в окно 2

ui.pushButton_2.clicked.connect(podbor)

def onclick_cal():
    print(ui.calendarWidget.selectedDate().toString('yyyy_MM_dd'))
    ui.plainTextEdit.appendPlainText(ui.calendarWidget.selectedDate().toString('yyyy_MM_dd'))

ui.calendarWidget.clicked.connect(onclick_cal)


sys.exit(app.exec())
