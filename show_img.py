import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer
import configparser as cp
import schedule
import time

cfg = cp.ConfigParser()
cfg.read('cfg.ini')

image_path = cfg['Settings']['img']
#tim = cfg['Settings']['time']
tslp = int(cfg['Settings']['tslp'])
tslp_msec = tslp*1000

def open():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    width, height = screen.size().width(), screen.size().height()
    pixmap = QPixmap(image_path)
    scaled_pixmap = pixmap.scaled(width, height)
    # создаем окно
    widget = QWidget()
    widget.setWindowFlags(widget.windowFlags() | Qt.WindowStaysOnTopHint)
    label = QLabel(widget)
    label.setPixmap(scaled_pixmap)
    widget.setGeometry(0, 0, width, height)
    # отображаем окно в полноэкранном режиме
    widget.showFullScreen()
    timer = QTimer()
    timer.timeout.connect(widget.close)
    timer.start(tslp_msec) # запускаем таймер
    sys.exit(app.exec_())

open()

#schedule.every().hour.at(tim).do(open)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
