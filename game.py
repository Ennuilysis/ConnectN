
    from ConnectNGame.src import board


class Game(object):
    def __init__(self, board_array: board.Board, pieces_to_win: int):
        self.board_array = board_array
        self.players = []
        self.board = board
        self.pieces_to_win = pieces_to_win

    def create_player1(self, player_num):
        enter_player = input(f"Player {player_num} enter your name")
        if len(enter_player) == 0:
            print("Your name cannot be the empty string or whitespace")
        self.players.append(enter_player)
        player1_piece = input(f"Player {player_num} enter your piece")

    def create_player2(self, player_num):
        second_player = input(f"Player {player_num} enter your name")
        if len(second_player) == 0:
            print("Your name cannot be the empty string or whitespace")
        if second_player == self.players[0]:
            print(f"you cannot use {second_player} for your name as someone else is already using it")

    ...
