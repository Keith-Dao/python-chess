# Modules
import random

# Files
from board import Board
from pieces import Pieces

class Player(object):
    """ One of the players in the game. """

    def __init__(self, colour: int, board: Board) -> None:
        """
        Initialise the player.

        Parameters
            colour (int): The enum value of the player's colour
            board (Board): The board the player is playing on
        """
        self.colour: int = colour
        self.pieces: Pieces = Pieces(colour, board)


class Bot(Player):
    """ Generic bot. """
    
    def move(self):
        """
        Abstract method.
        Generate a move.
        """
        pass


class RandBot(Bot):
    """ Bot that performs random moves. """

    def move(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """ 
        Randomly choose a possible move.

        Returns:
            tuple[tuple[int, int], tuple[int, int]]: tuple of starting coordinates and ending coordinates
        """
        possibleMoves = self.pieces.getAllMoves()
        return possibleMoves[random.randrange(0, len(possibleMoves))]


class SmartBot(Bot):
    """ Bot that strategically chooses moves. """
    def move(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Strategically choose the next move.

        Returns:
            tuple[tuple[int, int], tuple[int, int]]: tuple of starting coordinates and ending coordinates
        """
        pass
