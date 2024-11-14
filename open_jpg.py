import os
from datetime import datetime, timedelta
from PIL import Image
import time
import schedule
import config
import pygame
import configparser as cp
import pyautogui

cfg = cp.ConfigParser()
cfg.read('cfg.ini')
#1
image_path = cfg['Settings']['img']
tim = cfg['Settings']['time']

# image_path = config.img
# tim =config.time

def open():

    pygame.init()
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN | pygame.DOUBLEBUF)
    image1 = pygame.image.load(image_path)
    #z_order = 1

    image1 = pygame.transform.scale(image1, (screen.get_width(), screen.get_height()))
    screen.blit(image1, (0, 0))

    #screen.blit(image1, (0, 0), (0, 0, image1.get_width(), image1.get_height()), z_order)
    pygame.display.flip()
    #pygame.display.update()
    time.sleep(config.tslp)
    pygame.quit()
#image_path = 'C:/cat.jpg'

def open1():
    image = Image.open(image_path)
    image.show()
    time.sleep(config.tslp)
    os.system("taskkill /im PhotosApp.exe /f")

def cls():
    pyautogui.hotkey('win', 'd')


#schedule.every().hour.at(tim).do(cls)
schedule.every().hour.at('42:00').do(cls)
schedule.every().hour.at('42:05').do(open)
schedule.every().hour.at('42:20').do(cls)
while True:
    schedule.run_pending()
    time.sleep(1)



    # # Определяем текущее время

    # now = datetime.now()
    # print(now)
    # # Открываем картинку, если текущее время равно 0 минутам
    # if now.minute == 0:
    #     image = Image.open(image_path)
    #     image.show()
    #
    #     # Закрываем картинку через 15 минут
    #     #time.sleep(1)  # 15 минут = 900 секунд
    #     #image.close()
    #     os.system("taskkill /im PhotosApp.exe /f")

    # Ждем до следующего часа
    # next_hour = now.replace(hour=now.hour+1, minute=0, second=0, microsecond=0)
    # time_to_wait = (next_hour - now).total_seconds()
    # time.sleep(time_to_wait)
