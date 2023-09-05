import os
import sys
import glob
from remoteinst import *

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


def pstools():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    dialog.exec()
    file_path = dialog.selectedFiles()[0]
    ui.lineEdit_3.setText(file_path)
    print(file_path)

ui.pushButton_2.clicked.connect(pstools)

def pc_names():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.exec()
    file_path = dialog.selectedFiles()[0]
    ui.lineEdit_4.setText(file_path)
    print(file_path)


ui.pushButton_3.clicked.connect(pc_names)

def scrypt():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.exec()
    file_path = dialog.selectedFiles()[0]
    ui.lineEdit_5.setText(file_path)
    print(file_path)



ui.pushButton_4.clicked.connect(scrypt)

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