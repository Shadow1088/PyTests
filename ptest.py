import pygame

pygame.init()

size = (1000,900)
screen = pygame.display.set_mode(size)

oldMousePos = None
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Get the start time

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == "e"):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            oldMousePos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "green", oldMousePos, 30, width=4)
    
    
    
    pygame.display.flip()
    clock.tick(60)

