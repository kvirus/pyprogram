import pygame
import sys
import random
import time

pygame.init()
window_width = 853
window_height = 434
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('MI First Game')
player  = pygame.image.load('C:/g/1b.png')
player_1  = pygame.image.load('C:/g/1b_1.png')
player1 = pygame.image.load('C:/g/1c.png')
player2 = pygame.image.load('C:/g/1d.png')
ghost = pygame.image.load('C:/g/ghost.png')
ghost_min = pygame.transform.scale(ghost,(40,40))
ghost_x = -100

pygame.mixer.music.load('C:/g/sound.mp3')
pygame.mixer.music.set_volume(0.2)

walk_left = [player1,player2,player_1,player]

player_walk = 0

bg = pygame.image.load('c:/g/back.png')

running = True

clock = pygame.time.Clock()
bg_x = 0
pygame.mixer.music.play()
pl_go = 0

while running:
    bg_up = 0

    screen.blit(bg, (bg_x, 0))
    bg_x += 50 #скорость персонажа
    screen.blit(bg, (bg_x-854, 0))
    screen.blit(ghost_min, (ghost_x, 300))

    player_rect = walk_left[0].get_rect(topleft=(700-pl_go,200 - bg_up))
    ghost_rect = ghost_min.get_rect(topleft=(ghost_x,250))

    if player_rect.colliderect(ghost_rect):
        print('game over')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bg_up += 100
                pl_go += 130
    screen.blit(walk_left[player_walk], (700-pl_go , 200 - bg_up))

    if pl_go >= 650:
        pl_go = 0
    else:
        pl_go += 10
    if player_walk == 3:
        player_walk = 0
        #time.sleep(0.15)
    else:
        player_walk += 1
        #time.sleep(0.15)
    if bg_x >= 800:
        bg_x = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    ghost_x +=30 #скорость приведения
    if ghost_x >= 900:
        ghost_x = -50
    clock.tick(5)
