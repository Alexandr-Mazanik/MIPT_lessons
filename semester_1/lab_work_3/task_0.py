"""
Task 0
@author: Alexandr Mazanik
"""
import random
import time
import turtle


def moving():
    turtle.left(random.randint(0, 360))
    turtle.forward(random.randint(0, l_max))


turtle.shape('turtle')
turtle.speed(3)

n = 60              # кол-во перемещений
l_max = 100         # максимальное смещение за ход

for i in range(n):
    moving()

time.sleep(2)
