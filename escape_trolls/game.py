import maze
import os

class Game():
    def __init__(self):
        self.game = maze.Maze()
        self.play()

    def play(self):
        self.welcome_screen()

        while not self.game.is_won():
            os.system('cls')
            self.game.print_maze()
            move = self.get_movement()
            self.game.move( move )

    def welcome_screen(self):
        print( "Welcome to Escape the Trolls v0.1!" )
        input()

    def get_movement(self):
        movement = 'x'
        while movement not in 'udlr':
            movement = input( "Direction movement? (u, d, l, r)")
        return movement