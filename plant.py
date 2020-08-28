class Plant:
    """Create super-class Plant."""

    def __init__(self, x, y, num_protrusions, color, protrusion_size, protrusion_length):
        """Init super-class properties."""
        self.x = x
        self.y = y
        self.num_protrusions = num_protrusions
        self.color = color
        self.protrusion_size = protrusion_size
        self.protrusion_length = protrusion_length
        self.turn_degrees = 0

    def get_turn_degrees(self):
        """Will calculate the number of degrees jerry needs to turn."""
        self.turn_degrees = 360/self.num_protrusions
        return self.turn_degrees
