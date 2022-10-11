import netmiko
import paramiko
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from netmiko import ConnectHandler

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def del_ban(ip):
    client.connect(hostname='192.168.1.34', port=2231, username="bka", password="Jackal.85mm!", look_for_keys=False,
                   allow_agent=False)
    _stdin, _stdout, _stderr = client.exec_command('ip firewall address-list print where list="Blocked bruteforcers"')
    x = _stdout.read().decode()
    file = open('c:\\intel\\1.txt', 'w')
    file.write(x)
    file.close()
    file1 = open('c:\\intel\\1.txt', 'r')
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        if ip in line:
            print(line.strip())
            txt_ipadd.insert(INSERT,line.strip())
            #_stdin, _stdout, _stderr = client.exec_command('ip firewall address-list remove [find address='+ ip +']')
            #print('ip firewall address-list remove [find address='+ ip +']')
    file1.close()
    client.close()

def remove_def(ip):
    try:
        client.connect(hostname='192.168.1.34', port=2231, username="bka", password="Jackal.85mm!", look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command(
            'ip firewall address-list print where list="Blocked bruteforcers"')
        x = _stdout.read().decode()
        file = open('c:\\intel\\1.txt', 'w')
        file.write(x)
        file.close()
        file1 = open('c:\\intel\\1.txt', 'r')
        while True:
            # считываем строку
            line = file1.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            if ip in line:
                print(line.strip())
                txt_ipadd.insert(INSERT, line.strip())
                _stdin, _stdout, _stderr = client.exec_command('ip firewall address-list remove [find address='+ ip +']')
                # print('ip firewall address-list remove [find address='+ ip +']')
        file1.close()
        client.close()
    except Exception as ex:
        print(ex)

def remove():
    try:
        ip = txt_ip.get()
        remove_def(ip)
    except Exception as ex:
        print(ex)
def seach():
    txt_ipadd.delete(1.0, END)
    try:
        ip = txt_ip.get()
        del_ban(ip)
    except Exception as ex:
        print(ex)
#try:
    #del_ban()
#except Exception as ex:
    #print(ex)

window = Tk()
window.title("Поиск блокировки в бан листе Микротика")
window.geometry('500x250')
lbl_ip = Label(window, text="Введите адрес")
lbl_ip.grid(column=0, row=0)
txt_ip = Entry(window, width=30)
txt_ip.grid(column=1, row=0)
btn_seach = Button(window, text="Поиск", command=seach)
btn_seach.grid(column=4, row=0)
txt_ipadd = scrolledtext.ScrolledText(window, width=70, height=10, font = ("Arial",10)) # Окно с удаление
txt_ipadd.grid(row=7,column=0,columnspan=5)
btn_remove = Button(window, text="Удалить", command=remove)
btn_remove.grid(column=0, row=10)


window.mainloop()

