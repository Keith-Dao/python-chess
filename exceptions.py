class EmptyCoordinateException(Exception):
    """
    Exception raised for attempting to get a piece in an empty coordinate.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, coord: (int, int)):
        """
        Initialise the empty coordinate exception.

        Parameters:
            coord ((int, int)): The empty x- y-coordinate
        """
        self.message = f'The coordinate {coord} is empty.'