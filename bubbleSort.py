import pygame
import time
import sys
import random

pygame.init()
SCREENX = 1000
SCREENY = 600
screen = pygame.display.set_mode((SCREENX, SCREENY))
ARRAY_SIZE = 100

BAR_WIDTH = SCREENX // ARRAY_SIZE

list0 = [random.randint(50, 500) for _ in range(ARRAY_SIZE)]

def draw_array():
    screen.fill("grey15")
    for i, value in enumerate(list0):
        color = "blue" if i % 2 == 0 else "red" # firebrick1 + red, navy + blue, blue + blue2, yellow + orange
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, SCREENY - value, BAR_WIDTH, value))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_e):
                pygame.quit()
                sys.exit()
        

def bubble_sort():
    for i in range(len(list0)):
        for j in range(len(list0)-i-1):
            if list0[j] > list0[j+1]:
                list0[j], list0[j+1] = list0[j+1], list0[j]
                draw_array()
                pygame.display.update()
                
                

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_e):
            pygame.quit()
            sys.exit()

    bubble_sort()
    draw_array()
    
    
    pygame.display.update()
    clock.tick(60)