class Config:
    def __init__(self, path_to_config_file: str):
        with open(path_to_config_file) as file:
            for line in file:
                line = line.split(":")
                key, value = line
                key = key.strip()
                value = value.strip()
                if key == "num_rows":
                    self.num_rows = int(value)
                if key == "num_cols":
                    self.num_columns = int(value)
                if key == "blank_char":
                    self.blank_character = value
                if key == 'num_pieces_to_win':
                    self.num_pieces_to_win = int(value)
