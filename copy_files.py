import glob
import os
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


def clicked():
    dir_input = txt.get() #Каталог удаления
    exe_input=txt_exe.get()
    #exe_input =list(map(str,txt_exe.get().split(" "))) #получение название файла для удаления
    path = txt_path.get()
    dir = dir_input + '\**\*' + exe_input + "*.*" #собираем название файла с путем
    all = list(glob.glob(dir, recursive=True)) #рекурсивный поиск
    print(all)
    file = open("c:/intel/1.txt", 'w') #открываем файл
    for i in all:
        file.write(i + '\n')        #запись в файл
    file.close()                    #закрываем файл
    file1 = open("c:/intel/1.txt", "r")
    line = file1.readlines()
    for lin in line:
        txt1.insert(INSERT, lin)
    #messagebox.showinfo("GUI Python", "Сохранено")
def clicked_del():
    dir_input = txt.get()  # Каталог удаления
    exe_input = txt_exe.get()  # получение навазнеи файла для удаления
    dir = dir_input + '\**\*' + exe_input + "*.*"  # собираем название файла с путем
    all = list(glob.glob(dir, recursive=True))
    for i in all:
        os.remove(i)
    messagebox.showinfo("GUI Python", "Файлы удалены")
window = Tk()
window.title("Удаление файлов из каталога")
window.geometry('800x550')
lbl1 = Label(window, text="Введите каталог файла:")
lbl1.grid(column=0, row=0)
txt = Entry(window, width=30)
txt.grid(column=1, row=0)
lbl2 = Label(window, text="Введите расширение файла:")
lbl2.grid(column=0, row=2)
txt_exe = Entry(window, width=30)
txt_exe.grid(column=1, row=2)
lbl3 = Label(window, text="Удаленныые файлы:")
lbl3.grid(column=0, row=3)
txt1 = scrolledtext.ScrolledText(window, width=50, height=20)
txt1.grid(column=1, row=6)
txt_path = Entry(window, width=30)
txt_path.grid(column=1, row=3)
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)
btn_del = Button(window, text="Удалить", command=clicked_del)
btn_del.grid(column=3, row=0)
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