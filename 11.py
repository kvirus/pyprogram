from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog as fd
import gtts
import pyttsx3
from playsound import playsound

#engine = pyttsx3.init()
#text=''
#engine.say(text)
#engine.runAndWait()
#t1 = gtts.gTTS("Привет Дарья, как дела ?")
#t1.save("1.mp3")


def open_f():
    folder = open_in.get()
    print(folder)
    file = open(filename,'r')
    file_line=file.readlines()
    t1 = gtts.gTTS("Welcome to javaTpoint")
    for i in file_line:
        textbox.insert(END, i+'\n')

    print(file_line)
    file.close()

def open_file():

    global filename
    filename = fd.askopenfilename(title='Open a file', initialdir='c:/')
    print(filename)

def play():
    engine = pyttsx3.init()
    text_g=textbox.get("1.0",END)
    text=text_g
    engine.say(text)
    engine.runAndWait()


window = Tk()
window.title("Открытие текстового документа и поместить его в окно")
window.geometry('600x550')

open_lbl = Label(window, text="Открыть документ")
open_lbl.grid(column=0, row=0)
open_in = Entry(window, width=30)
open_in.grid(column=0, row=1)
open_btn = Button(window, text="Перенести в окно", command=open_f)
open_btn.grid(column=0, row=8)
open_btn_2 = Button(window, text="открыть документ", command=open_file)
open_btn_2.grid(column=0, row=7)
open_btn_2 = Button(window, text="Проиграть текст", command=play)
open_btn_2.grid(column=0, row=9)

textbox = scrolledtext.ScrolledText(window, width=50, height=10)
textbox.grid(column=0, row=2, columnspan = 2)

window.mainloop()