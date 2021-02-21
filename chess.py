# Import modules
import pygame, sys
from typing import Tuple

# Files
from constants import *

# Functions
def drawTiles(screen: pygame.Surface) -> None:
    """
    Draw the tiles onto the game display.

    Parameters:
        screen (pygame.Surface): The game display
    """
    # Background / UI colour
    screen.fill((100,100,100))

    # Create checker board
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            x: int = UI_WIDTH + i * SQUARE_DIMENSIONS
            y: int = UI_HEIGHT + j * SQUARE_DIMENSIONS

            if (i + j) % 2 == Colours.WHITE.value:  
                colour: Tuple[int, int, int] = (255, 255, 255)
            else:
                colour: Tuple[int, int, int] = (0, 0, 0)
            pygame.draw.rect(screen, colour, (x, y, SQUARE_DIMENSIONS, SQUARE_DIMENSIONS))


def main() -> None:
    """ Setup the game display. """
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    drawTiles(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()