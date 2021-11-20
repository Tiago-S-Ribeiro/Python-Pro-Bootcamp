import colorgram
import turtle
import random

extracted_colors = colorgram.extract('20_001.jpeg', 20)
colors = []
valentino = turtle.Turtle()
turtle.colormode(255)
turtle.pensize(5)

for color in extracted_colors:
  red = color.rgb.r
  green = color.rgb.g
  blue = color.rgb.b

  if red < 220 and green < 220 and blue < 220:
    rgb_tuple = (red, green, blue)
    colors.append(rgb_tuple)

def reset_header():
  valentino.penup()
  valentino.right(180)
  valentino.forward(500)
  valentino.right(90)
  valentino.forward(50)
  valentino.right(90)
  valentino.pendown()

def random_color():
  return random.choice(colors)

def draw_line():
  for _ in range(10):
    valentino.dot(20, random_color())
    valentino.penup()
    valentino.forward(50)
    valentino.pendown()

for _ in range(10):
  draw_line()
  reset_header()