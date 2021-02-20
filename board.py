# Modules
import operator

# Files
from constants import *

class Board(object):
    """ Board the game is played on."""

    def __init__(self):
        """ Initialise an empty board with the correct dimensions. """
        self.board = [[None] * BOARD_WIDTH] * BOARD_HEIGHT

    def is_empty_coord(self, coord:(int, int)):
        """
        Check if the slot at the given coordinate is empty.

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot to be checked

        Returns:
            bool: True is slot is empty, otherwise false. If the coordinate is invalid, return false.
        """

        return self.is_in_bounds(coord) and self.get_piece(coord) is None

    def is_in_bounds(self, coord:(int, int)):
        """
        Checks if the given coordinate is in bounds.

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot to be checked
        
        Returns:
            bool: True if coordinate is in bounds, else false
        """
        x, y = coord
        return not (x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT)

    def get_piece(self, coord:(int, int)):
        """
        Gets the piece on the board at the given coordinate

        Parameters:
            coord ((int, int)): x- y-coordinate to get the piece from

        Returns:
            Piece / None: Piece at the coordinate or None if there is no piece
        """

        x, y = coord
        return self.board[y][x]

    def get_new_coord(self, coord:(int, int), direction:(int, int)):
        """
        Get the coordinate of the next position.

        Parameters:
            coord ((int, int)): current x- y-coordinate
            direction ((int, int)): x- y-direction of the the next move

        Returns:
            (int , int): new x- y-coordinate
        """
        return tuple(map(operator.add, coord, direction))
