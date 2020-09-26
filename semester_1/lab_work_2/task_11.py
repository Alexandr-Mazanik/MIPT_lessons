"""
Task 11
@author: Alexandr Mazanik
"""
import time
import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.left(90)

n = 10
radius_0 = 40
delta_radius = 10

radius = radius_0
for i in range(2*n):
    turtle.circle(radius * (-1)**i)
    if (i + 1) % 2 == 0:
        radius += delta_radius

time.sleep(2)
