import pygame

pygame.init()

resolutions = ["Normal", "Low", "High"]
resolution = "Normal"

window_sizes = ["Small", "Normal", "Big", "Full"]
window_size = "Normal"

if resolution not in resolutions:
    print("Invalid resolution.")

if window_size not in window_sizes:
    print("Invalid window size.")
elif window_size == "Small":
    screen_width = 424
    screen_height = 212
elif window_size == "Normal":
    screen_width = 800
    screen_height = 400
elif window_size == "Big":
    screen_width = 1200
    screen_height = 600
elif window_size == "Full":
    print("Full window size is not set yet")


screen = pygame.display.set_mode((screen_width, screen_height))

print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()
