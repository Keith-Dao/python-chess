# Modules
import operator

# Files
from constants import BOARD_HEIGHT, BOARD_WIDTH
from pieces import Piece

# Exceptions
from exceptions import EmptyCoordinateException

class Board(object):
    """ Board the game is played on."""

    def __init__(self) -> None:
        """ Initialise an empty board with the correct dimensions. """
        self.board = [[None] * BOARD_WIDTH] * BOARD_HEIGHT

    def is_empty_coord(self, coord: (int, int)) -> bool:
        """
        Check if the slot at the given coordinate is empty.

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot to be checked

        Returns:
            bool: True is slot is empty, otherwise false. If the coordinate is invalid, return false.
        """

        return self.is_in_bounds(coord) and self.get_piece(coord) is None

    def is_in_bounds(self, coord: (int, int)) -> bool:
        """
        Checks if the given coordinate is in bounds.

        Parameters:
            coord ((int, int)): x- y-coordinate of the slot to be checked
        
        Returns:
            bool: True if coordinate is in bounds, else false
        """
        x, y = coord
        return not (x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT)

    def get_piece(self, coord: (int, int)) -> Piece:
        """
        Gets the piece on the board at the given coordinate

        Parameters:
            coord ((int, int)): x- y-coordinate to get the piece from

        Returns:
            Piece: Piece at the coordinate
        
        Raises:
            EmptyCoordinateException: If there is no piece at the coordinate
        """

        x, y = coord
        if self.board[y][x] is None:
            raise EmptyCoordinateException(coord)
        return self.board[y][x]

    def get_new_coord(self, coord: (int, int), direction: (int, int)) -> (int, int):
        """
        Get the coordinate of the next position.

        Parameters:
            coord ((int, int)): current x- y-coordinate
            direction ((int, int)): x- y-direction of the the next move

        Returns:
            (int , int): new x- y-coordinate
        """
        return tuple(map(operator.add, coord, direction))

    def get_piece_in_direction(self, coord:(int, int), direction:(int, int)) -> Piece:
        """ 
        Recursively checks for a piece in a given direction.

        Parameters:
            coord ((int, int)): x- y-coordinate to check for a piece
            direction ((int, int)): x- y-direction to check for if there is not piece

        Returns:
            Piece: First piece to be found

        Raises:
            EmptyCoordinateException: If there is no piece at the coordinate
        """
        
        # Check bounds
        if not self.is_in_bounds(coord):
            raise EmptyCoordinateException

        # Get the piece
        try:
            return self.get_piece(coord)
        except EmptyCoordinateException:
            return self.get_piece_in_direction(self.get_new_coord(coord, direction), direction)
