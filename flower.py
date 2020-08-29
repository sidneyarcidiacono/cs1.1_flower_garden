"""Import turtle graphics under alias jerry."""
import turtle as jerry
from plant import Plant


class Flower(Plant):
    """Flower class creates flower."""

    def __init__(self, num_protrusions, color, protrusion_size, protrusion_length):
        """Initialize flower properties."""
        super().__init__(num_protrusions, color, protrusion_size, protrusion_length)
        self.turn_degrees = 0

    def draw(self, center_color):
        """Will draw the flower."""
        #call get_turn_degrees, use return value
        self.get_turn_degrees()
        #draw petals
        jerry.penup()
        jerry.goto(self.x, self.y)
        jerry.pendown()
        jerry.pencolor(self.color)
        jerry.pensize(self.protrusion_size)
        for _ in range(self.num_protrusions):
            jerry.forward(self.protrusion_length)
            jerry.backward(self.protrusion_length)
            jerry.right(self.turn_degrees)

        #draw center
        jerry.pencolor(center_color)
        jerry.dot(self.protrusion_length/2)
        jerry.penup()
