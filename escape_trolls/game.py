import maze
import os
import string



class Game():
    def __init__(self):
        self.game = maze.Maze()
        self.difficulty = None
        self.play()

    def play(self):
        self.welcome_screen()
        self.get_difficulty()
        self.game.set_initial_troll_position(self.difficulty)
        safe = True
        game_won = False

        while not game_won and safe:
            os.system('cls')
            self.game.print_maze()
            move = self.get_movement()
            safe = self.game.move( dir = move )
            self.game.trolls_move()

            if not game_won: 
                game_won = self.game.is_won()

        os.system('cls')

        if game_won is True:
            print('You won!')
        elif safe is False:
            print('The trolls got you. Bummer.')

    def welcome_screen(self):
        print( "Welcome to Escape the Trolls v0.2!" )
        input()

    def get_difficulty(self):
        difficulty = None
        while not difficulty or difficulty not in '1234':
            difficulty = input("How difficult? (1-4 where each number is # of trolls): ")

        self.difficulty = int(difficulty)

    def get_movement(self):
        movement = None
        while not movement or movement not in 'udlr':
            movement = input( "Direction movement? (u, d, l, r)")
        return movement