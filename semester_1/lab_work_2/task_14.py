"""
Task 14
@author: Alexandr Mazanik
"""
import time
import turtle


def main():
    turtle.shape('turtle')
    turtle.speed(2)

    a = 300                     #the length of the side of the star

    goto(50, 20)
    draw_star(a, 5)
    goto(-400, 20)
    draw_star(a, 11)


def draw_star(length, n):
    alpha = 180 - 180 / n
    for i in range(n):
        turtle.forward(length)
        turtle.right(alpha)


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

main()
time.sleep(2)