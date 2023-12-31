import pygame, sys
import time
import math

pygame.init()


class Settings:
    resolutions = ["Low", "Normal", "High"]
    resolution = "Normal"

    window_sizes = ["Small", "Normal", "Big", "Full"]
    window_size = "Small"
sets = Settings()

if sets.resolution not in sets.resolutions:
    print("Invalid resolution.")

if sets.window_size not in sets.window_sizes:
    print("Invalid window size.")
elif sets.window_size == "Small":
    screen_width = 800
    screen_height = 400
    x = 1
    y = 1
elif sets.window_size == "Normal":
    screen_width = 1200
    screen_height = 600
    x = 1.5	
    y = 1.5
elif sets.window_size == "Big":
    screen_width = 1800
    screen_height = 900
    x = 2.25
    y = 2.25
elif sets.window_size == "Full":
    print("Full window size is not set yet")


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meteor shooter - ZZ")

# sizes
test_surface = pygame.Surface((400*x, 200*y))
line0 = pygame.Surface(((math.floor((screen_width/2)-(test_surface.get_width()/2))),20))
line1 = pygame.Surface(((math.floor((screen_width/2)-(test_surface.get_width()/2))),20))
def QUIT():
    pygame.quit()
    sys.exit()

while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updates
    screen.fill("grey13")
    # location of surfaces
    test_surface.fill("grey")
    screen.blit(test_surface, ((screen_width/2)-(test_surface.get_width()/2), 70))

    line0.fill("red")
    screen.blit(line0, (0, 70-10))

    line1.fill("red")
    screen.blit(line1, ((screen_width/2)+(test_surface.get_width()/2), test_surface.get_height()+70-10))

    ##
    pygame.display.update()