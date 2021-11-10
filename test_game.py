import sys
import unittest
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

