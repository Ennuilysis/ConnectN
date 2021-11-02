from typing import List    

class Board(object):
    def __init__(self, num_rows: int, num_columns: int, blank_character: str):
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

    
    ...
