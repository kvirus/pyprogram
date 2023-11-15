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

walk_left = [player1,player2,player_1,player]

player_walk = 0

bg = pygame.image.load('c:/g/back.png')

running = True

clock = pygame.time.Clock()
bg_x = 0

while running:

    screen.blit(bg, (bg_x, 0))
    bg_x += 5
    screen.blit(bg, (bg_x-854, 0))
    screen.blit(walk_left[player_walk],(700,200))
    if player_walk == 3:
        player_walk = 0
        #time.sleep(0.15)
    else:
        player_walk += 1
        #time.sleep(0.15)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(5)
