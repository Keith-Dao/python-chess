from pieces import Pieces
from board import Board

class Player(object):
    """ One of the players in the game. """

    def __init__(self, colour: int, board: Board) -> None:
        """
        Initialise the player.

        Parameters
            colour (int): The enum value of the player's colour
            board (Board): The board the player is playing on
        """
        self.colour = colour
        self.board = Pieces(colour, board)