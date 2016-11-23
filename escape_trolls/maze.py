import operator
import random
from player import Player

direction_key = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

maze = """#########################################################################
#   #               #               #           #                   #   #
#   #   #########   #   #####   #########   #####   #####   #####   #   #
#               #       #   #           #           #   #   #       #   #
#########   #   #########   #########   #####   #   #   #   #########   #
#       #   #               #           #   #   #   #   #           #   #
#   #   #############   #   #   #########   #####   #   #########   #   #
#   #               #   #   #       #           #           #       #   #
#   #############   #####   #####   #   #####   #########   #   #####   #
#           #       #   #       #   #       #           #   #           #
#   #####   #####   #   #####   #   #########   #   #   #   #############
#       #       #   #   #       #       #       #   #   #       #       #
#############   #   #   #   #########   #   #####   #   #####   #####   #
#           #   #           #       #   #       #   #       #           #
#   #####   #   #########   #####   #   #####   #####   #############   #
#   #       #           #           #       #   #   #               #   #
#   #   #########   #   #####   #########   #   #   #############   #   #
#   #           #   #   #   #   #           #               #   #       #
#   #########   #   #   #   #####   #########   #########   #   #########
#   #       #   #   #           #           #   #       #               #
#   #   #####   #####   #####   #########   #####   #   #########   #   #
#   #                   #           #               #               #   #
# X #####################################################################"""

class Maze():
    def __init__(self):
        self.create_maze()
        self.player = Player()
        self.set_initial_player_position()
        self.find_maze_exit()

    def create_maze(self):
        self.board = [list(line) for line in maze.split('\n')]

    def print_maze(self):
        for item in self.board:
            print( ''.join(item)  )

    def set_initial_player_position(self):
        random.seed()
        player_position = False
        while not player_position:
            column = random.randrange(0, len(self.board[0])-1)
            row = random.randrange(0, len(self.board)-1)

            if self.board[row][column] == ' ':
                self.board[row][column] = self.player.direction
                self.player.x_pos = column
                self.player.y_pos = row
                player_position = True

    def find_maze_exit(self):
        y_pos = 0
        for row in self.board:
            if 'X' in row:
                self.exit = [row.index('X'), y_pos]
            y_pos += 1


    def is_won(self):
        if self.player.position() is exit:
            return True
        return False

    def move(self, dir):
        position = self.player.position()

        new_pos = tuple(map(operator.add, position, direction_key[dir]))

        if '#' not in self.board[new_pos[1]][new_pos[0]]:
            self.player.set_position(new_pos)
            self.player.set_direction(dir)
            self.board[position[1]][position[0]] = ' '
            self.board[new_pos[1]][new_pos[0]] = self.player.facing()



