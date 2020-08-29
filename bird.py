"""Import random & turtle graphics."""
import random
import turtle as jerry

sc = jerry.Screen()
sc.setup = (400, 400)


class Bird:
    """Define bird class."""

    def __init__(self, color, width, beak_color):
        """Init properties of Bird."""
        self._x = random.randint(-250, 250)
        self._y = random.randint(-250, 250)
        self._wingspan = random.randint(45, 100)
        self._bodysize = random.randint(30, 70)
        self._beaksize = self._bodysize/4
        self.beak_color = beak_color
        self.width = width
        self.color = color

    def draw(self, x, y):
        """Draw bird."""
        jerry.penup()
        jerry.goto(self._x, self._y)
        jerry.pendown()
        jerry.pencolor(self.color)
        jerry.pensize(self.width)
        jerry.forward(self._bodysize)
        jerry.backward(self._bodysize/2)
        jerry.left(45)
        jerry.forward(self._wingspan)
        jerry.backward(self._wingspan)
        jerry.left(20)
        jerry.forward(self._wingspan)
        jerry.backward(self._wingspan)
        jerry.right(45)
        jerry.forward(self._bodysize)
        jerry.pensize(self.width/3)
        jerry.pencolor(self.beak_color)
        jerry.right(20)
        jerry.forward(self._beaksize)
        jerry.right(160)
        jerry.forward(self._beaksize)
        jerry.penup()

    def click_handler(self):
        """Handle click event."""
        jerry.onscreenclick(self.draw, 1)
