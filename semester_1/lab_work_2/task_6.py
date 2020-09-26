"""
Task 6
@author: Alexandr Mazanik
"""
import time
import turtle

n = int(input('enter the number of legs - '))
alpha = 360 / n
length = 150

turtle.shape('turtle')
turtle.speed(5)
for i in range(n):
    turtle.forward(length)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(length)
    turtle.left(180)
    turtle.left(alpha)
turtle.hideturtle()

time.sleep(2)