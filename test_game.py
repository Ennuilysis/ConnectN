import sys
import unittest

from ConnectNGame.src import game
from ConnectNGame.src.board import Board
from unittest.mock import patch
from ConnectNGame.src.game import Game
from ConnectNGame.src.config import Config
from ConnectNGame.test.fake_config import fake_config
from ConnectNGame.test.print_capturer import PrintCapturer


class TestGame(unittest.TestCase):
    def test_check_name_empty(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        user_input = ['', "Ian", "^"]
        capture = PrintCapturer()
        with patch("ConnectNGame.src.game.input", side_effect=user_input):
            with patch("ConnectNGame.src.game.print", side_effect=capture):
                connect_n.create_player()
                self.assertEqual("Your name cannot be the empty string or whitespace\n", capture.as_string())

    def test_name_already_used(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        user_input = ["Ian", "^", "Ian", "Bob", "$", "Bob", "@"]
        capture = PrintCapturer()
        with patch("ConnectNGame.src.game.input", side_effect=user_input):
            with patch("ConnectNGame.src.game.print", side_effect=capture):
                connect_n.create_player()
                connect_n.create_player()
                self.assertEqual("You cannot use Ian for your name as someone else is already using it.\n",
                                 capture.as_string())


    def test_piece_already_used(self):
        def test_name_already_used(self):
            game_config = fake_config(3, 3, 3, "*")
            connect_n = Game(game_config)
            user_input = ["Ian", "^", "Bob", "^", "Bob", "$"]
            capture = PrintCapturer()
            with patch("ConnectNGame.src.game.input", side_effect=user_input):
                with patch("ConnectNGame.src.game.print", side_effect=capture):
                    connect_n.create_player()
                    connect_n.create_player()
                    self.assertEqual("You cannot use ^ for your name as Ian is already using it.\n",
                                     capture.as_string())


        ...

    def test_piece_is_single_character(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        user_input = ["Ian", "&*^", "Ian", "$"]
        capture = PrintCapturer()
        with patch("ConnectNGame.src.game.input", side_effect=user_input):
            with patch("ConnectNGame.src.game.print", side_effect=capture):
                connect_n.create_player()
                self.assertEqual("&*^ is not a single character. Your piece can only be a single character.\n",
                                 capture.as_string())


        ...

    def test_piece_is_not_blank_character(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        user_input = ["Ian", "*", "Ian", "$"]
        capture = PrintCapturer()
        with patch("ConnectNGame.src.game.input", side_effect=user_input):
            with patch("ConnectNGame.src.game.print", side_effect=capture):
                connect_n.create_player()
                self.assertEqual("Your piece cannot be the same as the blank character.\n",
                                 capture.as_string())


    def test_create_player_list(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        answer = 1
        connect_n.create_player()
        self.assertEqual(answer, len(connect_n.Player_instants))


    def test_create_player_1(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        answer = connect_n.players
        connect_n.create_player()
        yesss = [('Ian', '#', 1)]
        self.assertEqual(answer, yesss)

    def test_create_player_2(self):
        game_config = fake_config(3, 3, 3, "*")
        connect_n = Game(game_config)
        answer = connect_n.players
        connect_n.create_player()
        connect_n.create_player()
        yesss = [('Ian', '@', 1), ('Bob', '$', 2)]
        self.assertEqual(answer, yesss)

#     def test_column_is_int(self):
#         game_config = fake_config(3, 3, 3, "*")
#         connect_n = Game(game_config)
#         user_input = ["Ian", "@", "Bob", "!", "F", "2", "2", "1"]
#         capture = PrintCapturer()
#         with patch("ConnectNGame.src.game.input", side_effect=user_input):
#             with patch("ConnectNGame.src.game.print", side_effect=capture):
#                 connect_n.create_player()
#                 connect_n.create_player()
#                 connect_n.play()
#                 self.assertEqual("Ian, column needs to be an integer, F is not an integer.\n", capture.as_string())
        ...

    def test_column_is_in_board(self):

        ...

    def test_col_is_full(self):
        ...

    def test_win_horizontal(self):
        ...

    def test_win_vertical(self):
        ...

#     def test_win_diagonal(self):
#         game_config = fake_config(3, 3, 3, "*")
#         connect_n = Game(game_config)
#         test_contents = [['X', 'X', 'X'],
#                          ['X', 'X', 'X'],
#                          ['X', 'X', 'X']]
#         connect_n.board.contents = test_contents
#         result = connect_n.win_check()
        ...




        # test_contents = [['*', '*', '*', '*'],  # bottom?
        #                  ['*', '*', '*', '*'],
        #                  ['*', '*', '*', '*'],
        #                  ['X', 'X', '*', 'X']]  # top ?
        # board = Board(3, 4, "*", 4)
        # board.contents = test_contents
        # answer_contents = [['*', 'O', 'X', '*'],  # bottom?
        #                    ['*', 'X', 'O', '*'],
        #                    ['X', 'X', 'O', '*'],
        #                    ['X', 'X', 'X', 'X']]  # top ?
        # Game.win_check(answer_contents, "X", "Ian")




if __name__ == '__main__':
    unittest.main()

