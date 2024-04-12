import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 300

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ввод текста")

# Шрифт для текста
font = pygame.font.Font(None, 32)

# Создание текстового поля
input_box = pygame.Rect(100, 100, 300, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos): #Этот код проверяет, было ли нажато внутри прямоугольника input_box.
                active = True #если нажато окно то активируется
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_RETURN: # Это условие проверяет, была ли нажата клавиша Enter. Если да, введенный текст выводится в консоль.
                    print(text) #Получаем текст из окна и выводим в консоль
                    text = ''
                elif event.key == pygame.K_BACKSPACE:#Это условие проверяет, была ли нажата клавиша Backspace. Если да, последний символ в тексте удаляется.
                    text = text[:-1]
                else:
                    text += event.unicode

    # Отрисовка фона и текста
    screen.fill(WHITE)
    pygame.draw.rect(screen, color, input_box, 2)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()