import os
import sys
from tkinter import *
from tkinter import messagebox as mb
from tkinter import scrolledtext
from tkinter import filedialog



def install():
    isDirectory = os.path.isfile(filepath_sc)
    if isDirectory==False:
        mb.showinfo("Информация","Не файла со скриптом")
        return
    isFile = os.path.isfile(filepath)
    if isDirectory==False:
        mb.showinfo("Информация","Не введен путь к скрипту")
        return
    if len(login.get())==0:
        mb.showinfo("Информация", "Не введен Логин")
        return
    if len(passwd.get())==0:
        mb.showinfo("Информация", "Не введен Пароль")
        return
    print(isDirectory)
    name = open(filepath, 'r')
    print(name)
    #print(name)
    passwdd = passwd.get()
    login_l = login.get()
    filepath_scp = filepath_sc
    while True:
        line = name.readline()
        if not line:
            break
        command3 = ("cd c:\PSTools & PsExec \\\{} -u {} -p {} -s {}".format(line.strip(),login_l, passwdd,filepath_scp))
        print(command3)
        #os.system(command3)
    name.close

def open_f():
    global filepath
    filepath = filedialog.askopenfilename()

def open_scr():
    global filepath_sc
    filepath_sc = filedialog.askopenfilename()
    print(filepath_sc)

def open_pst(): #Дописать путь к PSTools
    False


window = Tk()
window.title("Разливание платформы 1С")
window.geometry('600x550')
global filepath
filepath=0
global filepath_sc
filepath_sc=0

lbl_prog = Label(window, text="\u2600 Программа устанавливает платформу прописанную в \\\it15\\tmp\install.cmd")
lbl_prog.grid(column=0, row=0, columnspan=2)
# lbl_prog1 = Label(window, text="\u2600 Название ПК берется из C:\Intel\\name.txt")
# lbl_prog1.grid(column=0, row=1)
file_name = Button(window, text='\u2601 Путь к файлу с именами ПК', command=open_f)
file_name.grid(column=1, row=6)
login_lbl = Label(window, text="Логин")
login_lbl.grid(column=0, row=3, sticky = 'w')
login = Entry(window, width=30)
login.grid(column=1, row=3)
pass_lbl = Label(window, text="Пароль")
pass_lbl.grid(column=0, row=4,sticky = 'w')
passwd = Entry(window, width=30,show="\u2623")
passwd.grid(column=1, row=4)
pstool_lbl = Label(window, text="Расположение PSTOOLS")
pstool_lbl.grid(column=0, row=5,sticky = 'w')

pstool_map = Button(window, text='\u2601 Путь к PSTOOLS', command=open_pst)
pstool_map.grid(column=1, row=5)

script_lbl = Label(window, text="Путь к скрипту\n (должен лежать в общей папке, в сети)")
script_lbl.grid(column=0, row=7, sticky = 'w')
script_name = Button(window, text='\u2601 Путь к скрипту', command=open_scr)
script_name.grid(column=1, row=7)
start_btn = Button(window, text="\u2623 Запуск установки", command=install)
start_btn.grid(column=0, row=9, columnspan=3)
sk_opis = Label(window, text="Скрипт одолжен иметь вид:\n msiexec.exe /i \\\it15\\tmp\\8.3.22.1709\\1CEnterprise 8.msi /passive /log \\\it15\\tmp\\msi_setup.log")
sk_opis.grid(column=0, row=8, columnspan=3)

window.mainloop()



# for nam in line:
#     print(nam)
    #command3 = ("cd c:\PSTools & PsExec \\\{} -u pp.local\\bka -p J -s \\\it15\\tmp\install.cmd".format(nam))
    #print(command3)
#print(command3)
#res = os.system(command3)
#print("Returned Value: ", res)
