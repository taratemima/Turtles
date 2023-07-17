"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

#print("Hello, everyone")
def ShapeDraw(selectedColor, shapeLen, sides):
  t.color(selectedColor)
  try: 
    angle = 360/sides
    if(angle >= 180):
      t.penup()
      print("Not enough sides for a polygon. Use 3 sides or more.")
      t.pendown()
    else:
      for i in range(sides):
        t.forward(shapeLen)
        t.left(angle)
  except ZeroDivisionError as e:
    t.penup()
    print("No division by zero.")
    t.pendown()
#may need to make the angle check its own function 

def Backup(len):
  t.penup()
  t.backward(len)
  t.pendown()

def MoveFwd(len):
  Backup(-1*len)

def MultiShape(shapeLimit, sizeShape):
  t.pendown()
  MoveFwd(50)
  for j in range(shapeLimit):
    ShapeDraw("black", sizeShape, j)
    if(j>=3):
      MoveFwd(shapeLimit/j)
      t.right(360/shapeLimit)
      #MoveFwd(50)
      #Backup(50)

  #should have an error message for 0, 1, 2, apparently the if statement was not enough
MultiShape(10, 20) 
#ShapeDraw("green", 100, 2)
#Backup(50)
#ShapeDraw("yellow", 100, 1)
  
#ShapeDraw("blue",100, 3)
#this is meant to be a large blue triangle
#Backup(75)
#ShapeDraw("blue", 100, 4)
#Backup(120)
#ShapeDraw("red", 100, 4)
