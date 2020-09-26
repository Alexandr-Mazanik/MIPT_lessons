"""
Task 13
@author: Alexandr Mazanik
"""
import time
import math
import turtle


def main():
    turtle.shape('turtle')
    turtle.speed(5)
    preparation()

    turtle.pensize(5)
    draw_circle(200, "yellow")

    turtle.left(110)
    turtle.forward(280)
    turtle.right(20)

    draw_circle(-30, "blue")

    turtle.right(90)
    turtle.forward(160)
    turtle.left(90)

    draw_circle(-30, "blue")

    turtle.left(110)
    turtle.forward(55)
    turtle.right(110)
    turtle.pendown()
    turtle.pensize(10)
    turtle.backward(100)
    turtle.penup()

    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    draw_arc(100)


def preparation():
    turtle.penup()
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.pendown()


def draw_circle(radius, color):
    turtle.color("black", color)
    num_of_rotate = 40
    alpha = 360 / num_of_rotate
    step = radius * alpha * math.pi / 180

    turtle.pendown()
    turtle.begin_fill()
    for i in range(num_of_rotate):
        turtle.forward(step)
        turtle.left(alpha)
    turtle.end_fill()
    turtle.penup()

def draw_arc(radius):
    turtle.color("red")
    num_of_rotate = 40
    alpha = 360 / num_of_rotate
    step = radius * alpha * math.pi / 180

    turtle.pendown()
    for i in range(int(num_of_rotate / 2)):
        turtle.forward(step)
        turtle.right(alpha)
    turtle.penup()

main()
time.sleep(2)