"""
Task 7
@author: Alexandr Mazanik
"""
import time
import math
import turtle

turtle.shape('turtle')
turtle.radians()
turtle.speed(20)

alpha = math.pi/50          # коэффициент влияет на точночть счета
k = 1 / (2 * math.pi)       # коэффициент в формуле архимедовой сприали
length_0 = 25               # определяет размер и шаг (масштаб)
r_max = 300                 # радиус конечной спиарли

r = 0
i = 0
while r < r_max:
    length = length_0 * k * alpha**2 * i
    r = length / alpha
    turtle.forward(length)
    turtle.left(alpha)
    i += 1

time.sleep(2)
