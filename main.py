import turtle as jerry

def draw_flower(x, y, num_petals, petal_size, color, petal_length):
  """This function draws a flower using turtle graphics"""

  jerry.goto(x,y)
  jerry.pencolor(color)
  jerry.pensize(petal_size)

  #draw petals
  for _ in range(num_petals):
    jerry.forward(petal_length)
    jerry.backward(petal_length)
    jerry.right(360/num_petals)

  #draw center
  jerry.pencolor("orange")
  jerry.dot(50)


draw_flower(0,0,6,40,"pink", 100)
