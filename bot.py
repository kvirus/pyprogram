import telebot
import os, wikipedia, re
from telebot import types
import paramiko
#from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

#!!!! Не забудь поменять пароли на скриптах!!!

passwd = "Ja" #Пароль для скриптов!!!

#Активация работы с SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#from ping3 import ping
bot = telebot.TeleBot('') #Основной БОТ

#bot = telebot.TeleBot('') #Запасной бот

keyboard = types.InlineKeyboardMarkup()
key_start = types.InlineKeyboardButton(text='\U0001F609 Википедия \U0001F915', callback_data='startt')
key_spisok_wr = types.InlineKeyboardButton(text='Добавить в список', callback_data='spisok_wr')
key_spisok_r = types.InlineKeyboardButton(text='Показать список', callback_data='spisok_r')
key_spisok_del = types.InlineKeyboardButton(text='Удалить строчку из списка', callback_data='spisok_del')
key_spisok_clear = types.InlineKeyboardButton(text='Очистить список', callback_data='spisok_clear')
key_sql_open = types.InlineKeyboardButton(text='Открыть правило 1C', callback_data='sql_open')
key_sql_close = types.InlineKeyboardButton(text='Закрыть правило 1C', callback_data='sql_close')
key_micr_open = types.InlineKeyboardButton(text='Открыть Микротик снаружи', callback_data='micr_open')
key_micr_close = types.InlineKeyboardButton(text='Закрыть Микротик снаружи', callback_data='micr_close')

#keyboard.add(key_start)
#keyboard.add(key_spisok_wr,key_spisok_r)
#keyboard.add(key_spisok_del)
#keyboard.add(key_spisok_clear)
keyboard.add(key_sql_open)
keyboard.add(key_sql_close)
keyboard.add(key_micr_open)
keyboard.add(key_micr_close)
wikipedia.set_lang("ru")

#Кнопки клавиатуры
# button_hi = KeyboardButton('Привет! 👋')
#
# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(button_hi)


keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
key_sql_open1 = types.InlineKeyboardButton(text='Открыть правило 1C', callback_data='sql_open')
key_sql_close1 = types.InlineKeyboardButton(text='Закрыть правило 1C', callback_data='sql_close')
keyboard1.add(key_sql_open1)
keyboard1.add(key_sql_close1)

#Функция википедия
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Что будем делать:", reply_markup=keyboard)


@bot.message_handler(commands=['mikrotik'])
def start(message):
    bot.send_message(message.chat.id, "Пока что бот умеет это:", reply_markup=keyboard1)


@bot.message_handler(commands=["wiki"])
def start(message):
    bot.send_message(message.chat.id, 'О чем рассказать?')
    bot.register_next_step_handler(message, info)

def info(message):
    print(message.text)
    bot.send_message(message.chat.id, getwiki(message.text))

@bot.callback_query_handler(func=lambda call: call.data =='spisok_wr')
def callback_worker1(call):
    if call.data == "spisok_wr":
        msg1 =bot.send_message(call.message.chat.id, 'Запись списка продуктов')
        bot.register_next_step_handler(msg1, spisok_wr1)

def spisok_wr1(message):
    file_sp_wr2 = open("c:/intel/1.txt", 'r')
    len_file = file_sp_wr2.readlines()
    file_sp_wr2.close()
    x=0
    for i in len_file:
        x=x+1
        print(i)
    print('x равно',x)
    x1 = str(x)
    print(len_file)
    lens = str(len(len_file))
    print(lens)
    wr = str(message.text)
    file_sp_wr1 = open("c:/intel/1.txt", 'a')
    file_sp_wr1.write(x1 + '. ' + wr + "\n")
    file_sp_wr1.close()

@bot.callback_query_handler(func=lambda call: call.data =='spisok_r')
def callback_worker_r(call):
    if call.data == "spisok_r":
        bot.send_message(call.message.chat.id, 'Список такой:')
        file_sp_wr1 = open("c:/intel/1.txt", 'r')
        line_wr1 = file_sp_wr1.readlines()
        # print(line_wr1[2])
        for i in line_wr1:
            bot.send_message(call.message.chat.id, i)
        file_sp_wr1.close()

@bot.callback_query_handler(func=lambda call: call.data =='spisok_del')
def spisok_del(call):
    if call.data == "spisok_del":
        msg2 = bot.send_message(call.message.chat.id, 'Какую строчку удалить?:')
        bot.register_next_step_handler(msg2, spisok_del)

