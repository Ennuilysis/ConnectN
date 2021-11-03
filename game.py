from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from typing import List, Tuple


class Game(object):
    def __init__(self, board_array: Board):
        self.board_array = board_array
        self.players: List[Tuple[str, str]] = []
        self.Player_instants: List[Player] = []
        self.board: Board = board
        self.pieces_to_win: int = pieces_to_win
        self.player_num = 0

    def create_player(self, player_num):
        self.player_num += 1
        player_name = self.check_player_name(player_num)
        player_piece = self.check_player_piece(player_num)
        self.players.append((player_name, player_piece))
        globals()[player_name] = Player(player_name, player_piece, self.player_num)
        self.Player_instants.append(globals()[player_name])

    def create_board(self, file):

    def check_player_name(self, player_num):
        x = [t[0] for t in self.players]
        while True:
            player_name = input(f"Player {player_num} enter your name")
            if len(player_name) == 0 or player_name == " ":
                print("Your name cannot be the empty string or whitespace")
                continue
            elif player_name in x:
                print(f'You cannot use {player_name} for your name as someone else is already using it.')
                continue
            return player_name

    def check_player_piece(self, player_num):
        x = [t[1] for t in self.players]
        while True:
            piece = input(f"Player {player_num} enter your piece")
            if len(piece) == 0 or piece == " ":
                print("Your piece cannot be the empty string or whitespace")
                continue
            elif len(piece) > 1:
                print(f'{piece} is not a single character. Your piece can only be a single character.')
                continue
            elif piece == self.board.blank_character:
                print('Your piece cannot be the same as the blank character.')
                continue
            elif piece in x:
                pos = x.index(piece)
                print(f'You cannot use {piece} for your piece as {self.players[pos][0]} is already using it.')
                continue
            return piece
