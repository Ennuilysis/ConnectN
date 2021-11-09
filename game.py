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
        player_name, player_piece= self.check_name_and_piece(self.player_num)
        self.players.append((player_name, player_piece, self.player_num))
        globals()[player_name] = Player(player_name, player_piece, self.player_num)
        self.Player_instants.append(globals()[player_name])

    def check_name_and_piece(self, player_num:int) -> str:
        x = [t[0] for t in self.players]
        x = [t.lower() for t in x]
        y = [t[1] for t in self.players]
        while True:
            player_name = input(f"Player {player_num} enter your name: ")
            player_name_lower = player_name.lower()
            if len(player_name) == 0 or player_name=="_":
                print("Your name cannot be the empty string or whitespace")
                continue
            elif len(player_name.replace(" ",""))==0:
                print("Your name cannot be the empty string or whitespace")
                continue
            elif player_name_lower in x:
                print(f'You cannot use {player_name} for your name as someone else is already using it.')
                continue
            piece = input(f"Player {self.player_num} enter your piece: ")
            if len(piece.replace(" ", "")) == 0:
                print("Your piece cannot be the empty string or whitespace")
                continue
            elif len(piece) > 1:
                print(f'{piece} is not a single character. Your piece can only be a single character.')
                continue
            elif piece == self.board.blank_character:
                print('Your piece cannot be the same as the blank character.')
                continue
            elif piece in y:
                pos = y.index(piece)
                print(f'You cannot use {piece} for your piece as {self.players[pos][0]} is already using it.')
            return player_name,piece

    def is_only_white_space(self,name):
        str
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
                    win = self.win_check(x.piece,x.name)
                    if win:
                        print(f"{x.name} won the game!")
                        quit()
                    if self.board.is_full():
                        print("Tie Game.")
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

    def win_check(self, piece,name) -> bool:
        board_list: List[List[str]] = self.board.contents
        longest_vect = 0
        def check_next(row: int, col: int, row_chng: int, col_chng: int) -> int:
            if row==-1 or col==-1:
                return 0
            try:
                next_chr: str = board_list[row][col]
            except IndexError:
                # print("problem")
                return 0
            if next_chr == piece:
                # print("{}", row, col, next_chr)
                return 1 + check_next(row + row_chng, col + col_chng, row_chng, col_chng)
            else:
                return 0

        for col in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                if piece == self.board.contents[row][col]:
                    #print("{}", row, col)
                    up_vect: int = check_next(row, col, -1, 0)
                    #print("topright")
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, -1, 1)
                    #print("!!!!",up_vect,top_right_vect,right_vect,bottom_right_vect)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect, longest_vect)
                    # print("?????",longest_vect)
        if longest_vect >= self.board.pieces_to_win:
            print(f"{name} won the game!")
            quit()

        return False
