"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
#def Spiral(turns):
 # for i in range(turns):
  #  t.forward(5+i)
  #  t.right(15)
    #turtle.done()

#t.pendown()
t.color("black")
for k in range(240):
  t.forward(2+k/4)
  t.left(30 - k/12)

#Spiral(100)
#for c in ['red', 'green', 'blue', 'yellow']:
    #t.color(c)
    #t.forward(75)
    #t.left(90)
