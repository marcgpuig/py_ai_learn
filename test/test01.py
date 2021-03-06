import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from py_ai_learn.Game import Board


class TestBoard(unittest.TestCase):
    """docstring for TestBoard"""

    def test_clear_board(self):
        b = Board()
        self.assertEqual(b.board, [[' ', ' ', ' '], [
                         ' ', ' ', ' '], [' ', ' ', ' ']])
        b.set_x(0, 0)
        b.set_o(2, 2)
        b.set_x(1, 1)
        b.set_o(0, 2)
        self.assertNotEqual(
            b.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        b.clear_board()
        self.assertEqual(b.board, [[' ', ' ', ' '], [
                         ' ', ' ', ' '], [' ', ' ', ' ']])

    def test_cell_empty(self):
        b = Board()
        b.set_x(0, 0)
        b.set_o(1, 1)
        b.set_x(2, 2)

        self.assertTrue(b.empty_cell(0, 1))
        self.assertTrue(b.empty_cell(1, 2))
        self.assertTrue(b.empty_cell(2, 0))

        self.assertFalse(b.empty_cell(0, 0))
        self.assertFalse(b.empty_cell(1, 1))
        self.assertFalse(b.empty_cell(2, 2))

    def test_pos_is_in_board(self):
        b = Board()
        self.assertTrue(b.pos_is_in_board(0, 0))
        self.assertTrue(b.pos_is_in_board(1, 1))
        self.assertTrue(b.pos_is_in_board(2, 2))
        self.assertTrue(b.pos_is_in_board(0, 2))
        self.assertTrue(b.pos_is_in_board(2, 0))

        self.assertFalse(b.pos_is_in_board(-1, 0))
        self.assertFalse(b.pos_is_in_board(0, -1))
        self.assertFalse(b.pos_is_in_board(0, 3))
        self.assertFalse(b.pos_is_in_board(3, 0))

    def test_row(self):
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(0, i))
            self.assertFalse(b.set_x(1, i))
            self.assertTrue(b.set_x(2, i))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(1, i))
            self.assertFalse(b.set_x(2, i))
            self.assertTrue(b.set_x(0, i))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(0, i))
            self.assertFalse(b.set_x(2, i))
            self.assertTrue(b.set_x(1, i))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(2, i))
            self.assertFalse(b.set_x(1, i))
            self.assertTrue(b.set_x(0, i))

    def test_column(self):
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(i, 0))
            self.assertFalse(b.set_x(i, 1))
            self.assertTrue(b.set_x(i, 2))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(i, 1))
            self.assertFalse(b.set_x(i, 2))
            self.assertTrue(b.set_x(i, 0))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(i, 0))
            self.assertFalse(b.set_x(i, 2))
            self.assertTrue(b.set_x(i, 1))
        for i in range(3):
            b = Board()
            self.assertFalse(b.set_x(i, 2))
            self.assertFalse(b.set_x(i, 1))
            self.assertTrue(b.set_x(i, 0))

if __name__ == '__main__':
    unittest.main()
