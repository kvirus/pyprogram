import pygame
import random
import time
import random

# инициализация pygame
pygame.init()

# установка размеров окна
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

# создание буферной области
buffer_size = (800, 200)
buffer = pygame.Surface(buffer_size)


# установка заголовка окна
pygame.display.set_caption("Убей А")

# установка цветов
white = (255, 255, 255)
black = (0, 0, 0)

# загрузка картинки
image = pygame.image.load("C:/g/3.jpg")
image1 = pygame.image.load("C:/g/3.jpg")
image2 = pygame.image.load("C:/g/2.jpg")

# Загрузка звука
sound = pygame.mixer.Sound('C:/g/shot.wav')
sound_ha = pygame.mixer.Sound('C:/g/ha.wav')
# Загружаем изображение курсора
#cursor_img = pygame.image.load('C:/g/curs.png').convert_alpha()

#cursor = pygame.cursors.compile(cursor_img)
# Создание кортежа изображения курсора
#cursor_data, cursor_mask = pygame.cursors.compile(cursor_img.get_buffer().raw, black=cursor_img.get_at((0, 0)))

# Создаем кнопку
button_rect = pygame.Rect(150, 100, 100, 50)

# Установка курсора мыши
#pygame.mouse.set_cursor((cursor_img.get_width(), cursor_img.get_height()), (0, 0), cursor_data, cursor_mask)
#pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.mouse.set_cursor(*pygame.cursors.ball)

# основной цикл игры
def game_loop():
    # Установка начальной картинки

    game_over = False
    # начальные координаты картинки
    image_x = random.randrange(0, window_width - image.get_width())
    image_y = random.randrange(0, window_height - image.get_height())
    # начальное количество очков
    score = 0
    # основной цикл игры
    x = image
    while not game_over:
        current_image = x
        # обработка нажатий клавиш и выход из игры
        for event in pygame.event.get():

            if 80 < image_x < 760:
                image_x = image_x + random.randint(-20, 20)
            else:
                image_x = image_x + random.randint(0, 0)

            if 80 < image_y < 760:
                image_y = image_y + random.randint(-20, 20)
            else:
                image_y = image_y + random.randint(0, 0)

            if event.type == pygame.QUIT:
                game_over = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if image_x <= mouse_x <= image_x + image.get_width() and image_y <= mouse_y <= image_y + image.get_height():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score += 1
                        print(score)
                        sound.play()
                        current_image = image2
                        image_x = random.randrange(0, window_width - image.get_width())
                        image_y = random.randrange(0, window_height - image.get_height())
                        x = random.choice([image, image1])

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score -= 1
                        sound_ha.play()
                        if score == - 1:
                            print('game over')
                            font = pygame.font.Font(None, 25)
                            text = "Game как говорится oveR \n нажмите любую клавишу"
                            score_text = font.render(text, True, black)
                            text_rect = score_text.get_rect()
                            text_rect.center =(400,400)
                            #pygame.draw.rect(window, (255, 0, 0), button_rect)
                            window.blit(score_text,text_rect)
                            pygame.display.flip()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        pygame.quit()
                                        quit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     current_image = image2
            #     mouse_x, mouse_y = pygame.mouse.get_pos()
            #     if image_x <= mouse_x <= image_x + image.get_width() and image_y <= mouse_y <= image_y + image.get_height():
            #         score += 1
            #         sound.play()
            #         image_x = random.randrange(0, window_width - image.get_width())
            #         image_y = random.randrange(0, window_height - image.get_height())
            #     else:
            #         score -= 1
            #         sound_ha.play()
        # отрисовка картинки
        window.blit(current_image, (image_x, image_y))
        pygame.time.delay(100)
        pygame.display.flip()

        # вывод счета на экран
        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Количество очков: " + str(score), True, black)
        window.blit(score_text, (10, 10))
        #window.blit(image1, (10+score*10, 10))


        # обновление экрана
        pygame.display.update()

        # очистка экрана
        window.fill(white)

    # выход из игры
    pygame.quit()
    quit()

# запуск игры
game_loop()