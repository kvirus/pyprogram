
from tkinter import *
from tkinter import messagebox
from PIL import Image

sample = Image.open('d:/1.png')
print(type(sample))
print(sample.size)
sample.show()


#Написать программу открытия каталога выбора файла и кнопки для его открытия, потом ковертации и сохранения в другое место