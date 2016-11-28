from unit import Unit

class Troll( Unit ):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def position(self):
        return super().position()

    def set_position(self, new_position, dir = None):
        return super().set_position(new_position, dir)
     
    def facing(self):
        return 'T'