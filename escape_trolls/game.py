import Maze

class Game():
    def __init__(self):
        self.game = Maze.Maze()
        self.game.print_maze()
        self.play()

    def play(self):
        self.welcome_screen()

        while not game.is_won():
            move = get_movement
    def welcome_screen(self):
        print( "Welcome to Escape the Trolls v0.1!" )

    def get_movement(self):
        movement = ''
        while movement not in 'udlr':
            movement = input( "Direction movement? (u, d, l, r)")
        return movement