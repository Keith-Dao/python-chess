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
        self.message: str = f'The coordinate {coord} is empty.'

class InvalidCoordinateException(Exception):
    """
    Exception raised for attempting to get an invalid coordinate.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, coord: (int, int)):
        """
        Initialise the empty coordinate exception.

        Parameters:
            coord ((int, int)): The invalid x, y position
        """
        self.message: str = f'There is no coordinate at (x,y): {coord}.'