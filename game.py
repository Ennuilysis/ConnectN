
from ConnectNGame.src import board


class Game(object):
    def __init__(self, board_array: board.Board, pieces_to_win: int):
        self.board_array = board_array
        self.players = []
        self.board = board
        self.pieces_to_win = pieces_to_win

    def create_player(self, player_num):
        enter_player = input(f"Player {player_num} enter your name")
        self.players.append(enter_player)    
    ...
