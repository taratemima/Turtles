
"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

def Backup(len):
  t.penup()
  t.backward(len)
  t.pendown()

def moveFwd(len):
  Backup(-1*len)
  
def Spiral(longestSide, angle):
  for i in range(longestSide, 5, -5):
    t.forward(i)
    t.right(angle)

Spiral(75, 45)
t.color("blue")
moveFwd(100)
#I used Backup rather than MoveFwd
Spiral(100, 90)
    


