from constants import *
from board import Board

class Piece(object):
    """ A generic piece on the board """

    def __init__(self, x:int, y:int, colour:int, board:Board):
        """
        Initialise the generic piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
            colour (int): Enum value of the piece's colour
            board (Board): Board the piece is on
        """
        self.x = x
        self.y = y
        self.colour = colour
        self.captured = False
        self.moved = False
        self.board = board

    def move(self, x:int, y:int):
        """ 
        Move the piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
        """
        self.x = x
        self.y = y
        self.moved = True
    
    def set_captured(self):
        """ Set the piece to be captured. """
        self.captured = True

    def get_possible_moves(self):
        """ 
        Abstract method.
        Gets all the possible moves.

        Returns:
            [(x, y), ...]: Array of x- y-coordinates that the piece can move to
        """
        pass

    def validate_move(self, coord:(int, int)):
        """ 
        Checks that the move is valid.

        Returns:
            bool: Whether the move is valid
        """

        # Check bounds
        x, y = coord
        if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT:
            return False
        # Check space is not occupied
        return self.board.is_empty_slot(coord)