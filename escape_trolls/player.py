
direction = {
    "u" : "^",
    "d" : "V",
    "l" : "<",
    "r" : ">"
}

class Player():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.direction = direction['d']

    def position(self):
        return (self.y_pos, self.x_pos)

    def facing(self):
        return self.direction

    def set_position(self, new_position):
        self.y_pos, self.x_pos = new_position

    def set_direction(self, dir):
        self.direction = direction[dir]


        