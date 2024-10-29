from speed_test import *
import sys
import speedtest
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *


print(1)
st = speedtest.Speedtest()

app = QtWidgets.QApplication(sys.argv)
SpeedTest = QtWidgets.QMainWindow()
ui = Ui_SpeedTest()
ui.setupUi(SpeedTest)
SpeedTest.show()


def speed():
    down_speed = st.download()
    down_speed_1 = down_speed / (2 ** 20)
    print(down_speed / (2 ** 20))
    # ui.lineEdit.append(down_speed_1)

    # up_speed = st.upload()
    # print(up_speed/ (2**20))


ui.pushButton.clicked.connect(speed)

sys.exit(app.exec())
