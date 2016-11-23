
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
        return (self.x_pos, self.y_pos)


        