import os
import sys
import glob

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication(sys.argv)
window = Window()
form = Form()
form.setupUi(window)
window.show()

def onclick():
    print(form.plainTextEdit.toPlainText())
    #print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))

    print("Нажато")
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    #date = QDate(2022, 9, 7)
    #form.calendarWidget.setSelectedDate(QDate(2022, 9, 7))
    x = form.plainTextEdit.toPlainText()
    y = x.split('\n')
    # print(x.split('\n'))
    for name in y:
        print(name)
        txt = form.pathEdit.displayText()  # отображение текста в строке
        dir = txt + '\**\*' + name + "*.bac"  # собираем название файла с путем
        print(dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        print("найденные:", all)
        #form.plainTextEdit_2.appendPlainText(all)
        for i in all:
            os.remove(i)
    #print(x)
    # r=[]
    # r.append(x)
    # print(r)
    #dir = dir_input + '\**\*' + name + "*.*" #собираем название файла с путем




form.pushButton.clicked.connect(onclick)

def podbor():
    #print(form.plainTextEdit.toPlainText())
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))

    #print("Нажато")
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2022, 9, 7)
    # form.calendarWidget.setSelectedDate(QDate(2022, 9, 7))
    x = form.plainTextEdit.toPlainText()
    y = x.split('\n')
    # print(x.split('\n'))
    for name in y:
        print(name)
        txt = form.pathEdit.displayText()  # отображение текста в строке
        dir = txt + '\**\*' + name + "*.*"  # собираем название файла с путем
        print(dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        print("найденные:", all)
        for x in all:
            form.plainTextEdit_2.appendPlainText(x)

form.pushButton_2.clicked.connect(podbor)

def onclick_cal():
    print(form.calendarWidget.selectedDate().toString('yyyy_MM_dd'))
    #form.dateEdit.setDate(form.calendarWidget.selectedDate())
    #form.calendarWidget.selectedDate()
    form.plainTextEdit.appendPlainText(form.calendarWidget.selectedDate().toString('yyyy_MM_dd'))

form.calendarWidget.clicked.connect(onclick_cal)
# def edittxt():
#     print("edittext")

#form.plainTextEdit.textChanged.connect(edittxt)

sys.exit(app.exec())
