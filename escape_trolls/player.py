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

    def position(self):
        return super().position()

    def set_position(self, new_position, dir):
        self.y_pos, self.x_pos = new_position
        self.set_direction( dir )

    def set_direction(self, dir):
        self.direction = direction[dir]


        