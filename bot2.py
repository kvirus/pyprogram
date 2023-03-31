import telebot
from pythonping import ping
import os, wikipedia, re
from telebot import types
import paramiko
import requests
#from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

#!!!! Не забудь поменять пароли на скриптах!!!

passwd = "Jac" #Пароль для скриптов!!!

#Активация работы с SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#from ping3 import ping
bot = telebot.TeleBot('5388668812:AAFiSusMexQ5fO9mkxpUjp20uje-qGJp4ws') #Основной БОТ

#bot = telebot.TeleBot('5800064216:AAFWd0BnsgM9MH94ppPZKU9plisU0L9K_2k') #Запасной бот

#Верхний уровень клавиатуры (выбор раздела)

keyboard_up = types.InlineKeyboardMarkup()
key_1c = types.InlineKeyboardButton(text='Открыть/закрыть доступ в 1С', callback_data='1c_rule')
key_mikrot = types.InlineKeyboardButton(text='Открыть/закрыть доступ в Микротик', callback_data='mikrot_rule')
keyboard_up.add(key_1c)
keyboard_up.add(key_mikrot)

#Открытие/закрытие правил 1С

keyboard_1c = types.InlineKeyboardMarkup()
key_sql_open = types.InlineKeyboardButton(text='\U0001F7E2 Открыть правило 1C', callback_data='sql_open')
key_sql_close = types.InlineKeyboardButton(text='\U000026D4 Закрыть правило 1C', callback_data='sql_close')
keyboard_1c.add(key_sql_open)
keyboard_1c.add(key_sql_close)

#Правила Микротика

keyboard_mikrot = types.InlineKeyboardMarkup()
key_micr_open1 = types.InlineKeyboardButton(text='\U0001F7E2 Открыть Микротик снаружи', callback_data='micr_open')
key_micr_close1 = types.InlineKeyboardButton(text='\U000026D4 Закрыть Микротик снаружи', callback_data='micr_close')
keyboard_mikrot.add(key_micr_open1)
keyboard_mikrot.add(key_micr_close1)

keyboard_ping = types.InlineKeyboardMarkup()
key_ping_sql = types.InlineKeyboardButton(text='\U0001F7E2 Проверка сервера 1с', callback_data='ping_sql')
key_ping_term = types.InlineKeyboardButton(text='\U000026D4 Проверка Терминала', callback_data='ping_term')
key_ping_host_sql = types.InlineKeyboardButton(text='\U000026D4 Проверка хоста SQL', callback_data='ping_host_sql')
key_ping_host_all = types.InlineKeyboardButton(text='\U000026D4 Проверка общего хоста', callback_data='ping_host_all')
key_ping_all = types.InlineKeyboardButton(text='\U000026D4 Проверка всех серверов', callback_data='ping_all')
keyboard_ping.add(key_ping_sql)
keyboard_ping.add(key_ping_term)
keyboard_ping.add(key_ping_host_sql)
keyboard_ping.add(key_ping_host_all)
keyboard_ping.add(key_ping_all)

# keyboard = types.InlineKeyboardMarkup()
# key_start = types.InlineKeyboardButton(text='\U0001F609 Википедия \U0001F915', callback_data='startt')
# key_spisok_wr = types.InlineKeyboardButton(text='Добавить в список', callback_data='spisok_wr')
# key_spisok_r = types.InlineKeyboardButton(text='Показать список', callback_data='spisok_r')
# key_spisok_del = types.InlineKeyboardButton(text='Удалить строчку из списка', callback_data='spisok_del')
# key_spisok_clear = types.InlineKeyboardButton(text='Очистить список', callback_data='spisok_clear')
# key_sql_open = types.InlineKeyboardButton(text='Открыть правило 1C', callback_data='sql_open')
# key_sql_close = types.InlineKeyboardButton(text='Закрыть правило 1C', callback_data='sql_close')
# key_micr_open = types.InlineKeyboardButton(text='Открыть Микротик снаружи', callback_data='micr_open')
# key_micr_close = types.InlineKeyboardButton(text='Закрыть Микротик снаружи', callback_data='micr_close')
#
# #keyboard.add(key_start)
# #keyboard.add(key_spisok_wr,key_spisok_r)
# #keyboard.add(key_spisok_del)
# #keyboard.add(key_spisok_clear)
# keyboard.add(key_sql_open)
# keyboard.add(key_sql_close)
# keyboard.add(key_micr_open)
# keyboard.add(key_micr_close)
# #wikipedia.set_lang("ru")