def spisok_del(message):
    wr_del = int(message.text)
    file_sp_del = open("c:/intel/1.txt", 'r+')
    line_del = file_sp_del.readlines()
    del line_del[wr_del]
    file_sp_del.close()
    os.remove("c:/intel/1.txt")
    file_sp_new_del = open("c:/intel/1.txt", 'w')
    for i in line_del:
            file_sp_new_del.write(i)
    file_sp_new_del.close()

@bot.callback_query_handler(func=lambda call: call.data =='spisok_clear')
def spisok_del(call):
    if call.data == "spisok_clear":
        open('c:/intel/1.txt', 'w').close()
    msg2 = bot.send_message(call.message.chat.id, 'Список очищен')

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



@bot.callback_query_handler(func=lambda call: call.data =='startt')
def callback_worker(call):
    if call.data == "startt":
        msg = bot.send_message(call.from_user.id, "Что ищем?")
        bot.register_next_step_handler(msg,msg_us)
def msg_us(message):
    print('1')
    bot.send_message(message.from_user.id, getwiki(message.text))



    # def get_text_messages(message):
    #     bot.register_next_step_handler (call,search)
    # def search(call):
    #     return
    #     bot.send_message(call.message.chat.id, getwiki(call.message.text))



@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.from_user.id, 'адрес пинга')
    bot.register_next_step_handler(message, addr)
def addr(message):
    z=str(message.text)
    file = open("c:/intel/1.txt", 'w')
    for i in z:
        file.write(i)
    file.close()
    file = open("c:/intel/1.txt", 'r')
    line = str(file.readlines())
    #pyping('8.8.8.8')
    print(x)
        #bot.send_message(message.from_user.id, x)
    file.close()

    #file = open("c:/intel/1.txt", 'w')
    #for i in z:
    #    file.write(i)
    #file.close()

@bot.message_handler(commands=['spisok_w'])
def spisok_w(message):
    bot.send_message(message.from_user.id, 'Запись списка продуктов')
    bot.register_next_step_handler(message, spisok_wr)

def spisok_wr(message):
    wr = str(message.text)
    file_sp_wr = open("c:/intel/1.txt", 'a')
    file_sp_wr.write(wr + "\n")
    file_sp_wr.close()


@bot.message_handler(commands=['spisok_r'])
def spisok_r(message):
    bot.send_message(message.from_user.id, 'Список такой:')
    file_sp_wr1 = open("c:/intel/1.txt", 'r')
    line_wr1 = file_sp_wr1.readlines()
    #print(line_wr1[2])
    for i in line_wr1:
        bot.send_message(message.from_user.id, i)
    file_sp_wr1.close()
@bot.message_handler(commands=['spisok_del'])
def spisok_del(message):
    bot.send_message(message.from_user.id, 'Какую строчку удалить?:')
    bot.register_next_step_handler(message, spisok_del)

def spisok_del(message):
    wr_del = int(message.text)
    file_sp_del = open("c:/intel/1.txt", 'r+')
    line_del = file_sp_del.readlines()
    del line_del[wr_del]
    file_sp_del.close()
    os.remove("c:/intel/1.txt")
    file_sp_new_del = open("c:/intel/1.txt", 'w')
    for i in line_del:
            file_sp_new_del.write(i)
   # file_sp_new_del.write(" "+ '\n')
    #file_sp_new_del.write("\n")
    file_sp_new_del.close()
    # file_sp_wr1 = open("c:/intel/1.txt", 'r')
    # line_wr1 = file_sp_wr1.readlines()
    # x=int(message.text)
    # line_wr1.pop(x)

#    bot.register_next_step_handler(message, spisok_r)

# def spisok_wr(message):
#     wr = str(message.text)
#     file_sp_wr = open("c:/intel/1.txt", 'r')
#     for i in file_sp_wr:
#         print(i)
#     file_sp_wr.close()




@bot.message_handler(commands=['help'])
def ping(message):
    bot.send_message(message.from_user.id, 'Тут всякая фигня')


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "привет":
#         bot.send_message(message.from_user.id, "привет привет")
#     elif message.text == "даша":
#         bot.send_message(message.from_user.id, "мммм любимая :-****")
#     elif message.text == "Даша":
#         bot.send_message(message.from_user.id, "мммм любимая :-****")
#     elif message.text == "2+2":
#         bot.send_message(message.from_user.id, 2+2)
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# @bot.message_handler(commands=['command'])
# def _command_(message):
#      bot.send_message(message.chat.id, "Введите имя: ")
#      bot.register_next_step_handler(message, add_user)
#
# def add_user(message):
#     #тут функция записи в бд
#     pass



bot.polling(none_stop=True)
