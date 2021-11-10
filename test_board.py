import sys
import unittest
from unittest.mock import patch, mock_open
from ConnectNGame.src.board import Board
from ConnectNGame.src.config import Config
from ConnectNGame.src.game import Game


class TestBoard(unittest.TestCase):


    def test_drop_piece(self):
        test_contents = [['*', 'O', 'X', '*'],  # bottom?
                         ['*', 'X', 'O', '*'],
                         ['*', 'X', 'O', '*'],
                         ['X', '*', '*', '*']]  # top ?
        board = Board(4, 4, "*", 4)
        board.contents = test_contents

        answer_contents = [['*', 'O', 'X', '*'],  # bottom?
                           ['*', 'X', 'O', '*'],
                           ['X', 'X', 'O', '*'],
                           ['X', '*', '*', '*']]  # top ?
        board.drop_piece_into_column(0, 'X')

        self.assertEqual(board.contents, answer_contents)


if __name__ == '__main__':
    unittest.main()