#Кнопки клавиатуры
# button_hi = KeyboardButton('Привет! 👋')
#
# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(button_hi)


keyboard1 = types.InlineKeyboardMarkup()
key_pc_back_open = types.InlineKeyboardButton(text='\U0001F7E2 Открыть доступ на ПК бекап (49900)', callback_data='pc_back_open')
key_host_basic_open = types.InlineKeyboardButton(text='\U0001F7E2 Открыть на основной хост (49901)', callback_data='host_basic_open')
key_pc_back_close = types.InlineKeyboardButton(text='\U000026D4 Закрыть доступ на ПК бекап (49900)', callback_data='pc_back_close')
key_host_basic_close = types.InlineKeyboardButton(text='\U000026D4 Закрыть на основной хост (49901)', callback_data='host_basic_close')
keyboard1.add(key_pc_back_open)
keyboard1.add(key_pc_back_close)
keyboard1.add(key_host_basic_open)
keyboard1.add(key_host_basic_close)



@bot.message_handler(commands=['start'])
def start(message):
    adm = [32949476] #Доступ пользователей
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Нефик тут лазить! Уходите!')
    else:
        bot.send_message(message.chat.id, "Что будем делать:", reply_markup=keyboard_up)


@bot.message_handler(commands=['mikrotik'])
def start(message):
    adm = [32949476]  # Доступ пользователей
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Нефик тут лазить! Уходите!')
    else:
        bot.send_message(message.chat.id, "Правила Микротика:", reply_markup=keyboard1)

@bot.message_handler(commands=['ping'])
def start(message):
    adm = [32949476]  # Доступ пользователей
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Нефик тут лазить! Уходите!')
    else:
        bot.send_message(message.chat.id, "Проверка пинга:", reply_markup=keyboard_ping)




def info(message):
    print(message.text)
    bot.send_message(message.chat.id, getwiki(message.text))

@bot.callback_query_handler(func=lambda call: call.data =='1c_rule')
def spisok_del(call):
    if call.data == "1c_rule":
        bot.send_message(call.message.chat.id, "Что будем делать:", reply_markup=keyboard_1c)

@bot.callback_query_handler(func=lambda call: call.data =='mikrot_rule')
def spisok_del(call):
    if call.data == "mikrot_rule":
        bot.send_message(call.message.chat.id, "Что будем делать:", reply_markup=keyboard_mikrot)

#Открываем правило SQL

@bot.callback_query_handler(func=lambda call: call.data =='sql_open')#ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "sql_open": #Сюда вписать настройки подключения к SQL и открытия правила, сделать для закрытия
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat enable numbers=5')
    bot.send_message(call.message.chat.id, '1C доступ открыт')

#Закрываем правило SQL

@bot.callback_query_handler(func=lambda call: call.data =='sql_close') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "sql_close": #Сюда вписать настройки подключения к SQL и открытия правила, сделать для закрытия
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat disable numbers=5')
    bot.send_message(call.message.chat.id, '1C доступ закрыт')
#Открыаем микрот снаружи

@bot.callback_query_handler(func=lambda call: call.data =='micr_open')   #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "micr_open": #Сюда вписать настройки подключения к SQL и открытия правила, сделать для закрытия
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall filter disable numbers=2')
    bot.send_message(call.message.chat.id, 'Микрот открыт снаружи!')

#Закрываем Микрот снаружи

