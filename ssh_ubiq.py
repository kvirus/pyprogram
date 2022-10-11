import paramiko
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def comands(ip,cmd):
    print(cmd)
    try:
        client.connect(hostname=ip, username="admin", password="CeBVCfE9Aygi1qD2", look_for_keys=False, allow_agent=False)
        #comand = input("Введите команду: ", )
        _stdin, _stdout, _stderr = client.exec_command(cmd)
        print(_stdout.read().decode())
        client.close()
    except Exception as ex:
        error_str=str(ex)
        if "getaddrinfo" in error_str:
            print('Не верный адрес')
            txt_err.insert(INSERT, 'Не верный адрес')
        elif "Authentication" in error_str:
            print('Логин или пароль')
            txt_err.insert(INSERT, 'Не верный логин или пароль')
        elif '10060' in error_str:
            print('Нет ответа от сервера')
            txt_err.insert(INSERT, 'Нет ответа от сервера')
        else:
            print("Другая ошибка, код ошибки:")
            txt_err.insert(INSERT,ex)
            print(ex)
def reboot():
    ip_ub=txt_ip.get()
    print(ip_ub)
    comands(ip_ub, 'reboot')

def adopt():
    ip_ub=txt_ip.get()
    print(ip_ub)
    comands(ip_ub, 'set-inform http://192.168.0.245:8080/inform')
def restore():
    ip_ub=txt_ip.get()
    print(ip_ub)
    comands(ip_ub, 'syswrapper.sh restore-default')

window = Tk()
window.title("Перезагрузка точки Unifi")
window.geometry('500x250')
lbl_ip = Label(window, text="Введите адрес точки")
lbl_ip.grid(column=0, row=0)
txt_ip = Entry(window, width=30)
txt_ip.grid(column=1, row=0)
btn_reboot = Button(window, text="Перезагрузка", command=reboot)
btn_reboot.grid(column=0, row=5)
btn_adopt = Button(window, text="Адаптация", command=adopt)
btn_adopt.grid(column=1, row=5)
btn_restore = Button(window, text="Сбросить точку доступа", command=restore)
btn_restore.grid(column=2, row=5)
lbl_err = Label(window, text="Ошибки:")
lbl_err.grid(column=0, row=6)
txt_err = scrolledtext.ScrolledText(window, width=50, height=10) # Окно с удаление
txt_err.grid(row=7,column=0,columnspan=5)
window.mainloop()




