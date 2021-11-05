from ConnectNGame.src.game import Game
from ConnectNGame.src.player import Player

game_master = Game()
game_board = game_master.board
empty_player = Player("", "piece", 1)


#####IGNORE ABOVE#######

def main() -> None:
    global game_master
    while True:
        game_master.create_player()
        game_master.create_player()
        playing = True
        while playing:
            for x in game_master.Player_instants:
                play_col = int(input(f"{x.name} please enter the column you want to play in: "))
                game_master.board.fill_spot(play_col, x.piece)
                playing=game_master.win_check(x.piece)
                winner=x.name
        print(f"{winner} won the game!")
        
        game_config = Config(sys.argv[1])
        connect_n = Game(game_config)
        Game.play(connect_n)


if __name__ == '__main__':
    main()
