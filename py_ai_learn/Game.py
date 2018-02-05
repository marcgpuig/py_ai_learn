class Board(object):
    """docstring for Board"""
    def __init__(self):
        self.clear()

    def __str__(self):
        row = ['| {} | {} | {} |\n', '|---+---+---|\n', ' ----------- \n']
        return row[2] + row[0].format(*self.board[0]) + row[1] + \
               row[0].format(*self.board[1]) + row[1] + \
               row[0].format(*self.board[2]) + row[2]

    def clear(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def pos_in_board_bounds(self, x, y):
        return x < 3 and x >= 0 and y < 3 and y >= 0

    def set_value(self, x, y, value):
        if self.pos_in_board_bounds(x, y) and self.board[y][x] == ' ':
            self.board[y][x] = value
            return self.column_complete(x) or \
                   self.row_complete(y) or \
                   self.diagonal_complete()
        return False

    def set_x(self, x, y):
        return self.set_value(x, y, 'X')

    def set_o(self, x, y):
        return self.set_value(x, y, 'O')

    def row_complete(self, y):
        return self.board[y][0] == self.board[y][1] == self.board[y][2] != ' '

    def column_complete(self, x):
        return self.board[0][x] == self.board[1][x] == self.board[2][x] != ' '

    def diagonal_complete(self):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
               self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '


class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.player = 0
        self.board = Board()

    def __str__(self):
        return str(self.board)

