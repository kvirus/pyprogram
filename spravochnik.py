import pyodbc
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

#подключение к БД и использование базы данных
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=Z', autocommit=True)
cursor = conn.cursor()
cursor.execute('USE test')
#cursor.execute('CREATE TABLE phones (id int IDENTITY, name varchar(20), last varchar (20), phone BIGINT)')

def del_table():
    cursor.execute('DROP TABLE phones')

def create_table():
    cursor.execute('CREATE TABLE phones (id int IDENTITY, name varchar(20), last varchar (20), phone BIGINT)')

def add_phone():
    a= name_in.get()
    b=sname_in.get()
    c=phone_in.get()
    print(a,b,c)
    cursor.execute("INSERT INTO phones VALUES (?,?,?)", a, b, c)

def search_f():
    x = search_in.get()
    cursor.execute('SELECT * FROM phones WHERE  (* = ?)', x)
    out = cursor.fetchone()
    print(out)
   #search_out.insert(INSERT, out)
    #d=0
    # for i in result:
    #     if d==0:
    #         False
    #     if d==1:
    #
    #         print("Имя",i)
    #     if d==2:
    #         print("Фамилия", i)
    #     if d==3:
    #         print("Телефон", i)
    #     d=d+1

#Вызываем окно
window = Tk()
window.title("Удаление файлов из каталога")
window.geometry('700x750')

#ФИО и телефон челока, которого нужно добавить
sname = Label(window, text="Фамилия:")
sname.grid(column=0, row=1)
sname_in = Entry(window, width=30)
sname_in.grid(column=1, row=1)
name = Label(window, text="Имя:")
name.grid(column=0, row=2)
name_in = Entry(window, width=30)
name_in.grid(column=1, row=2)
phone = Label(window, text="Телефон:")
phone.grid(column=0, row=3)
phone_in = Entry(window, width=30)
phone_in.grid(column=1, row=3)

#Поиск
search = Label(window, text="Найти:")
search.grid(column=0, row=4)
search_in = Entry(window, width=30)
search_in.grid(column=1, row=4)
search_btn = Button(window, text="Поиск", command=search_f)
search_btn.grid(column=2, row=4)

#Вывод поиска
search_out = scrolledtext.ScrolledText(window, width=100, height=20, font = ("Calibri", 8))
search_out.grid(row=5,column=0,columnspan=7)


#Кнопки удаления/создания таблицы, добавления нового человека
btn_del = Button(window, text="Удалить таблицу", command=del_table) #Кнопка удаления таблицы
btn_del.grid(column=0, row=0)
crt_tbl = Button(window, text="Создать таблицу", command=create_table)
crt_tbl.grid(column=1, row=0)
add_man = Button(window, text="Добавить номер", command=add_phone)
add_man.grid(column=2, row=0)


window.mainloop()