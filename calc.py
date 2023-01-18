#Калькулятор

from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

def one():
    global a
    a = 1
    output.insert(INSERT, a)

def two():
    global b
    b = 2
def tree():
    global c
    c = 3

def outx():
    x=x
    output.insert(INSERT, x)



def out():
    output.insert(INSERT, a)
    output.insert(INSERT, "\n")


window = Tk()
a=1
b=1
c=1
window.title("Калькулятор")
window.geometry('300x400')
#Окно вывода
output = scrolledtext.ScrolledText(window, width=33, height=3)
output.grid(column=0, row=0, columnspan =4)

#Кнопки
btn_1 = Button(window, text="1", height=2,width =8, command=one)
btn_1.grid(column=0, row=1, sticky=W)
btn_2 = Button(window, text="2", height=2,width =8,command=two)
btn_2.grid(column=1, row=1)
btn_3 = Button(window, text="3",height=2, width =8, command=tree)
btn_3.grid(column=3, row=1, sticky=E)
btn_x_x = Button(window, text="x", height=2,width =8, command=outx)
btn_x_x.grid(column=0, row=2, sticky=W)

#Вывод что сейчас есть

btn_x = Button(window, text="xx", height=2,width =8, command=out)
btn_x.grid(column=0, row=3, sticky=W)

window.mainloop()