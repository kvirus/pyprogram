# Form implementation generated from reading ui file 'speed_test.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpeedTest(object):
    def setupUi(self, SpeedTest):
        SpeedTest.setObjectName("SpeedTest")
        SpeedTest.resize(494, 301)
        self.centralwidget = QtWidgets.QWidget(parent=SpeedTest)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 130, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        SpeedTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SpeedTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        SpeedTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SpeedTest)
        self.statusbar.setObjectName("statusbar")
        SpeedTest.setStatusBar(self.statusbar)

        self.retranslateUi(SpeedTest)
        QtCore.QMetaObject.connectSlotsByName(SpeedTest)

    def retranslateUi(self, SpeedTest):
        _translate = QtCore.QCoreApplication.translate
        SpeedTest.setWindowTitle(_translate("SpeedTest", "MainWindow"))
        self.label.setText(_translate("SpeedTest", "Измерение скорости интернет"))
        self.label_2.setText(_translate("SpeedTest", "Скорость скачки"))
        self.label_3.setText(_translate("SpeedTest", "Скорость загрузки"))
        self.pushButton.setText(_translate("SpeedTest", "Измерить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpeedTest = QtWidgets.QMainWindow()
    ui = Ui_SpeedTest()
    ui.setupUi(SpeedTest)
    SpeedTest.show()
    sys.exit(app.exec())