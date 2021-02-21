# Modules
import operator
from typing import List, Tuple, Dict

# Files
from constants import BOARD_HEIGHT, BOARD_WIDTH, Colours

# Exceptions
from exceptions import EmptyCoordinateException

# Board type
class BoardType(object):
    """ Generic board to allow for compilation. """
    pass

# Type of pieces
class Piece(object):
    """ A generic piece on the board """
    MOVES = []

    def __init__(self, x: int, y: int, colour: int, board: BoardType) -> None:
        """
        Initialise the generic piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
            colour (int): Enum value of the piece's colour
            board (BoardType): Board the piece is on
        """
        self.x: int = x
        self.y: int = y
        self.colour: int = colour
        self.captured: bool = False
        self.moved: bool = False
        self.board = board

    def get_coord(self) -> (int, int):
        """ 
        Get the piece's coordinates.

        Returns:
            (int, int): x- y-coordinate of the piece
        """
        return (self.x, self.y)

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

    def get_colour(self) -> int:
        """
        Get the piece's colour.

        Returns:
            (int): Enum value of the piece's colour
        """
        return self.colour

    def has_moved(self) -> bool:
        """
        Checks whether the piece has moved.
        
        Returns:
            bool: True if piece has moved, else false
        """
        return self.moved

    def move(self, x: int, y: int) -> None:
        """ 
        Move the piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
        """
        self.x = x
        self.y = y
        self.moved = True
    
    def set_captured(self) -> None:
        """ Set the piece to be captured. """
        self.captured = True

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """ 
        Gets all the possible moves.

        Returns:
            list[tuple[int, int]]: Array of x- y-coordinates that the piece can move to
        """

        moves: List[Tuple[int, int]] = []
        for move in self.MOVES:
            moves += self.get_indefinite_moves(self.get_new_coord(self.get_coord(), move), move)
        return moves

    def validate_move(self, coord: (int, int)) -> bool:
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

    def validate_attack(self, coord: (int, int)) -> bool:
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
        
        try: 
            # Check that the piece is on the opposite team
            return self.board.get_piece(coord).get_colour() != self.colour
        except EmptyCoordinateException:
            # Piece does not exist
            return False

    def get_indefinite_moves(self, coord: (int, int), direction: (int, int)) -> List[Tuple[int, int]]:
        """ 
        Gets all the valid moves in a direction indefinitely till it is not valid.
        
        Parameters:
            coord ((int, int)): x- y-coordinate of the move to be validated
            direction ((int, int)): x- y-direction of the the next move

        Return:
            list[tuple[int, int]]: Array of x- y-coordinates that the piece can move to
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

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """ 
        Gets all the possible moves.

        Returns:
            list[tuple[int, int]]: Array of x- y-coordinates that the piece can move to
        """
        
        moves: List[Tuple[int, int]] = []

        # Regular move
        MOVE: Tuple[int, int] = (0, 1)
        coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), MOVE)
        if self.validate_move(coord):
            moves += coord

        # Starting move
        STARTING_MOVE: Tuple[int, int] = (0, 2)
        coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), STARTING_MOVE)
        if not self.has_moved() and self.validate_move(coord):
            moves += coord

        # Attacks
        ATTACKS: List[Tuple[int, int]] = [(-1, 1), (1, 1)]
        for attack in ATTACKS:
            coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), attack)
            if self.validate_attack(coord):
                moves += coord

        return moves


class Knight(Piece):
    """ The knight piece. """

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """ 
        Gets all the possible moves.

        Returns:
            list[tuple[int, int]]: Array of x- y-coordinates that the piece can move to
        """

        moves: List[Tuple[int, int]] = []

        # Regular move
        MOVES: List[Tuple[int, int]] = [(-1, -2), (-1, 2), (1, -2), (-1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
        for move in MOVES:
            coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), move)
            if self.validate_move(coord):
                moves += coord

        # Attacks
        for attack in MOVES:
            coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), attack)
            if self.validate_attack(coord):
                moves += coord

        return moves


class Queen(Piece):
    """ The queen piece. """

    MOVES: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class Bishop(Piece):
    """ The bishop piece. """

    MOVES: List[Tuple[int, int]] = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


class Rook(Piece):
    """ The rook piece. """

    MOVES: List[Tuple[int, int]] = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class King(Piece):
    """ The king piece. """

    MOVES: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (-1, 0)]

    def __init__(self, x: int, y: int, colour: int, board: BoardType) -> None:
        """
        Initialise the king piece.

        Parameters:
            x (int): x-coordinate (column) of the piece
            y (int): y-coordinate (row) of the piece
            colour (int): Enum value of the piece's colour
            board (BoardType): Board the piece is on
        """
        super().__init__(x, y, colour, board)
        self.checked: bool = False

    def validate_move(self, coord: (int, int)) -> bool:
        """
        Validate the move.

        Parameters:
            coord ((int, int)): x- y-coordinate of the move to be validated

        Returns:
            bool: True if the move is valid, else false
        """
       
        return super().validate_move(coord) and not self.is_coord_checked(coord)

    def validate_attack(self, coord: (int, int)) -> bool:
        """
        Validate the move.

        Parameters:
            coord ((int, int)): x- y-coordinate of the attack to be validated

        Returns:
            bool: True if the attack is valid, else false
        """
       
        return super().validate_attack(coord) and not self.is_coord_checked(coord)

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """
        Gets all the possible moves.

        Returns:
            list[tuple[int, int]]: Array of x- y-coordinates that the piece can move to
        """

        moves: List[Tuple[int, int]] = []
        # Regular moves and attacks
        for move in self.MOVES:
            coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), move)
            if self.validate_move(coord) or self.validate_attack(coord):
                moves += coord
        
        # Castling
        if not self.has_moved():
            CASTLES: Dict[Tuple[int, int], Tuple[int, int]] = { # Map rook's direction to king's final coordinate
                (-1, 0): (-2, 0),
                (1, 0): (2, 0)
            } 
            for rookMove, kingMove in CASTLES:
                rookCoord: Tuple[int, int] = self.get_new_coord(self.get_coord(), rookMove)
                
                try:
                    piece: Piece = self.board.get_piece_in_direction(rookCoord, rookMove)
                except EmptyCoordinateException:
                    continue

                if piece is Rook and not piece.has_moved():
                    coord: Tuple[int, int] = self.get_new_coord(self.get_coord(), kingMove)
                    if self.validate_move(coord):
                        moves += coord

        return moves

    def in_check(self) -> bool:
        """ 
        Checks if the king is still in check.

        Returns:
            bool: True if the king's current coordinate is in check.
        """
        return self.is_coord_checked(self.get_coord())

    def is_coord_checked(self, coord: (int, int)) -> bool:
        """
        Checks that the new coordinate does not place the king in check.

        Parameters:
            coord ((int, int)): x- y-coordinate to check for check

        Return:
            bool: True if the coordinate would put the king in check, else false
        """

        # Check for recursive pieces
        REC_DIRECTIONS: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for direction in REC_DIRECTIONS:
            try:
                piece: Piece = self.board.get_piece_in_direction(self.get_new_coord(coord, direction), direction)
            except EmptyCoordinateException:
                continue

            if piece is not None and coord in piece.get_possible_moves():
                return True
        
        # Check for knights
        KNIGHT_DIRECTIONS: List[Tuple[int, int]] = [(-1, -2), (-1, 2), (1, -2), (-1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

        for direction in KNIGHT_DIRECTIONS:
            try:
                piece: Piece = self.board.get_piece(self.get_new_coord(coord, direction))
            except EmptyCoordinateException:
                continue

            if piece is Knight:
                return True

        # Coordinate is clear
        return False
        

class Pieces(object):
    """ Collection of pieces. """
    ROOK_COLUMNS: List[int] = [0, 7]
    KNIGHT_COLUMNS: List[int] = [1, 6]
    BISHOP_COLUMNS: List[int] = [2, 5]
    QUEEN_COLUMN: List[int] = 3
    KING_COLUMN: List[int] = 4

    def __init__(self, colour: int, board: BoardType) -> None:
        """
        Initialise player's pieces.

        Parameters:
            colour (int): Enum value of the piece's colour
            board (BoardType): Board the pieces are on
        """
        # Row number
        front: int = 1
        back: int = 0
        if colour == Colours.WHITE.value:
            front: int = BOARD_HEIGHT - 2
            back: int = BOARD_HEIGHT - 1

        # Front row pieces
        self.pawns: List[Pawn] = []
        for col in range(0, BOARD_WIDTH):
            self.pawns.append(Pawn(col, front, colour, board))

        # Back row pieces
        self.rooks: List[Rook] = []
        self.knights: List[Knight] = []
        self.bishops: List[Bishop] = []
        self.queens: List[Queen] = []
        
        # Rooks
        for col in self.ROOK_COLUMNS:
            self.rooks.append(Rook(col, back, colour, board))

        # Knights
        for col in self.KNIGHT_COLUMNS:
            self.knights.append(Knight(col, back, colour, board))

        # Bishops
        for col in self.BISHOP_COLUMNS:
            self.bishops.append(Bishop(col, back, colour, board))

        # Queen
        self.queens.append(Queen(self.QUEEN_COLUMN, back, colour, board))

        # King
        self.king: King = King(self.KING_COLUMN, back, colour, board)
        