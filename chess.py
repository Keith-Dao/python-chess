# Import modules
import pygame, sys

# Files
from constants import *

# Exceptions
from exceptions import InvalidCoordinateException

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
                colour: tuple[int, int, int] = (255, 255, 255)
            else:
                colour: tuple[int, int, int] = (0, 0, 0)
            pygame.draw.rect(screen, colour, (x, y, SQUARE_DIMENSIONS, SQUARE_DIMENSIONS))

def getTileIndex(coord: tuple[int, int]) -> tuple[int, int]:
    """
    Convert the mouse position to a tile index.

    Parameters:
        coord ((int, int)): x- y-coordinate of the mouse on the screen
    
    Returns:
        (int, int): column, row index of the tile

    Raises:
        InvalidCoordinateException: When the coordinates provided is None or is attempting to click the UI
    """
    
    if coord == None:
        raise InvalidCoordinateException(coord)

    x, y = coord
    row: int = (y - UI_HEIGHT) // SQUARE_DIMENSIONS
    column: int = (x - UI_WIDTH) // SQUARE_DIMENSIONS

    if row < 0 or column < 0 or row >= BOARD_HEIGHT or column >= BOARD_WIDTH:
        raise InvalidCoordinateException(coord)

    return column, row



def main() -> None:
    """ Setup the game display. """
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    drawTiles(screen)

    
    mousePos = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousePos == pygame.mouse.get_pos():
                mousePos = None
        pygame.display.update()

if __name__ == "__main__":
    main()