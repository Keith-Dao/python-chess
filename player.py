class Player(object):
    """ One of the players in the game. """

    def __init__(self, colour:int):
        """
        Initialise the player.

        Parameters
            colour (int): The enum value of the player's colour
        """
        self.colour = colour
        self.setup_pieces()

    def setup_pieces(self):
        """ Gives the player all the starting pieces. """
        pass