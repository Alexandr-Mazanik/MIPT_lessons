"""
Task 9
@author: Alexandr Mazanik
"""
import time
import math
import turtle


def main():
    turtle.shape('turtle')
    turtle.speed(5)
    turtle.penup()

    n = 10
    delta_r = 35

    for i in range(n):
        draw_polygon(i+3, delta_r)

    time.sleep(2)


def draw_polygon(num_of_sides, delta_r):
    r = delta_r * (num_of_sides - 2)
    alpha = 360 / num_of_sides
    length = calc_length(r, num_of_sides)

    turtle.forward(delta_r)
    turtle.left(0.5 * alpha + 90)
    turtle.pendown()

    for j in range(num_of_sides):
        turtle.forward(length)
        turtle.left(alpha)

    turtle.penup()
    turtle.right(90 + 0.5 * alpha)


def calc_length(r, num_of_sides):
    return r * 2 * math.sin(math.pi / num_of_sides)


main()
