from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from ConnectNGame.src.config import Config
from typing import List, Tuple, Union


class Game(object):
    def __init__(self, game_config: Config):
        self.players: List[Tuple[str, str, int]] = []
        self.board: Board = Board.build_board_from_config(game_config)
        self.Player_instants: List[Player] = []
        self.player_num = 0

    def create_player(self) -> None:
        self.player_num += 1
        player_name : str= self.check_player_name(self.player_num)
        player_piece : str = self.check_player_piece(self.player_num)
        self.players.append((player_name, player_piece, self.player_num))
        globals()[player_name] = Player(player_name, player_piece, self.player_num)
        self.Player_instants.append(globals()[player_name])

    def check_player_name(self, player_num) -> str:
        x = [t[0] for t in self.players]
        x = [t.lower() for t in x]

        while True:
            player_name = input(f"Player {player_num} enter your name: ")
            player_name_lower = player_name.lower()
            if len(player_name) == 0 or player_name == " ":
                print("Your name cannot be the empty string or whitespace")
                continue
            elif player_name_lower in x:
                print(f'You cannot use {player_name} for your name as someone else is already using it.')
                continue
            return player_name

    def check_player_piece(self, player_num) -> str:
        x = [t[1] for t in self.players]
        while True:
            piece = input(f"Player {player_num} enter your piece: ")
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

    def play(self):
        while True:
            self.create_player()
            self.create_player()
            print(self.board)
            while True:
                for x in self.Player_instants:
                    play_col : int= self.play_check(x.name) # type: ignore
                    self.board.drop_piece_into_column(play_col, x.piece)
                    print(self.board)
                    win = self.win_check(x.piece)
                    if win:
                        print(f"{x.name} won the game!")
                        quit()

    def play_check(self, player) -> Union[str]:
        col = self.board.num_columns
        while True:
            try:
                pos = input(f"{player}, please enter the column you want to play in: ")
                pos = int(pos)
            except:
                print(f'{player}, column needs to be an integer. {pos} is not an integer. ') # type: ignore
                continue
            if pos > col - 1 or pos < 0:
                print(f'Your column needs to be between 0 and {col - 1} but is actually {pos}.') # type: ignore
                continue
            x : List[str] = [t[pos] for t in self.board.contents]
            if self.board.blank_character not in x:
                print(f'You cannot play in {pos} because it is full.')
                continue
            break
        return pos

    def win_check(self, piece) -> bool:
        board_list: List[List[str]] = self.board.contents
        longest_vect = 0
        if self.board.blank_character not in self.board.contents[0]:
            print("Tie Game.")
            quit()

        def check_next(row: int, col: int, row_chng: int, col_chng: int) -> int:
            try:
                next_chr: str = board_list[row + row_chng][col + col_chng]
            except IndexError:
                return 0

            if next_chr == piece:
                return 1 + check_next(row + row_chng, col + col_chng, row_chng, col_chng)
            else:
                return 0

        for col in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                if piece == self.board.contents[row][col]:
                    up_vect: int = check_next(row, col, 1, 0)
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, 1, -1)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect, longest_vect)
        if longest_vect >= self.board.pieces_to_win - 1:
            return True
        return False
