import pygame
import random 
import math

pygame.init()

xy = (1500, 900)
screen = pygame.display.set_mode(xy)
pygame.display.set_caption("Test")


redRect = pygame.image.load("graphics/redrect.png")
redRectScale = pygame.transform.scale(redRect, (50, 50))
RectredRect = redRectScale.get_rect(center=(750, 450))
redCircle = pygame.image.load("graphics/redcircle.png")
redCircleScale = pygame.transform.scale(redCircle, (100, 100))
redline = pygame.image.load("graphics/redline.png")

class Line:
    def __init__(self, img, pos):
        self.img = img
        self.rect = self.img.get_rect(center = pos)

    def update(self, target_pos):
        angle = math.atan2(target_pos[1] - self.rect.center[1], target_pos[0] - self.rect.center[0])
        angle = math.degrees(angle)+90
        self.image = pygame.transform.rotate(self.img, -angle)
        self.rect = self.image.get_rect(center = self.rect.center)
line = Line(redline, (screen.get_width() // 2, screen.get_height() // 2))


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_e):
            pygame.quit()
            exit()

    mouse = pygame.mouse.get_pos()

    screen.fill("grey15")
    screen.blit(redRectScale, RectredRect)

    RectredCircle = redCircleScale.get_rect(center = (mouse[0], mouse[1]))
    screen.blit(redCircleScale, RectredCircle)

    line.update(mouse)
    screen.blit(line.image, line.rect)

    pygame.display.update()
    clock.tick(60)