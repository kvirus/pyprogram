import requests
import random
import telebot
from bs4 import BeautifulSoup as b

# URL = 'https://www.anekdot.ru/release/anekdot/week/'
# API_KEY = '5965034250:AAG7Gv6B90IUI2Zlv5zn6vFbVfSoVtX1WyM'
# def parser(url):
#     r = requests.get(url)
#     soup = b(r.text, 'html.parser')
#     anekdots = soup.find_all('div', class_='text')
#     return [c.text for c in anekdots] #возвращает очищенный список с анекдотами
#
# list_of_jokes = parser(URL)
# random.shuffle(list_of_jokes) #перемешивает анекдоты

bot = telebot.TeleBot("5965034250:AAG7Gv6B90IUI2Zlv5zn6vFbVfSoVtX1WyM")
@bot.message_handler(commands=['начать'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')
    #bot.send_message(message.chat.id, 'О чем рассказать?')
    bot.register_next_step_handler(message, info)

bot.polling(none_stop=True)
# def hello(message):
#     bot.send_message(message.chat.id, 'Привет!')

#bot.polling(non_stop=True)