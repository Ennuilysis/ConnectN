from typing import List


class Board(object):

    def __init__(self, num_rows: int, num_columns: int, blank_character: str, pieces_to_win: int):
        self.pieces_to_win = pieces_to_win
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.blank_character = blank_character
        self.contents = self.write_contents()

    def write_contents(self) -> List[List[str]]:
        contents = []
        for row in range(self.num_rows):
            new_row = []
            for element in range(self.num_columns):
                new_row.append(self.blank_character)
            contents.append(new_row)
        return contents

    def __str__(self):
        str_board = []
        col_headers = []
        for _ in range(self.num_columns):
            col_headers.append(str(_))

        col_headers = '  ' + ' '.join(col_headers)
        str_board.append(col_headers)

        for pos, row in enumerate(self.contents):
            new_string = str(pos) + ' ' + ' '.join(row)
            str_board.append(new_string)

        final_result = '\n'.join(str_board)

        return final_result

    def fill_spot(self, row: int, column: int, character: str):
        self.contents[row][column] = character

    def drop_piece_into_column(self, column, piece):
        for row in reversed(self.contents):
            if row[column] == self.blank_character:
                row[column] = piece
                break

    @staticmethod
    def build_board_from_config(game_config) -> "Board":

        return Board(game_config.num_rows, game_config.num_columns, game_config.blank_character,
                     game_config.num_pieces_to_win)


