class Player(object):
    """ One of the players in the game. """
    _pieces = []
    _first = None

    def __init__(self, first:bool):
        """
        Initialise the player.

        Parameters
            first (bool): Determines whether the player goes first or not
        """
        self._first = first