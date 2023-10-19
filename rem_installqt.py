import os
import sys
import glob
from remoteinst import *
import multiprocessing as ms

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import *

app = QtWidgets.QApplication(sys.argv)
RemoteInstall = QtWidgets.QMainWindow()
ui = Ui_RemoteInstall()
ui.setupUi(RemoteInstall)
RemoteInstall.show()


# Form, Window = uic.loadUiType()
#
# app = QApplication(sys.argv)
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
#
#wb_patch = QtWidgets.QFileDialog.getOpenFileName()
# print(wb_patch)

#Логин

def pstools():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    dialog.exec()
    global file_path_pstools
    file_path_pstools = dialog.selectedFiles()[0]
    ui.lineEdit_3.setText(file_path_pstools)
    print(file_path_pstools)



ui.pushButton_2.clicked.connect(pstools)


def pc_names():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.exec()
    global file_path_pc_names
    file_path_pc_names= dialog.selectedFiles()[0]
    ui.lineEdit_4.setText(file_path_pc_names)
    print(file_path_pc_names)


ui.pushButton_3.clicked.connect(pc_names)

def scrypt():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.exec()
    global file_scrypt
    file_scrypt = dialog.selectedFiles()[0]
    ui.lineEdit_5.setText(file_scrypt)
    print(file_scrypt)



ui.pushButton_4.clicked.connect(scrypt)

def install():
    login = ui.lineEdit.displayText() #Берем логин из окна
    passwd = ui.lineEdit_2.displayText() #Берем пароль из окна
    scrs = file_scrypt.replace('/', "\\")  # Заменяем слеши
    file = open(file_path_pc_names, 'r')# Открывам файл с именами
    while True:
        line = file.readline() #вычитываем строки
        print(line)
        if not line:
            break
        command3 = ("cd {} & PsExec \\\{} -u {} -p {} -s {}".format(file_path_pstools,line.strip() ,login, passwd, scrs))
        #command3 = ("cd {} & PsExec \\\{} -u {} -p {} -s {}".format(file_path_pstools, !!НАЗВАНИЕ ПК!!, login, passwd, file_scrypt))
        print(command3)
        os.system(command3)


    file.close

def inst():
    d =ms.Process(target = install)
    d.start()

#ui.pushButton.clicked.connect(inst)
ui.pushButton.clicked.connect(install) #функция установки





sys.exit(app.exec())

# login = ui.lineEdit.displayText()
# passwd = ui.lineEdit_2.displayText()
# pspath = ui.lineEdit_3.clicked.connect(dialog)
# file_path = dialog.selectedFiles()[0]
# print(file_path)
# pctxt = ui.lineEdit_4.displayText()
# sckript = ui.lineEdit_5.displayText()
# print(sckript)
# print(pctxt)
# print(pspath)
# print(passwd)
# print(login)
# print("hi")

# cd {1} & PsExec \\\{2} -u {3} -p {4} -s {5}
#
# 1 путь к расположению PsTools
# 2 строка из файла с название ПК (пк на который будем ставить)
# 3 Логин (адин домена)
# 4 Пароль пользователя
# 5 Скрипт установки (в нем прописана программа для установки в виде : msiexec.exe /i \\\it15\\tmp\\8.3.22.1709\\1CEnterprise 8.msi /passive /log \\\it15\\tmp\\msi_setup.log)