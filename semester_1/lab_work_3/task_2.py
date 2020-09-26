"""
Task 2
@author: Alexandr Mazanik
"""
import time
import turtle


def main():
    x0, y0 = -400, -90           # initial coordinates of the ball
    v_x_0 = 10                   # initial Ox axis speed
    v_y_0 = 40                   # initial Oy axis speed
    a_y = -3                     # Oy acceleration
    d_t = 0.1                    # time step in calculations
    alpha = 0.8                  # speed loss on rebound
    remaining_jumps = 4          # number of jumps

    turtle.shape('circle')
    turtle.pensize(3)
    turtle.speed(6)

    draw_a_zero_line(x0, y0)

    coordinates = calc_coordinates(x0, y0, v_x_0, v_y_0, a_y, d_t,
                                   alpha, remaining_jumps)

    draw_a_trajectory(coordinates)


def draw_a_zero_line(x0, y0):
    turtle.penup()
    turtle.goto(-x0, y0)
    turtle.pendown()
    turtle.goto(x0, y0)


def calc_coordinates(x0, y0, v_x_0, v_y_0, a_y, d_t,
                     alpha, remaining_jumps):
    coord = [(x0, y0)]
    x, y = x0, y0
    v_x, v_y = v_x_0, v_y_0

    while remaining_jumps > 0:
        x += v_x * d_t
        y += v_y * d_t + a_y * d_t**2 / 2
        coord.append((x, y))
        if y < y0:
            v_y = -v_y * alpha
            remaining_jumps -= 1
        else:
            v_y += a_y * d_t

    return coord


def draw_a_trajectory(coordinates):
    for x, y in coordinates:
        turtle.goto(x, y)


main()

time.sleep(2)
