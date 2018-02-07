'''
Main Game file
'''


class Board(object):
    """docstring for Board"""

    def __init__(self):
        self.clear_board()

    def __str__(self):
        rows = [' ----------- \n', '| {} | {} | {} |\n', '|---+---+---|\n']
        order = [0, 1, 2, 1, 2, 1, 0]
        return ''.join([rows[i] for i in order]).format(*self.to_1d_array())

    def to_1d_array(self):
        '''Return a 1D array with the board information'''
        return [i for j in self.board for i in j]

    def clear_board(self):
        '''Empty the board'''
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    @staticmethod
    def pos_is_in_board(pos_x, pos_y):
        '''Validates a board position'''
        return pos_x < 3 and pos_x >= 0 and pos_y < 3 and pos_y >= 0

    def empty_cell(self, pos_x, pos_y):
        '''Return true if an specific cell is empty'''
        return self.board[pos_y][pos_x] == ' '

    def set_value(self, pos_x, pos_y, value):
        '''Set a board cell and return true if completes the game'''
        if self.pos_is_in_board(pos_x, pos_y) and self.empty_cell(pos_x, pos_y):
            self.board[pos_y][pos_x] = value
            return self.column_complete(pos_x) or \
                self.row_complete(pos_y) or \
                self.diagonal_complete()
        return False

    def set_x(self, pos_x, pos_y):
        '''Puts a X on a certain cell'''
        return self.set_value(pos_x, pos_y, 'X')

    def set_o(self, pos_x, pos_y):
        '''Puts a O on a certain cell'''
        return self.set_value(pos_x, pos_y, 'O')

    def row_complete(self, pos_y):
        '''True if the row of position y is complete'''
        return self.board[pos_y][0] == \
            self.board[pos_y][1] == self.board[pos_y][2] != ' '

    def column_complete(self, pos_x):
        '''True if the column of position x is complete'''
        return self.board[0][pos_x] == \
            self.board[1][pos_x] == self.board[2][pos_x] != ' '

    def diagonal_complete(self):
        '''True if one diagonal is complete'''
        return self.board[0][0] == \
            self.board[1][1] == \
            self.board[2][2] != ' ' or \
            self.board[0][2] == \
            self.board[1][1] == \
            self.board[2][0] != ' '


class Player(object):
    """docstring for Player"""

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.puntuation = 0


class AIPlayer(Player):
    """docstring for AIPlayer"""

    def __init__(self):
        super(AIPlayer, self, "AI").__init__()


class Game(object):
    """docstring for Game"""

    def __init__(self):
        self.player = 0
        self.board = Board()

    def __str__(self):
        return str(self.board)
