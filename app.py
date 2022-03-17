import pygame
import yahtzee
from constants import *


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

game = yahtzee.Yahtzee()

while game.getGameContinue():

    # Check if the user closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.setGameContinue(False)

    screen.fill(SCREEN_COLOR)

    pygame.display.flip()
    
    game.runOneIteration()

print('GAME OVER!')
pygame.quit()
