# Form implementation generated from reading ui file 'passchng.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RemoteInstall(object):
    def setupUi(self, RemoteInstall):
        RemoteInstall.setObjectName("RemoteInstall")
        RemoteInstall.resize(954, 604)
        self.centralwidget = QtWidgets.QWidget(parent=RemoteInstall)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 110, 231, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 190, 471, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 240, 471, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 891, 91))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 290, 471, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 190, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 240, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 340, 471, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 60, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 390, 471, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 390, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 390, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        RemoteInstall.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RemoteInstall)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 21))
        self.menubar.setObjectName("menubar")
        RemoteInstall.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RemoteInstall)
        self.statusbar.setObjectName("statusbar")
        RemoteInstall.setStatusBar(self.statusbar)

        self.retranslateUi(RemoteInstall)
        QtCore.QMetaObject.connectSlotsByName(RemoteInstall)

    def retranslateUi(self, RemoteInstall):
        _translate = QtCore.QCoreApplication.translate
        RemoteInstall.setWindowTitle(_translate("RemoteInstall", "MainWindow"))
        self.label.setText(_translate("RemoteInstall", "Удаленное изменение паролей"))
        self.label_2.setText(_translate("RemoteInstall", "Login"))
        self.label_3.setText(_translate("RemoteInstall", "Password"))
        self.label_4.setText(_translate("RemoteInstall", "Путь к PsTools"))
        self.label_5.setText(_translate("RemoteInstall", "Путь к файлу с именами ПК"))
        self.pushButton.setText(_translate("RemoteInstall", "ЗАПУСК СМЕНЫ ПАРОЛЯ"))
        self.label_9.setText(_translate("RemoteInstall", "Введите пользователя"))
        self.pushButton_2.setText(_translate("RemoteInstall", "выбрать"))
        self.pushButton_3.setText(_translate("RemoteInstall", "выбрать"))
        self.label_10.setText(_translate("RemoteInstall", "Введите пароль"))
        self.label_11.setText(_translate("RemoteInstall", "Доменный администратор"))
        self.label_12.setText(_translate("RemoteInstall", "Путь сохранения ошибок"))
        self.pushButton_4.setText(_translate("RemoteInstall", "выбрать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoteInstall = QtWidgets.QMainWindow()
    ui = Ui_RemoteInstall()
    ui.setupUi(RemoteInstall)
    RemoteInstall.show()
    sys.exit(app.exec())