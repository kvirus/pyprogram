import pygame
import random

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 400, 300

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, ножницы, бумага")

# Шрифт
font = pygame.font.Font(None, 36)

# Выбор компьютера
def computer_choice():
    choices = ["Камень", "Ножницы", "Бумага"]
    return random.choice(choices)

# Определение победителя
def determine_winner(player, computer):
    if player == computer:
        return "Ничья"
    elif (player == "Камень" and computer == "Ножницы") or \
         (player == "Ножницы" and computer == "Бумага") or \
         (player == "Бумага" and computer == "Камень"):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

#подгружем картинки
rock  = pygame.image.load('C:/g/rock.jpg')
rock_min = pygame.transform.scale(rock,(50,50))
paper = pygame.image.load('c:/g/paper.jpg')
paper_min = pygame.transform.scale(paper,(50,50))
sciser = pygame.image.load('c:/g/sciser.jpg')
sciser_min = pygame.transform.scale(sciser,(50,50))
play = pygame.image.load('c:/g/play.jpg')
play_min = pygame.transform.scale(play, (50,50))

button_rect1 = pygame.Rect(50, 230, 50, 50)
button_rect2 = pygame.Rect(150, 230, 50, 50)
button_rect3 = pygame.Rect(250, 230, 50, 50)

# Основной цикл программы
def game_loop():
    player_choice_text = ""
    computer_choice_text = ""
    winner_text = ""
    player_choice = ""
    button_clicked1 = False
    button_clicked2 = False
    button_clicked3 = False
    while True:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect1.collidepoint(event.pos):
                    button_clicked1 = True
                    button_clicked2 = False
                    button_clicked3 = False
                if button_rect2.collidepoint(event.pos):
                    button_clicked1 = False
                    button_clicked2 = True
                    button_clicked3 = False
                if button_rect3.collidepoint(event.pos):
                    button_clicked1 = False
                    button_clicked2 = False
                    button_clicked3 = True
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 100 and 230 <= y <= 280:
                    player_choice = "Камень"
                elif 150 <= x <= 200 and 230 <= y <= 280:
                    player_choice = "Ножницы"
                elif 250 <= x <= 300 and 230 <= y <= 280:
                    player_choice = "Бумага"
                if 320 <= x <= 370 and 230 <= y <= 280:
                    computer = computer_choice()
                    player_choice_text = "Ваш выбор: " + player_choice
                    computer_choice_text = "Компьютер выбрал: " + computer
                    winner_text = determine_winner(player_choice, computer)

        # Отрисовка кнопок выбора
        #pygame.draw.rect(screen, RED, [50, 250, 100, 40])
        screen.blit(rock_min,(50,230) )
        screen.blit(sciser_min, (150,230))
        screen.blit(paper_min, (250, 230))
        screen.blit(play_min, (320, 230))
        # play_text = font.render("И", True, RED)
        # screen.blit(play_text, [10, 10])

        # Отрисовка выбора игрока, выбора компьютера и результата
        player_text = font.render(player_choice_text, True, BLACK)
        screen.blit(player_text, [10, 10])

        computer_text = font.render(computer_choice_text, True, BLACK)
        screen.blit(computer_text, [10, 50])

        winner_display = font.render(winner_text, True, BLACK)
        screen.blit(winner_display, [10, 90])

        if button_clicked1:
            pygame.draw.rect(screen, RED, button_rect1, 4)
        if button_clicked2:
            pygame.draw.rect(screen, RED, button_rect2, 4)
        if button_clicked3:
            pygame.draw.rect(screen, RED, button_rect3, 4)
        # Обновление экрана
        pygame.display.flip()

# Запуск игрового цикла
game_loop()