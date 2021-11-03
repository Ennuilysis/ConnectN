
class Player(object):
       def __init__(self, name, piece, number: int):
        self.num: int = number
        self.name: str = name
        self.piece: str = piece
        self.piece_locations=[] #[(col,row)]
