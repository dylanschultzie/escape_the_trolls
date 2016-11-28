class Unit( object ):
    def __init__(self):
        raise NotImplementedError("Must implement init method")

    def position(self):
        return (self.y_pos, self.x_pos)

    def set_position(self, new_position, dir = None):
        self.y_pos, self.x_pos = new_position

    def facing(self):
        raise NotImplementedError("Implement facing method")