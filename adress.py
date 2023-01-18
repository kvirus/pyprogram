from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter.messagebox as mb


def safe():
    print(name_enter.get(), '\t',fam_enter.get(), '\t',tel_enter.get())
    safe_file = open('H:\\1\\note.txt','a')
    name_safe = name_enter.get()
    fam_safe = fam_enter.get()
    tel_safe = tel_enter.get()
    safe_file.write('\n' + name_safe +'\t'+fam_safe +'\t' + tel_safe)
    safe_file.close()

def seach ():
    phone_sch1 = seach_enter.get()
    phone_sch = phone_sch1.title()
    seach_look.delete(1.0, END)
    print(phone_sch)
    #stroki = sum(1 for line in open('H:\\1\\note.txt', 'r'))
    #i=0
    #print(stroki-1)
    safe_file = open('H:\\1\\note.txt', 'r')
    while True:
        stroka = safe_file.readline()
        if not stroka:
            break
        if phone_sch in stroka:
            seach_look.insert(INSERT, '\n'+stroka)
            #mb.showinfo(title="Найдено",message=stroka)

        # if phone_sch in safe_file.readline():
        #     print(safe_file.readline(),end='')
    safe_file.close()

def dell():
    del_file = open('H:\\1\\note.txt', 'w')
    del_file.close()


window = Tk()
window.title("Адресная книга")
window.geometry('600x550')
#Ввод имени
lbl_seach = Label(window, text="Добавить телефон")
lbl_seach.grid(column=1, row=0, sticky= 'n')
name_lbl = Label(window, text="Введите Имя:")
name_lbl.grid(column=0, row=1, sticky = 'e')
name_enter = Entry(window, width=30)
name_enter.grid(column=1, row=1)
#Ввод фамилии
fam_lbl = Label(window, text="Введите фамилию:")
fam_lbl.grid(column=0, row=2, sticky = 'e')
fam_enter = Entry(window, width=30)
fam_enter.grid(column=1, row=2)
#Ввод Телефона
tel_lbl = Label(window, text="Введите телефон:")
tel_lbl.grid(column=0, row=3, sticky = 'e')
tel_enter = Entry(window, width=30)
tel_enter.grid(column=1, row=3)

#Поиск по файлу
seach_lbl = Label(window, text="Найти телефон:")
seach_lbl.grid(column=2, row=0)
seach_enter = Entry(window, width=30)
seach_enter.grid(column=2, row=1)
seach_btn = Button(window, text="Поиск по справочнику", command=seach)
seach_btn.grid(column=2, row=4)

#Вывод найденного телефона
seach_look = scrolledtext.ScrolledText(window, width=50, height=10)
seach_look.grid(column=0, row=5, columnspan=9)

#Кнопка записи в файл
safe_btn = Button(window, text="Сохранить в телефонный справочник", command=safe)
safe_btn.grid(column=1, row=4)

#Удалить справичник
del_all = Button(window, text="Удалить справочник", command=dell)
del_all.grid(column=1, row=8)
window.mainloop()