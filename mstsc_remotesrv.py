
import os
from tkinter import *
from tkinter import messagebox

# cmdkey /generic:"TERMSRV" /user:"sysadmin" /pass:"dontshowit"
# mstsc /v:"TERMSRV
# reboot = "shutdown /m \\\\" + name + " /r" + " /f" + " /t " + time
# os.system(reboot)

def mstsc():
    srv_def = server_win.get()
    pass_def = pass_win.get()
    login_def = login_win.get()
    pass_save = "cmdkey /generic:"+ srv_def + " /user:" + login_def + " /pass:" + pass_def
    os.system(pass_save)
    #print(pass_save)
    conect = "mstsc /v:" + srv_def
    os.system(conect)
    print(conect)
    return False
    #del_pass = "cmdkey / delete:" + srv_def
    #os.system(del_pass)
    #print(pass_save)



window = Tk()
window.title("Удаленные рабочие столы")
window.geometry('600x300')
label = Label(window, text="Введите учетные данные для подключения к удаленному рабочему столу")
label.grid(column=0, row=0, columnspan=3)
login = Label(window, text="Введите логин:")
login.grid(column=0, row=2)
login_win = Entry(window, width=30)
login_win.grid(column=1, row=2)
passwd = Label(window, text="Введите пароль:")
passwd.grid(column=0, row=3)
pass_win = Entry(window, width=30, show="*")
pass_win.grid(column=1, row=3)
server = Label(window, text="Введите сервер подключения:")
server.grid(column=0, row=4)
server_win = Entry(window, width=30)
server_win.grid(column=1, row=4)
mstsc = Button(window, text="Подключиться", command=mstsc)
mstsc.grid(column=3, row=2)

window.mainloop()