@bot.callback_query_handler(func=lambda call: call.data =='micr_close')   #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "micr_close": #Сюда вписать настройки подключения к SQL и открытия правила, сделать для закрытия
        #client.connect(hostname='192.168.1.34', port=2231, username="bka", password=passwd, look_for_keys=False, allow_agent=False)
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False, allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall filter enable numbers=2')
    bot.send_message(call.message.chat.id, 'Микрот закрыт снаружи!')


#Открываем комп бекапа снаружи

@bot.callback_query_handler(func=lambda call: call.data =='pc_back_open')   #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "pc_back_open":
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat enable numbers=4')
    bot.send_message(call.message.chat.id, 'ПК бекапа открыт')

#Закрываем комп бекапа снаружи

@bot.callback_query_handler(func=lambda call: call.data =='pc_back_close') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "pc_back_close":
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat disable numbers=4')
    bot.send_message(call.message.chat.id, 'ПК бекапа закрыт')

#Открываем основной хост снаружи

@bot.callback_query_handler(func=lambda call: call.data =='host_basic_open')   #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "host_basic_open":
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat enable numbers=6')
    bot.send_message(call.message.chat.id, 'Хост открыт')

#Закрываем основной хост снаружи

@bot.callback_query_handler(func=lambda call: call.data =='host_basic_close') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "host_basic_close":
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat disable numbers=6')
    bot.send_message(call.message.chat.id, 'ПК бекапа закрыт')



#Пинг 1С сервера

@bot.callback_query_handler(func=lambda call: call.data =='ping_sql') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "ping_sql":
        response_list = ping('10.100.2.32', size=40, count=3)
        print(response_list.stats_packets_returned)
    bot.send_message(call.message.chat.id,"Потеряно пакетов")
    bot.send_message(call.message.chat.id, response_list.packet_loss)

#Пинг Терминала

@bot.callback_query_handler(func=lambda call: call.data =='ping_term') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "ping_term":
        response_list = ping('10.100.2.145', size=40, count=3)
        print(response_list)
    bot.send_message(call.message.chat.id, "Потеряно пакетов")
    bot.send_message(call.message.chat.id, response_list.packet_loss)

#Пинг  хоста 1С

@bot.callback_query_handler(func=lambda call: call.data =='ping_host_sql') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "ping_host_sql":
        response_list = ping('10.100.2.31', size=40, count=3)
        print(response_list)
    bot.send_message(call.message.chat.id, "Потеряно пакетов")
    bot.send_message(call.message.chat.id, response_list.packet_loss)

#Пинг общего хоста

@bot.callback_query_handler(func=lambda call: call.data =='ping_host_all') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "ping_host_all":
        response_list = ping('10.100.2.43', size=40, count=3)
        print(response_list)
    bot.send_message(call.message.chat.id, "Потеряно пакетов")
    bot.send_message(call.message.chat.id, response_list.packet_loss)

#Пинг всех серверов

@bot.callback_query_handler(func=lambda call: call.data =='ping_all') #ПАРОЛЬ!!!!
def spisok_del(call):
    if call.data == "ping_all":
        response_list_1 = ping('10.100.2.32', size=40, count=4)
        bot.send_message(call.message.chat.id, "Потеряно пакетов сервер 1с - {}".format(response_list_1.stats_packets_lost))
        response_list_2 = ping('10.100.2.145', size=40, count=4)
        bot.send_message(call.message.chat.id, "Потеряно пакетов сервер Терминалов - {}".format(response_list_2.stats_packets_lost))
        response_list_3 = ping('10.100.2.31', size=40, count=4)
        bot.send_message(call.message.chat.id, "Потеряно пакетов сервер Хост 1с -{}".format(response_list_3.stats_packets_lost))
        response_list_4 = ping('10.100.2.43', size=40, count=4)
        bot.send_message(call.message.chat.id, "Потеряно пакетов общий хост - {}".format(response_list_4.stats_packets_lost))
        response_list_5 = ping('8.8.8.8', size=40, count=4)
        bot.send_message(call.message.chat.id,"Пинг интернета, потерь - {}".format(response_list_5.stats_packets_lost))


bot.polling(none_stop=True)