##Обернуть в try с выдачей ошибки, разобраться с языком
import subprocess
from subprocess import PIPE, run
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import requests
import python_weather

# site=input("Введите адрес для проверки")
# result = run(["ping", site], stdout=PIPE, stderr=PIPE, universal_newlines=True)
# #code = subprocess.call(["ping", site])
# #print(result.returncode, result.stdout, result.stderr)

def clicked():
        result = run(["ping", adress_enter.get()], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if result.returncode==0:
            output.delete("1.0", END)
            output.insert(INSERT, 'Ресурс доступен')
            output.insert(INSERT, result.stderr)
            output.insert(INSERT, result.stdout)
            output.insert(INSERT, result.returncode)
        else:
            output.delete("1.0",END)
            output.insert(INSERT, 'Ресурс недоступен')


def tracert():
    result = run(["tracert", adress_enter.get()], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    if result.returncode == 0:
        output.delete("1.0", END)
        output.insert(INSERT, 'Ресурс доступен')
        output.insert(INSERT, result.stderr)
        output.insert(INSERT, result.stdout)
        output.insert(INSERT, result.returncode)
    else:
        output.delete("1.0", END)
        output.insert(INSERT, 'Ресурс недоступен')

def request():
    resp = adress_enter.get()
    response = requests.get(f'http://ipinfo.io/'+resp+'/json')
    user_ip = response.json()['ip']
    user_city = response.json()['city']
    user_region = response.json()['region']
    user_country = response.json()['country']
    user_location = response.json()['loc']
    user_org = response.json()['org']
    user_timezone = response.json()['timezone']
    output.delete("1.0", END)
    output.insert(INSERT,"IP адрес    ")
    output.insert(INSERT,user_ip)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Город    ")
    output.insert(INSERT,user_city)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Регион    ")
    output.insert(INSERT,user_region)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Страна    ")
    output.insert(INSERT,user_country)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Расположение    ")
    output.insert(INSERT,user_location)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Организация    ")
    output.insert(INSERT,user_org)
    output.insert(INSERT, '\n')
    output.insert(INSERT,"Таймзон    ")
    output.insert(INSERT,user_timezone)
    output.insert(INSERT, '\n')

def weather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Rostov"
    API_KEY = "9d075ab04124d2af84c606a28995e976"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    #response = requests.get(URL)
    print(URL)

window = Tk()
window.title("Проверка пинга сайта")
window.geometry('700x750')
name_pr = Label(window, text="Проверка доступности ресурса", font=("Arial", 14))
name_pr.grid(column=0, row=1, sticky=N, columnspan=10)
adress = Label(window, text="Введите адрес для проверки:", font=("Arial", 10))
adress.grid(column=0, row=2)
adress_enter = Entry(window, width=30)
adress_enter.grid(column=1, row=2)
adress_w = Label(window, text="Введите город:", font=("Arial", 10))
adress_w.grid(column=0, row=3)
adress_w_enter = Entry(window, width=30)
adress_w_enter.grid(column=1, row=3)
btn_out = Button(window, text="Проверка ресурса", command=clicked)
btn_out.grid(column=3, row=2)
btn_out = Button(window, text= 'Трассировка', command=tracert)
btn_out.grid(column=4, row=2)
btn_out = Button(window, text= 'Инфо о IP', command=request)
btn_out.grid(column=3, row=3)
btn_out = Button(window, text= 'Погода', command=weather)
btn_out.grid(column=4, row=3)
output = scrolledtext.ScrolledText(window, width=100, height=20, font = ("Calibri", 8)) # Окно с удаление
output.grid(row=4,column=0,columnspan=5)

window.mainloop()