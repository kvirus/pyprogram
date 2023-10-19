import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import time


app = QApplication(sys.argv)
screen = app.primaryScreen()
width, height = screen.size().width(), screen.size().height()

image_path = "C:/cat.jpg"
pixmap = QPixmap(image_path)
scaled_pixmap = pixmap.scaled(width, height)

widget = QWidget()
widget.setWindowFlags(widget.windowFlags() | Qt.WindowStaysOnTopHint)
label = QLabel(widget)
label.setPixmap(scaled_pixmap)
widget.setGeometry(0, 0, width, height)
widget.showFullScreen()
sys.exit(app.exec_())

