from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog as fd
#import gtts
#import pyttsx3
#from playsound import playsound

#engine = pyttsx3.init()
#text=''
#engine.say(text)
#engine.runAndWait()
#t1 = gtts.gTTS("Привет Дарья, как дела ?")
#t1.save("1.mp3")


def open_f():
    folder = open_docs.name
    print(folder)
    file = open(folder,'r')
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

def safe_txt():
    t0=textbox.get("1.0",END)
    t1 = gtts.gTTS(t0)
    dst = fd.asksaveasfile()
    print(dst.name)
    t1.save(dst.name)

def open_doc():
    global open_docs
    open_docs = fd.askopenfile()
    print(open_docs.name)

window = Tk()
window.title("Открытие текстового документа и поместить его в окно")
window.geometry('600x550')

open_lbl = Label(window, text="\u2600 Открыть документ")
open_lbl.grid(column=0, row=0)
open_btn_2 = Button(window, text='\u2601 Путь к файлу', command=open_doc)
open_btn_2.grid(column=1, row=0)
#open_in = Entry(window, width=30)
#open_in.grid(column=0, row=1)
open_btn = Button(window, text="\u2605 Перенести в окно", command=open_f)
open_btn.grid(column=2, row=0)
open_btn_2 = Button(window, text="открыть документ", command=open_file)
open_btn_2.grid(column=0, row=7)
open_btn_2 = Button(window, text="\u2623 Проиграть текст в окне", command=play)
open_btn_2.grid(column=3, row=0)
open_btn_2 = Button(window, text="\u2622 Сохранить текст как mp3", command=safe_txt)
open_btn_2.grid(column=1, row=7)

textbox = scrolledtext.ScrolledText(window, width=60, height=10)
textbox.grid(column=0, row=2, columnspan = 5)

window.mainloop()