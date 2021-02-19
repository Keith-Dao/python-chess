from constants import *

class Board(object):
    """ Board the game is played on."""

    def __init__(self):
        """ Initialise an empty board with the correct dimensions. """
        self.board = [[None] * BOARD_WIDTH] * BOARD_HEIGHT

    def is_empty_slot(self, coord:(int, int)):
        """
        Check if the slot at the given coordinate is empty.

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot to be checked

        Returns:
            bool: True is slot is empty, otherwise false. If the coordinate is invalid, return false.
        """
        
        # Check bounds
        x, y = coord
        if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT:
            return False

        # Check is empty
        return self.get_slot(coord) is None

    def get_slot(self, coord:(int, int)):
        """
        Gets the piece on the board at the given coordinate

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot

        Returns:
            Piece / None: Piece at the slot or None if there is no piece
        """

        x, y = coord
        return self.board[y][x]