"""Import turtle graphics under alias jerry."""
import turtle as jerry
from plant import Plant


class Tree(Plant):
    """Define Tree class."""

    def __init__(self, num_protrusions, color, protrusion_size, protrusion_length):
        """Init inherited properties."""
        super().__init__(num_protrusions, color, protrusion_size, protrusion_length)
        self.iteration = 1

    def get_turn_degrees(self):
        """Override Plant class get_turn_degrees."""
        self.turn_degrees = 180/self.num_protrusions
        return self.turn_degrees

    def draw(self, trunk_color, trunk_size, height):
        """Draw tree."""
        #call get_turn_degrees
        self.get_turn_degrees()
        #draw trunk
        jerry.goto(self.x, self.y)
        jerry.pendown()
        jerry.pencolor(trunk_color)
        jerry.pensize(trunk_size)
        jerry.left(90)
        jerry.forward(height)

        #draw leaves
        jerry.pencolor(self.color)
        jerry.pensize(self.protrusion_size)
        while self.iteration < 4:
            for _ in range(self.num_protrusions):
                jerry.right(self.turn_degrees)
                jerry.forward(self.protrusion_length)
                jerry.backward(self.protrusion_length)
                jerry.left(self.turn_degrees)
                jerry.forward(self.protrusion_length)
                self.iteration += 1
        jerry.right(90)
        jerry.penup()
