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
        error_str = str(ex)

def reboot():
    ips= [
        '192.168.0.99','192.168.0.134','192.168.3.21','192.168.3.37','192.168.3.64','192.168.3.127',
        '192.168.3.129','192.168.51.30','192.168.51.31','192.168.51.40','192.168.51.42','192.168.51.43','192.168.51.44',
        '192.168.51.45','192.168.51.46','192.168.51.48','192.168.51.50','192.168.51.51','192.168.51.60',
        '192.168.51.66','192.168.51.67','192.168.51.68','192.168.51.69','192.168.51.70','192.168.51.71',
        '192.168.51.73','192.168.51.74','192.168.51.75','192.168.51.80','192.168.51.90','192.168.51.91',
        '192.168.51.92','192.168.51.93','192.168.51.94','192.168.51.161','192.168.51.162','192.168.51.166',
        '192.168.51.167','192.168.51.168','192.168.51.169','192.168.51.170','192.168.51.171','192.168.51.172'
    ]
    for ip in ips:
        comands(ip, 'reboot')
    print('done')

reboot()



