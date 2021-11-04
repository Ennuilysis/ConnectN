from ConnectNGame.src.game import Game
from ConnectNGame.src.player import Player

game_master = Game()
game_board = game_master.board
empty_player = Player("", "piece", 1)


#####IGNORE ABOVE#######

def main() -> None:
    global game_master
    game_master.create_player()
    game_master.create_player()
    playing = True
    while playing:
        for x in game_master.Player_instants:
            play_col = int(input(f"{x.name} please enter the column you want to play in: "))
            game_master.board.fill_spot(play_col, x.piece)
            playing=game_master.win_check(x.piece)


if __name__ == '__main__':
    main()
