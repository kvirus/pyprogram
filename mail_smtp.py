##Обернуть в try с выдачей ошибки, разобраться с языком

import subprocess
from subprocess import PIPE, run
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

# site=input("Введите адрес для проверки")
# result = run(["ping", site], stdout=PIPE, stderr=PIPE, universal_newlines=True)
# #code = subprocess.call(["ping", site])
# #print(result.returncode, result.stdout, result.stderr)

def clicked():
    result = run(["ping", adress_enter.get()], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    output.insert(INSERT, result.stderr)
    output.insert(INSERT, result.stdout)
    output.insert(INSERT, result.returncode)

window = Tk()
window.title("Проверка пинга сайта")
window.geometry('700x750')
name_pr = Label(window, text="Проверка доступности ресурса", font=("Arial", 14))
name_pr.grid(column=0, row=1, sticky=N, columnspan=10)
adress = Label(window, text="Введите адрес для проверки:", font=("Arial", 10))
adress.grid(column=0, row=2)
adress_enter = Entry(window, width=30)
adress_enter.grid(column=1, row=2)
btn_out = Button(window, text="Проверка ресурса", command=clicked)
btn_out.grid(column=0, row=3)
output = scrolledtext.ScrolledText(window, width=100, height=20, font = ("Calibri", 8)) # Окно с удаление
output.grid(row=4,column=0,columnspan=4)

window.mainloop()