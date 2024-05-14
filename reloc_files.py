import os
import sys
import glob
import threading

import shutil
from tracker_reloc import *
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from tkinter import messagebox

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# def loging():
#     ui.plainTextEdit_3.appendPlainText(end_file)  # Логирование



def onclick(): #Кнопка удаления. Подбор файлов и рекурсивное удаление их
    #print(ui.plainTextEdit.toPlainText())
    x = ui.plainTextEdit.toPlainText()
    y = x.split('\n')
    z = ui.pathEdit_2.displayText()
    for name in y:
        #print(name)
        txt = ui.pathEdit.displayText()  # отображение текста в строке
        dir = txt + '\**\*' + name + "*.bak"  # собираем название файла с путем
        #print(dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        #print(all)
        #тут нужно получить путь куда переносить
        for i in all:
            only_folder = os.path.dirname(i)  # забираем директорию без названия файла
            only_last_folder = os.path.basename(only_folder)  # забираем директорию
            #print('только каталог последний:', only_last_folder)
            z1 = z + '\\' + only_last_folder  # Собираем каталог для проверки существования
            #print("путь куда", z1)
            #print(i)
            file_name = os.path.basename(i)
            #print("Имя файла", file_name)
            end_file = z1 + '\\' + file_name
            #print('элемент', i)
            print('Сейчас копируется:',end_file)
            ui.plainTextEdit_3.appendPlainText(end_file) #Логирование
            try:
                #os.rename(i, end_file)
                shutil.move(i, end_file)
            except Exception as exc:
                print(exc)

    messagebox.showinfo("GUI Python", "Файлы перенесены")

#ui.pushButton.clicked.connect(onclick) #Вызов функции удаления
background_thread = threading.Thread(target=onclick)
ui.pushButton.clicked.connect(background_thread.start)


def path(): #Диалоговое окно вызова директории
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    dialog.exec()
    global file_path_pstools
    file_path_pstools = dialog.selectedFiles()[0]
    ui.pathEdit.setText(file_path_pstools)
    #print(file_path_pstools)
    # #Тест выбор только папки
    # last_folder= os.path.basename(file_path_pstools) #забираем название папки для создание ее на хранилке
    # print(last_folder)
    # #Проверка на существования в другом месте
    # new_place = 'c:\intel\\' + last_folder
    # print(new_place)
    # if not os.path.exists(new_place):
    #     os.makedirs(new_place)
    # else:
    #     print("Каталог", last_folder, "уже существует")

ui.pushButton_3.clicked.connect(path)


def path_rem(): #Диалоговое окно вызова директории
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    dialog.exec()
    global file_path_pstools
    file_path_pstools = dialog.selectedFiles()[0]
    ui.pathEdit_2.setText(file_path_pstools)
    #print(file_path_pstools)
    # #Тест выбор только папки
    # last_folder= os.path.basename(file_path_pstools) #забираем название папки для создание ее на хранилке
    # print(last_folder)
    # #Проверка на существования в другом месте
    # new_place = 'c:\intel\\' + last_folder
    # print(new_place)
    # if not os.path.exists(new_place):
    #     os.makedirs(new_place)
    # else:
    #     print("Каталог", last_folder, "уже существует")

ui.pushButton_4.clicked.connect(path_rem)


def podbor(): # функция подбора файлов и вывода их в окно
    x = ui.plainTextEdit.toPlainText() #Получение текста из окна 1
    y = x.split('\n')
    z = ui.pathEdit_2.displayText() #Вычитываем путь
    print('вывод из строки', z)
    for name in y:
        #print(name)
        txt1 = ui.pathEdit.displayText()  # отображение текста в строке
        txt = txt1.replace('/', "\\")
        dir = txt1 + "\**\*" + name + "*.bak"  # собираем название файла с путем
        #print('Каталог', dir)
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        #print('Все', all)
        #print('txt_all', all[0])
        for i in all:
            only_folder= os.path.dirname(i) #забираем директорию без названия файла
            only_last_folder = os.path.basename(only_folder) #забираем директорию
            #print('только каталог последний:', only_last_folder)
            z1 = z + '/'+ only_last_folder #Собираем каталог для проверки существования
            #print('каталог для проверки', z1)
            if not os.path.exists(z1):
                os.makedirs(z1)
            else:
                print("Каталог", z1, "уже существует")

        for x in all:
            ui.plainTextEdit_2.appendPlainText(x) #помещение текста в окно 2

ui.pushButton_2.clicked.connect(podbor)

def onclick_cal():
    print(ui.calendarWidget.selectedDate().toString('yyyy_MM_dd'))
    ui.plainTextEdit.appendPlainText(ui.calendarWidget.selectedDate().toString('yyyy_MM_dd'))

ui.calendarWidget.clicked.connect(onclick_cal)



sys.exit(app.exec())
