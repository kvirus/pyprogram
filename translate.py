from googletrans import Translator
import os
import sys
from gtts import gTTS
from playsound import playsound


from translat import *
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.checkBox.setChecked(True)

#Выбираем только 1 горящий чекбокс
def chck1():
    ui.checkBox.setChecked(False)
ui.checkBox_2.clicked.connect(chck1) #вызов функции чтобы первый чек отжался

def chck2():
    ui.checkBox_2.setChecked(False)
ui.checkBox.clicked.connect(chck2)



def txt_tr(text='Hello', src='ru',dest='en'):
    try:
        translator = Translator()
        translation = translator.translate(text=text,src=src,dest=dest)
        return translation.text
    except Exception as ex:
        return ex

# a11 = ui.textEdit.toPlainText()
# print(a11)

def onclick(): #Получаем такст из первого окна и помещаем во второй
    ui.textEdit_2.clear()
    # text_val = ui.textEdit.toPlainText()
    # language = 'en'
    # obj = gTTS(text=text_val, lang=language, slow=False)
    # obj.save("C:\Intel\exam.mp3")
    # playsound ('C:/Intel/exam.mp3')
    if ui.checkBox.isChecked() is True:
        try:
            print(ui.textEdit.toPlainText()) #Вывод текста в окне 1
            lng_in = 'en'
            lng_out = 'ru'
            print(txt_tr(ui.textEdit.toPlainText(), lng_in, lng_out))
            x1 = txt_tr(text=ui.textEdit.toPlainText(),src='en',dest='ru')
            #print(x1)
            ui.textEdit_2.append(x1)
        except Exception as ex:
            es =str(ex)
            ui.textEdit_2.append(es)
            return ex
    if ui.checkBox_2.isChecked() is True:
        try:
            print(ui.textEdit.toPlainText()) #Вывод текста в окне 1
            lng_in = 'en'
            lng_out = 'ru'
            print(txt_tr(ui.textEdit.toPlainText(), lng_in, lng_out))
            x1 = txt_tr(text=ui.textEdit.toPlainText(),src='ru',dest='en')
            #print(x1)
            ui.textEdit_2.append(x1)
        except Exception as ex:
            print("22", ex)
            es =str(ex)
            ui.textEdit_2.append(es)
            return ex

ui.pushButton.clicked.connect(onclick)

#Озвучка текста со второго окна
def say():
    if ui.checkBox.isChecked() is True:
        try:
            text_val = ui.textEdit_2.toPlainText()
            print(text_val)
            language = 'ru'
            obj = gTTS(text=text_val, lang=language, slow=False)
            print(text_val)
            file_path = 'C:/Intel/exam.mp3'
            if os.path.exists(file_path):
                os.remove(file_path)
            obj.save("C:\Intel\exam.mp3")
            print(text_val)
            playsound('C:/Intel/exam.mp3')
        except Exception as ex:
            return ex
    if ui.checkBox_2.isChecked() is True:
        try:
            text_val = ui.textEdit_2.toPlainText()
            print(text_val)
            language = 'en'
            obj = gTTS(text=text_val, lang=language, slow=False)
            print(text_val)
            file_path = 'C:/Intel/exam.mp3'
            if os.path.exists(file_path):
                os.remove(file_path)
            obj.save("C:\Intel\exam.mp3")
            print(text_val)
            playsound('C:/Intel/exam.mp3')
        except Exception as ex:
            return ex
ui.pushButton_2.clicked.connect(say)

#print(txt_tr(text='Hello',src='ru',dest='en'))

# txt = 'Hello, how are you'
# lng_in = 'en'
# lng_out = 'ru'
# print(txt_tr(txt,lng_in,lng_out))

sys.exit(app.exec())