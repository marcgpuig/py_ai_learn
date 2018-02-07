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
    def pos_in_board_bounds(x, y):
        '''Validates a board position'''
        return x < 3 and x >= 0 and y < 3 and y >= 0

    def set_value(self, x, y, value):
        '''Set a board cell and return true if completes the game'''
        if self.pos_in_board_bounds(x, y) and self.board[y][x] == ' ':
            self.board[y][x] = value
            return self.column_complete(x) or \
                self.row_complete(y) or \
                self.diagonal_complete()
        return False

    def set_x(self, x, y):
        '''Puts a X on a certain cell'''
        return self.set_value(x, y, 'X')

    def set_o(self, x, y):
        '''Puts a O on a certain cell'''
        return self.set_value(x, y, 'O')

    def row_complete(self, y):
        '''True if the row of position y is complete'''
        return self.board[y][0] == self.board[y][1] == self.board[y][2] != ' '

    def column_complete(self, x):
        '''True if the column of position x is complete'''
        return self.board[0][x] == self.board[1][x] == self.board[2][x] != ' '

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

b = Board()
b.set_x(0, 0)
b.set_x(0, 1)
b.set_x(0, 2)
b.set_o(1, 1)
b.set_o(1, 2)
b.set_o(1, 0)
print b
