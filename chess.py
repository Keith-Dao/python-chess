# Import modules
import pygame, sys

# Files
from constants import *

# Functions
def drawTiles(screen: pygame.Surface):
    # Background / UI colour
    screen.fill((100,100,100))

    # Create checker board
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            x = UI_WIDTH + i * SQUARE_DIMENSIONS
            y = UI_HEIGHT + j * SQUARE_DIMENSIONS

            if (i + j) % 2 == Colours.WHITE.value:  
                colour = (255, 255, 255)
            else:
                colour = (0, 0, 0)
            pygame.draw.rect(screen, colour, (x, y, SQUARE_DIMENSIONS, SQUARE_DIMENSIONS))


def main():
    """ Setup the game display. """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    drawTiles(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()