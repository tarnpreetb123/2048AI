import os
import pygame
from Game import GameStateManager

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize pygame
pygame.init()
pygame.font.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Windoweva
window_size = (1200, 700)
gameDisplay = pygame.display.set_mode(window_size)
pygame.display.set_caption('2048')

# Frame rate and clock
clock = pygame.time.Clock()
running = True
solving = False

# Create a new game state manager
gsm = GameStateManager.GameStateManager(gameDisplay)

# Game Loop
while running:
    deltaT = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

        key = pygame.key.get_pressed()
        #if key[pygame.K_q]:

    gameDisplay.fill(gray)

    #Draw shit here
    gsm.update()
    gsm.draw()

    pygame.display.flip()

pygame.quit()