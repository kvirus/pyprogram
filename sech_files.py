import glob
import os
from tkinter import *
from tkinter import messagebox

def clicked():
    dir_input = txt.get()
    exe_input = txt_exe.get()
    path = txt_path.get()
    dir = dir_input + '\**\*.' + exe_input
    all = list(glob.glob(dir, recursive=True))
    file = open(path +".txt", 'w')
    for i in all:
        file.write(i + '\n')
    file.close()
    messagebox.showinfo("GUI Python", "Сохранено")

window = Tk()
window.title("Приложение для поиска файлов по расширению")
window.geometry('600x250')
lbl = Label(window, text="Введите каталог для поиска:")
lbl.grid(column=0, row=0)
txt = Entry(window, width=30)
txt.grid(column=1, row=0)
lbl = Label(window, text="Введите расширение файла:")
lbl.grid(column=0, row=2)
txt_exe = Entry(window, width=30)
txt_exe.grid(column=1, row=2)
lbl = Label(window, text="Название файла:")
lbl.grid(column=0, row=3)
txt_path = Entry(window, width=30)
txt_path.grid(column=1, row=3)
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
#dir_input = txt.get()
#print(dir_input)
#dir_input = input("Введите каталог для поиска: \n ",)
#if os.path.exists(dir_input):
#    print("Каталог существует")
#else:
#    print("Каталог не существует, введите верный каталог")
#    dir_input = input("Введите каталог для поиска: \n ", )
#exe_input = input("Введите расширение поиска: \n")
#output = input("Введите куда сохранять результаты поиска: \n")
#dir = dir_input + '\**\*.' + exe_input
#all = list(glob.glob(dir,recursive=True))
#path = output
#file = open(path, 'w')
#for i in all:
#    file.write(i + '\n')
#file.close()
#input("Нажмите ENTER",)