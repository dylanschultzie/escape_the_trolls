import operator
import random
from player import Player
from troll import Troll

direction_key = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

troll_movement = {
    0: 'u',
    1: 'd',
    2: 'l',
    3: 'r'
}

TROLL = 'T'

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
        self.trolls = list()
        self.player = Player()
        self.set_initial_player_position()
        self.find_maze_exit()
        random.seed()


    def create_maze(self):
        self.board = [list(line) for line in maze.split('\n')]

    def print_maze(self):
        for item in self.board:
            print( ''.join(item)  )

    def set_initial_player_position(self):
        row, column = self.generate_random_position()
        self.player.y_pos = row
        self.player.x_pos = column
        self.board[row][column] = self.player.direction

    def set_initial_troll_position(self, difficulty):
        for troll in range(difficulty):
            trolls = Troll()
            row, column = self.generate_random_position()
            trolls.y_pos = row
            trolls.x_pos = column
            self.board[row][column] = 'T'
            self.trolls.append(trolls)

    def generate_random_position(self):
        while True:
            column = random.randrange(0, len(self.board[0])-1)
            row = random.randrange(0, len(self.board)-1)

            if self.board[row][column] == ' ':
                return (row, column)


    def find_maze_exit(self):
        y_pos = 0
        for row in self.board:
            if 'X' in row:
                self.exit = (y_pos, row.index('X'))
            y_pos += 1


    def is_won(self):
        if self.player.position() == self.exit:
            return True
        return False

    def generate_troll_movement(self):
        dir = random.randrange(0, 4)
        return troll_movement[dir]

    def move(self, dir = None, unit = None):
        if unit is None:
            unit = self.player

        if dir is None:
            dir = generate_direction()

        position = unit.position()

        column, row = tuple(map(operator.add, position, direction_key[dir]))

        new_board_position = self.board[column][row]

        if self.movement_valid((column, row)):
            if unit.position() == self.player.position():
                if unit is self.player:
                    #if player steps onto a troll, you lose
                    if unit.position() in [troll.position() for troll in self.trolls]:
                        return False

                else:
                    #if troll steps on player, you lose
                    if unit.position() == self.player.position():
                        return False

            if '#' not in new_board_position:
                unit.set_position((column, row), dir)
                self.board[position[0]][position[1]] = ' '
                self.board[column][row] = unit.facing()

            else:
                block_new_pos = tuple(map(operator.add, (column, row), direction_key[dir]))

                if self.movement_valid(block_new_pos):
                    new_block_position = self.board[block_new_pos[0]][block_new_pos[1]]

                    if '#' not in new_block_position:
                        self.board[position[0]][position[1]] = ' '
                        self.board[block_new_pos[0]][block_new_pos[1]] = '#'

                        if TROLL in new_block_position:
                            for alive_troll in self.trolls:
                                if alive_troll.position() == block_new_pos:
                                    self.trolls.remove(alive_troll)
                                    self.board[block_new_pos[0]][block_new_pos[1]] = '%'

                        unit.set_position((column, row), dir)
                        self.board[column][row] = unit.facing()

        return True

    def trolls_move(self):
        for troll in self.trolls:
            dir = self.generate_troll_movement()
            self.move( dir, unit=troll )

    def movement_valid(self, position):
        if all( i > 0 for i in position):
            if position[0] < len(self.board) and position[1] < len(self.board[0]):
                return True
        return False



