# Modules
import operator

# Files
from constants import *
from board import Board

class Piece(object):
    """ A generic piece on the board """
    MOVES = []

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

    def get_coord(self):
        """ 
        Get the piece's coordinates.

        Returns:
            ((int, int)): x- y-coordinate of the piece
        """
        return (self.x, self.y)

    def get_new_coord(self, coord:(int, int), direction:(int, int)):
        """
        Get the coordinate of the next position.

        Parameters:
            coord ((int, int)): current x- y-coordinate
            direction ((int, int)): x- y-direction of the the next move

        Returns:
            (int , int): new x- y-coordinate
        """
        return tuple(map(operator.add, coord, direction))

    def get_colour(self):
        """
        Get the piece's colour.

        Returns:
            (int): Enum value of the piece's colour
        """
        return self.colour

    def has_moved(self):
        """
        Checks whether the piece has moved.
        
        Returns:
            bool: True if piece has moved, else false
        """
        return self.moved

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
        Gets all the possible moves.

        Returns:
            [(x, y), ...]: Array of x- y-coordinates that the piece can move to
        """

        moves = []
        for move in self.MOVES:
            moves += self.get_indefinite_moves(self.get_new_coord(self.get_coord(), move), move)
        return moves

    def validate_move(self, coord:(int, int)):
        """ 
        Checks that the move is valid.

        Parameters:
            coord ((int, int)): x- y-coordinate of the move to be validated

        Returns:
            bool: True if the move is valid, else false
        """

        # Check bounds
        x, y = coord
        if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT:
            return False
        # Check space is not occupied
        return self.board.is_empty_coord(coord)

    def validate_attack(self, coord:(int, int)):
        """ 
        Checks that the attack is valid.

        Parameters:
            coord ((int, int)): x- y-coordinate of the attack to be validated

        Returns:
            bool: True if the attack is valid, else false
        """

        # Check bounds
        x, y = coord
        if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT:
            return False
        # Check space is occupied by an opposing piece
        return not self.board.is_empty_coord(coord) and self.board.get_piece(coord).get_colour() != self.colour

    def get_indefinite_moves(self, coord:(int, int), direction:(int, int)):
        """ 
        Gets all the valid moves in a direction indefinitely till it is not valid.
        
        Parameters:
            coord ((int, int)): x- y-coordinate of the move to be validated
            direction ((int, int)): x- y-direction of the the next move

        Return:
            [(x, y)]: Array of x- y-coordinates that the piece can move to
        """

        # Check that the queen can attack and stop checking
        if self.validate_attack(coord):
            return [coord]
        # Check that the current move is valid and continue checking
        if self.validate_move(coord):
            return [coord] + self.get_indefinite_moves(self.get_new_coord(coord, direction), direction)
        # Current coordinate is invalid
        return []


class Pawn(Piece):
    """ The pawn piece. """  

    def get_possible_moves(self):
        """ 
        Gets all the possible moves.

        Returns:
            [(x, y)]: Array of x- y-coordinates that the piece can move to
        """
        
        moves = []

        # Regular move
        MOVE = (0, 1)
        coord = self.get_new_coord(self.get_coord(), MOVE)
        if self.validate_move(coord):
            moves += coord

        # Starting move
        STARTING_MOVE = (0, 2)
        coord = self.get_new_coord(self.get_coord(), STARTING_MOVE)
        if not self.has_moved() and self.validate_move(coord):
            moves += coord

        # Attacks
        ATTACKS = [(-1, 1), (1, 1)]
        for attack in ATTACKS:
            coord = self.get_new_coord(self.get_coord(), attack)
            if self.validate_attack(coord):
                moves += coord

        return moves


class Knight(Piece):
    """ The knight piece. """

    def get_possible_moves(self):
        """ 
        Gets all the possible moves.

        Returns:
            [(x, y)]: Array of x- y-coordinates that the piece can move to
        """

        moves = []

        # Regular move
        MOVES = [(-1, -2), (-1, 2), (1, -2), (-1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
        for move in MOVES:
            coord = self.get_new_coord(self.get_coord(), move)
            if self.validate_move(coord):
                moves += coord

        # Attacks
        for attack in MOVES:
            coord = self.get_new_coord(self.get_coord(), attack)
            if self.validate_attack(coord):
                moves += coord

        return moves


class Queen(Piece):
    """ The queen piece. """

    MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class Bishop(Piece):
    """ The bishop piece. """

    MOVES = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


class Rook(Piece):
    """ The rook piece. """

    MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class King(Piece):
    """ The king piece. """

    MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (-1, 0)]

    def __init__(self, x:int, y:int, colour:int, board:Board):
        """
        Initialise the king piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
            colour (int): Enum value of the piece's colour
            board (Board): Board the piece is on
        """
        super().__init__(x, y, colour, board)
        self.checked = False

    def validate_move(self, coord:(int, int)):
        """
        Validate the move.

        Parameters:
            coord ((int, int)): x- y-coordinate of the move to be validated

        Returns:
            bool: True if the move is valid, else false
        """
       
        return super().validate_move(coord) and not self.is_coord_checked(coord)

    def validate_attack(self, coord:(int, int)):
        """
        Validate the move.

        Parameters:
            coord ((int, int)): x- y-coordinate of the attack to be validated

        Returns:
            bool: True if the attack is valid, else false
        """
       
        return super().validate_attack(coord) and not self.is_coord_checked(coord)

    def get_possible_moves(self):
        """
        Gets all the possible moves.

        Returns:
            [(x, y), ...]: Array of x- y-coordinates that the piece can move to
        """

        moves = []
        # Regular moves and attacks
        for move in self.MOVES:
            coord = self.get_new_coord(self.get_new_coord, move)
            if self.validate_move(coord) or self.validate_attack(coord):
                moves += coord
        
        # Castling
        if not self.has_moved():
            pass # TODO add logic

        return moves

    def is_coord_checked(self, coord:((int, int))):
        """
        Checks that the new coordinate does not place the king in check.

        Parameters:
            coord ((int, int)): x- y-coordinate to check for check

        Return:
            bool: True if the coordinate would put the king in check, else false
        """

        # Check for recursive pieces
        REC_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for direction in REC_DIRECTIONS:
            piece = self.board.get_piece_in_direction(self.get_new_coord(coord, direction), direction)
            if piece is not None and coord in piece.get_possible_moves():
                return True
        
        # Check for knights
        KNIGHT_DIRECTIONS = [(-1, -2), (-1, 2), (1, -2), (-1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

        for direction in KNIGHT_DIRECTIONS:
            piece = self.board.get_piece(self.get_new_coord(coord, direction))
            if piece is Knight:
                return True

        # Coordinate is clear
        return False
        
