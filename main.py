"""Import turtle graphics under alias jerry."""
import turtle as jerry
from plant import Plant
from flower import Flower
from tree import Tree


flower = Flower(0, 0, 6, "pink", 40, 100)
flower.draw("orange")

tree = Tree(50, -50, 4, "green", 30, 50)
tree.draw("brown", 30, 200)

jerry.done()
