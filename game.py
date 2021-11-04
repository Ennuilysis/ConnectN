from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from ConnectNGame.src.config import Config
from typing import List, Tuple


class Game(Config):
    def __init__(self, pieces_to_win: int):
        self.players: List[Tuple[str, str]] = []
        self.Player_instants: List[Player] = []
        self.board: Board = Board.build_board_from_config()
        self.player_num = 0

    def create_player(self):
        self.player_num += 1
        player_name = self.check_player_name(self.player_num)
        player_piece = self.check_player_piece(self.player_num)
        self.players.append((player_name, player_piece))
        globals()[player_name] = Board(player_name, player_piece, self.player_num)
        self.Player_instants.append(globals()[player_name])

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
            elif piece == self.board.blank_character:
                print('Your piece cannot be the same as the blank character.')
                continue
            elif piece in x:
                pos = x.index(piece)
                print(f'You cannot use {piece} for your piece as {self.players[pos][0]} is already using it.')
                continue
            return piece

    def win_check(self, piece):
        board_list=self.board
        longest_vect=0
        def check_next(col, row, col_chng, row_chng):
            next_chr = board_list[col + col_chng][row + row_chng]
            if next_chr == piece:
                return 1 + check_next(col, row, col_chng, row_chng)
            else:
                return 0
        for col in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                if piece == self.board.contents[col][row]:
                    up_vect = check_next(col, row, 0, 1)
                    tor_right_vect = check_next(col, row, 1, 1)
                    right_vect = check_next(col, row, 1, 0)
                    bottom_right_vect = check_next(col, row, 0, 1)
                    longest_vect=max(up_vect,tor_right_vect,right_vect,bottom_right_vect,longest_vect)
        if longest_vect>=self.num_pieces_to_win:
            return False
