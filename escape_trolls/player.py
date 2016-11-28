from unit import Unit

direction = {
    "u" : "^",
    "d" : "V",
    "l" : "<",
    "r" : ">"
}

class Player( Unit ):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.direction = direction['d']

    def facing(self):
        return self.direction

    def set_direction(self, dir):
        self.direction = direction[dir]


        