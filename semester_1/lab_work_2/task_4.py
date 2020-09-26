"""
Task 4
@author: Alexandr Mazanik
"""
import time
import turtle

num_of_rotate = 70
alpha = 360 / num_of_rotate
step = 10

turtle.shape('turtle')

for i in range(num_of_rotate):
    turtle.forward(step)
    turtle.left(alpha)

time.sleep(2)
