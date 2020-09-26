"""
Task 3
@author: Alexandr Mazanik
"""
from random import randint
import math
import turtle


def main():
    number_of_turtles = 15
    max_speed = 5
    dt = 1
    steps_of_time_number = 400
    half_side_length = 350

    pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
    for unit in pool:
        unit.penup()

    draw_box(pool[0], half_side_length)

    init_coord, init_speed = rand_init_param(number_of_turtles, half_side_length, max_speed)
    coordinates = calc_coordinates(steps_of_time_number, number_of_turtles, dt,
                                   half_side_length, init_coord, init_speed
                                   )

    draw(pool, steps_of_time_number, coordinates)


def draw_box(painter, half_side_length):
    painter.hideturtle()
    painter.pensize(3)

    painter.penup()
    painter.goto(half_side_length, half_side_length)
    painter.pendown()

    painter.goto(half_side_length, -half_side_length)
    painter.goto(-half_side_length, -half_side_length)
    painter.goto(-half_side_length, half_side_length)
    painter.goto(half_side_length, half_side_length)

    painter.penup()
    painter.showturtle()


def rand_init_param(number_of_turtles, half_side_length, max_speed):
    coord = []
    speed = []
    for i in range(number_of_turtles):
        coord.append([])
        speed.append([])

        x0 = randint(-half_side_length, half_side_length)
        y0 = randint(-half_side_length, half_side_length)
        angle = deg_to_rad(randint(0, 360))
        v_x_0 = max_speed * math.cos(angle)
        v_y_0 = max_speed * math.sin(angle)
        coord[i] = [x0, y0]
        speed[i] = [v_x_0, v_y_0]

    return coord, speed


def deg_to_rad(angle):
    return angle * math.pi / 180


def calc_coordinates(steps_of_time_number, number_of_turtles, dt,
                     half_side_length, init_coord, init_speed
                     ):
    coordinates = []
    for i in range(number_of_turtles):
        coordinates.append([])
        x, y = init_coord[i]
        vx, vy = init_speed[i]
        coordinates[i].append([x, y])

        for j in range(steps_of_time_number):
            x += vx * dt
            y += vy * dt
            touching, side = touching_the_border(x, y, half_side_length)
            if touching:
                vx, vy = bounce_off(vx, vy, side)
            coordinates[i].append([x, y])

    return coordinates


def touching_the_border(x, y, half_side_length):
    if x < -half_side_length:
        return True, 3
    elif x > half_side_length:
        return True, 1
    elif y > half_side_length:
        return True, 2
    elif y < -half_side_length:
        return True, 4
    else:
        return False, -1


def bounce_off(vx, vy, side):
    if side == 1 or side == 3:
        return -vx, vy
    else:
        return vx, -vy


def draw(pool, steps_of_time_number, coord):
    for t in range(steps_of_time_number):
        i = 0
        for unit in pool:
            unit.goto(coord[i][t])
            i += 1


main()
