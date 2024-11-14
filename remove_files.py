import glob
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk


def clicked():
    dir_input = txt.get()  #Каталог удаления
    if os.path.isdir(txt.get()):
        print( )
    else:
        messagebox.showinfo("GUI Python", "Нет такого каталога")
    if len(txt.get()) == 0:
        messagebox.showinfo("GUI Python", "Не введен каталог поиска")
    #exe_input=txt_exe.get()
    exe_input =list(map(str,txt_exe.get().split(" "))) #получение название файла для удаления
    if len(txt_exe.get()) == 0:
        messagebox.showinfo("GUI Python", "Не введены файлы поиска")
    print(exe_input)
    #path = txt_path.get()
    file = open("c:/intel/1.txt", 'w')  # открываем файл
    for name in exe_input:
        dir = dir_input + '\**\*' + name + "*.*" #собираем название файла с путем
        print(dir)
        all = list(glob.glob(dir, recursive=True)) #рекурсивный поиск
        print(all)
        if len(all) == 0:
            messagebox.showinfo("GUI Python", "Ничего не найдено")
        print(all)
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
    # exe_input=txt_exe.get()
    exe_input = list(map(str, txt_exe.get().split(" ")))  # получение название файла для удаления
    print(exe_input)
    #path = txt_path.get()
    #file = open("c:/intel/1.txt", 'w')  # открываем файл
    for name in exe_input:
        dir = dir_input + '\**\*' + name + "*.*"  # собираем название файла с путем
        all = list(glob.glob(dir, recursive=True))  # рекурсивный поиск
        for i in all:
            os.remove(i)
    messagebox.showinfo("GUI Python", "Файлы удалены")


def clicked_clear():
    txt1.delete("1.0", "end")

window = Tk()
window.title("Удаление файлов из каталога")
window.geometry('600x450')
lbl1 = Label(window, text="Введите каталог файла:")
lbl1.grid(column=0, row=0)
txt = Entry(window, width=30)
txt.grid(column=1, row=0)
lbl2 = Label(window, text="Введите расширение файла:")
lbl2.grid(column=0, row=1)
txt_exe = Entry(window, width=30)
txt_exe.grid(column=1, row=1)
lbl3 = Label(window, text="Удаленныые файлы:")
lbl3.grid(column=1, row=3)
txt1 = scrolledtext.ScrolledText(window, width=70, height=20) # Окно с удаление
txt1.grid(row=6,column=0,columnspan=3)
btn = Button(window, text="OK", command=clicked)
btn.grid(column=2, row=0)
btn_del = Button(window, text="Удалить", command=clicked_del)
btn_del.grid(column=2, row=1)
btn_clear = Button(window, text="Очистить вывод", command=clicked_clear) # Очистка окна вывода
btn_clear.grid(column=2, row=2)

frame = tkinter.Frame(window)
frame.grid()
canvas = tkinter.Canvas(window, height=300, width=300)
#image = Image.open("d:/logo.jpg")
#img = image.resize((300, 300), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(img)
#img = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.grid(row=10,column=1)
window.mainloop()