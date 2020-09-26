"""
Task 12
@author: Alexandr Mazanik
"""
import time
import turtle


def preparation():
    turtle.left(180)
    turtle.penup()
    turtle.forward(400)
    turtle.right(90)
    turtle.pendown()


turtle.shape('turtle')
turtle.speed(5)
preparation()

n = 8
r_big = 60
r_small = 10

for i in range(n):
    turtle.circle(-r_big, 180)
    turtle.circle(-r_small, 180)

time.sleep(2)