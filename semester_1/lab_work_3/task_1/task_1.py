"""
Task 1
@author: Alexandr Mazanik
"""
import time
import turtle


def main():
    turtle.shape('turtle')
    turtle.pensize(5)
    turtle.speed(5)
    preparation()

    index = '141700'                # индекс
    delta_l = 30                    # расстояние между цифрами
    length = 100                    # длина палочки в цифре

    data = read_data()

    draw_index(data, index, delta_l, length)

    turtle.hideturtle()


def preparation():
    turtle.penup()
    turtle.left(180)
    turtle.forward(400)             # расстояние от центра т. начала рисования
    turtle.left(180)
    turtle.pendown()


def indent(delta_l):
    turtle.penup()
    turtle.forward(delta_l)
    turtle.pendown()


def read_data():
    with open('figures', 'r') as data_file:
        data = []
        i = -1
        for line in data_file:
            if line == '***\n':
                i += 1
                data.append([])
                continue
            data[i].append(tuple(map(float, line.split(','))))

    return data


def draw_index(data, index, delta_l, length):
    for number in index:
        indent(delta_l)
        draw_number(data, length, int(number))


def draw_number(data, length, number):
    for coord in data[number]:
        turtle.pendown()

        pen, step, angle = coord

        if not pen:
            turtle.penup()

        turtle.left(angle)
        turtle.forward(step * length)


main()
time.sleep(2)
