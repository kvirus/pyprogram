import pygame
import random
import os
import sys


pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 700, 700

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Название приложения
pygame.display.set_caption("Magic Ball")

#загружаем картинки
asklater = pygame.image.load('C:/g/mball/asklater.jpg')
bedpersp = pygame.image.load('C:/g/mball/bedpersp.jpg')
dontknow = pygame.image.load('C:/g/mball/dontknow.jpg')
goodschance = pygame.image.load('C:/g/mball/goodschance.jpg')
itstak = pygame.image.load('C:/g/mball/itstak.jpg')
manysomn = pygame.image.load('C:/g/mball/manysomn.jpg')
maybe = pygame.image.load('C:/g/mball/maybe.jpg')
no = pygame.image.load('C:/g/mball/no.jpg')
nottake = pygame.image.load('C:/g/mball/nottake.jpg')
nowno = pygame.image.load('C:/g/mball/nowno.jpg')
ofcourse = pygame.image.load('C:/g/mball/ofcourse.jpg')
smallshance = pygame.image.load('C:/g/mball/smallshance.jpg')
startssayno = pygame.image.load('C:/g/mball/startssayno.jpg')
tobe = pygame.image.load('C:/g/mball/tobe.jpg')
todo = pygame.image.load('C:/g/mball/todo.jpg')
yeees = pygame.image.load('C:/g/mball/yeees.jpg')
yes = pygame.image.load('C:/g/mball/yes.jpg')
yesofcour = pygame.image.load('C:/g/mball/yesofcour.jpg')

#Получаем список файлов в директории
image_folder = R'C:\g\mball\ans'
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Рендомный выбор изображения
def ans2():
    selected_image = pygame.image.load(os.path.join(image_folder, random.choice(image_files)))
    selected_image = pygame.transform.scale(selected_image, (170, 170))  # Изменение размера изображения
    return selected_image

#Бекграунд
back = pygame.image.load('C:/g/mball/back.jpg')

#Область нажатия
srect = pygame.Rect(0, 0, 700, 700)


WHITE = (255, 255, 255)


# Выбор ответа
def ansver():
    choices = [asklater,bedpersp,dontknow,goodschance,itstak,manysomn,maybe,no,nottake,nowno,ofcourse,smallshance,startssayno,tobe,yeees,yes,yesofcour]
    return random.choice(choices)



def game_loop():
    screen.blit(back, (0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(back, (0, 0))
                if srect.collidepoint(event.pos):
                    #ansver1 = ansver()
                    ansver1 = ans2()
                    screen.blit(ansver1, (260, 240))
        pygame.display.flip()
    pygame.display.flip()

# Запуск игрового цикла
game_loop()