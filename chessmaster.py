#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Searching for Bobby Fischer"""

import time


class ChessPiece(object):
    """A moving chess piece.

    Args:
        position (string): the space the piece occupies in tile notation.

    Attributes:
        position (string): the space the piece occupies in tile notation.
        prefix (string): Default = ''
        moves (list): a list that stores tuples of info the piece's history of moves.
    """
    prefix = ''

    def __init__(self, position):
        self.position = position
        if not self.is_legal_move(self.position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.moves = []

    def algebraic_to_numeric(self, tile):
        """Converts tile notation to a tuple with a numeric y-coordinate
            and x-coordinate.

        Args:
            tile (alnum): alphanumeric tile position.
        """

        alphas = ['a','b','c','d','e','f','g','h']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8']

        if len(tile) == 2:
            if tile[0].lower() in alphas:
                if tile[1] in nums:
                    for i in range(8):
                        if tile[0] == alphas[i]:
                            tile_coord = ((int(nums[i]) - 1),int(tile[1]) - 1)
                else:
                    return None
            else:
                return None
        else:
            return None

        return tile_coord

    def is_legal_move(self, position):
        """Checks legality of a possible move.

        Args:
            position(string): the new position to which this piece should be moved,
            in tile notation.
        """

        legal = self.algebraic_to_numeric(position)

        if legal is None:
            return False
        else:
            return True

    def move(self, position):
        """Move the chesspiece if the position is legal, and record it.

        Args:
            position (string)= the position to move the piece to,
            in algebraic notation.
        """

        legal = self.is_legal_move(position)

        if legal:
            temp = self.position
            self.position = position
            move = (self.prefix + temp, self.prefix + self.position, time.time())
            self.moves.append(move)
            return move
        else:
            return False


class Rook(ChessPiece):
    """A moving castle of sorts.

    Args:
        position (string): the space the piece occupies in tile notation.

    Attributes:
        position (string): the space the piece occupies in tile notation.
        prefix (string): Default = 'R' for Rook
        moves (list): a list that stores tuples of info the piece's history of moves.
    """
    
    def __init__(self, position):
        self.position = position
        if not ChessPiece.is_legal_move(self, self.position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.moves = []
        self.prefix = 'R'
        
    def is_legal_move(self, position):
        """Checks legality of a possible move for Rooks.

        Args:
            position(string): the new position to which this piece should be moved,
            in tile notation.
        """

        legal = self.algebraic_to_numeric(position)

        if legal is None:
            return False
        elif legal == self.algebraic_to_numeric(
            self.position):
            return False
        elif legal[0] == self.algebraic_to_numeric(
            self.position)[0] or legal[1] == self.algebraic_to_numeric(
                self.position)[1]:
            return True
            


class Bishop(ChessPiece):
    """A man in a funny hat.

    Args:
        position (string): the space the piece occupies in tile notation.

    Attributes:
        position (string): the space the piece occupies in tile notation.
        prefix (string): Default = 'B' for bishop
        moves (list): a list that stores tuples of info the piece's history of moves.
    """

    def __init__(self, position):
        self.position = position
        if not ChessPiece.is_legal_move(self, self.position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.moves = []
        self.prefix = 'B'

    def is_legal_move(self, position):
        """Checks legality of a possible move for Bishops.

        Args:
            position(string): the new position to which this piece should be moved,
            in tile notation.
        """

        cur_pos = self.algebraic_to_numeric(self.position)
        legal = self.algebraic_to_numeric(position)
        possibles = []
        
        if legal is None:
            return False
        else:
            lsum = cur_pos[0] + cur_pos[1]
            rdiff = cur_pos[0] - cur_pos[1]
            for i in range(0, 7):
                if (i - rdiff) in range(8):
                    possibles.append((i, (i - rdiff)))
            for i in range(0, 7):
                if (lsum - i) in range(8):
                    possibles.append((i, (lsum - i)))
            if (legal in possibles) and (legal != cur_pos):
                return True
            else:
                return False


class King(ChessPiece):
    """A slow, or lazy, man.

    Args:
        position (string): the space the piece occupies in tile notation.

    Attributes:
        position (string): the space the piece occupies in tile notation.
        prefix (string): Default = 'B' for bishop
        moves (list): a list that stores tuples of info the piece's history of moves.
    """

    def __init__(self, position):
        self.position = position
        if not ChessPiece.is_legal_move(self, self.position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.moves = []
        self.prefix = 'K'

    def is_legal_move(self, position):
        """Checks legality of a possible move for the King.

        Args:
            position(string): the new position to which this piece should be moved,
            in tile notation.
        """

        cur_pos = self.algebraic_to_numeric(self.position)
        legal = self.algebraic_to_numeric(position)
        possibles = []
        
        if legal is None:
            return False
        else:
            for i in range(cur_pos[0] - 1, cur_pos[0] + 2):
                for j in range(cur_pos[1] - 1, cur_pos[1] + 2):
                    possibles.append((i,j))
            if (legal in possibles) and (legal != cur_pos):
                return True
            else:
                return False


class ChessMatch(object):
    """

    Args:
        pieces (dict): a dictionary of pieces keyed by their positions on the board.
            Default = None
    """

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
            
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        self.log = []
        self.pieces = {
            'Ra1': Rook('a1'),
            'Rh1': Rook('h1'),
            'Ra8': Rook('a8'),
            'Rh8': Rook('h8'),
            'Bc1': Bishop('c1'),
            'Bf1': Bishop('f1'),
            'Bc8': Bishop('c8'),
            'Bf8': Bishop('f8'),
            'Ke1': King('e1'),
            'Ke8': King('e8'),
            }

    def move(self, piece_full_name, position):
        piece = self.pieces[piece_full_name]
        if piece.move(position) == False:
            return False
        else:
            self.log.append(piece.move(position))
            self.pieces[piece_full_name[0] + position] = self.pieces.pop(piece_full_name)

    def __len__(self):
        return len(self.log)
        
