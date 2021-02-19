class Piece(object):
    """ A generic piece on the board """

    def __init__(self, x:int, y:int, colour:int):
        """
        Initialise the generic piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
            colour (int): Enum value of the piece's colour
        """
        self.x = x
        self.y = y
        self.colour = colour