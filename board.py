
class Board(object):

    def __init__(self, num_rows: int, num_columns: int, blank_character: str, pieces_to_win: int) -> None:
        self.pieces_to_win: int = pieces_to_win
        self.num_rows: int = num_rows
        self.num_columns: int = num_columns
        self.blank_character: str = blank_character
        self.contents: List[List[str]] = self.write_contents()

    def write_contents(self) -> List[List[str]]:
        contents = []
        for row in range(self.num_rows):
            new_row = []
            for element in range(self.num_columns):
                new_row.append(self.blank_character)
            contents.append(new_row)
        return contents

    def __str__(self) -> str:
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

    def fill_spot(self, row: int, column: int, character: str) -> None:
        self.contents[row][column] = character

    def drop_piece_into_column(self, column: int, piece: str) -> None:
        for row in reversed(self.contents):
            if row[column] == self.blank_character:
                row[column] = piece
                break

    @staticmethod
    def build_board_from_config(game_config: object) -> "Board":

        return Board(game_config.num_rows, game_config.num_columns, game_config.blank_character, game_config.num_pieces_to_win)  # type: ignore

    def is_full(self)->bool:
        for row in self.contents:
            for spot in row:
                if self.blank_character == spot:
                    return False
        return True
