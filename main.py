"""Import turtle graphics under alias jerry."""
import turtle as jerry
from flower import Flower
from tree import Tree
from bird import Bird


jerry.speed(50)

flower = Flower(6, "pink", 25, 75)
flower.draw("orange")

small_flower = Flower(10, "orange", 20, 50)
small_flower.draw("pink")

smaller_flower = Flower(5, "blue", 20, 30)
smaller_flower.draw("green")

tree = Tree(4, "green", 30, 50)
tree.draw("brown", 30, 200)

small_tree = Tree(6, "yellow", 25, 30)
small_tree.draw("brown", 15, 50)

smaller_tree = Tree(3, "blue", 25, 25)
smaller_tree.draw("yellow", 15, 25)

jeffrey = Bird("black", 35, "yellow")
jeffrey.click_handler()

maggie = Bird("blue", 25, "orange")
maggie.click_handler()

alberto = Bird("green", 13, "red")
alberto.click_handler()


jerry.done()
