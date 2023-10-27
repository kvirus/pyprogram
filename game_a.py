import pygame
import random
import time
import random

# инициализация pygame
pygame.init()

# установка размеров окна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# установка заголовка окна
pygame.display.set_caption("Убей А")

# установка цветов
white = (255, 255, 255)
black = (0, 0, 0)

# загрузка картинки
image = pygame.image.load("C:/g/4.jpg")
image1 = pygame.image.load("C:/g/1.jpg")
image2 = pygame.image.load("C:/g/2.jpg")

# Загрузка звука
sound = pygame.mixer.Sound('C:/g/shot.wav')
sound_ha = pygame.mixer.Sound('C:/g/ha.wav')
# Загружаем изображение курсора
#cursor_image = pygame.image.load("C:/g/curs.png").convert_alpha()

# Устанавливаем курсор
#pygame.mouse.set_cursor((32, 32), (0, 0), cursor_image.get_buffer())


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
            if event.type == pygame.QUIT:
                game_over = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if image_x <= mouse_x <= image_x + image.get_width() and image_y <= mouse_y <= image_y + image.get_height():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score += 1
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

        # обновление экрана
        pygame.display.update()

        # очистка экрана
        window.fill(white)

    # выход из игры
    pygame.quit()
    quit()

# запуск игры
game_loop()