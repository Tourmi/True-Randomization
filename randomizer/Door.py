class Door:
    def __init__(self, room, x_block, z_block, direction_part, breakable):
        self.room = room
        self.x_block = x_block
        self.z_block = z_block
        self.direction_part = direction_part
        self.breakable = breakable