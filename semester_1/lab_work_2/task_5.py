"""
Task 5
@author: Alexandr Mazanik
"""
import time
import math
import turtle

turtle.shape('turtle')
turtle.speed(5)

a0 = 30             # длина стороны первого квадрата
delta_a = 30        # изменение длины стороны квадрата
n = 10

a = a0
for i in range(n):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)

    turtle.penup()
    turtle.right(135)
    turtle.forward((delta_a / 2) * math.sqrt(2))
    turtle.left(135)
    turtle.pendown()

    a += delta_a

turtle.hideturtle()
time.sleep(2)