"""
Task 10
@author: Alexandr Mazanik
"""
import time
import turtle

turtle.shape('turtle')
turtle.speed(4)

radius = 100
n = 6
alpha = 360 / n

for i in range(n):
    turtle.circle(radius * (-1)**i)
    if (i + 1) % 2 == 0:
        turtle.left(alpha)

time.sleep(2)