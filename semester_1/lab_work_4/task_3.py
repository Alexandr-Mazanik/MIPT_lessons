import pygame
from pygame.draw import *
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
PEN_WIDTH = 3
FPS = 10

WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
CAR_COLOR = (255, 0, 0)
ROAD_COLOR = (183, 200, 196)
SIDEWALK_COLOR = (180, 200, 240)
SKY_COLOR = (210, 210, 140)
CLOUD_COLOR = (0, 70, 70, 100)
HOUSE_COLORS = [
    (111, 145, 138),
    (183, 200, 196),
    (147, 169, 170),
    (147, 172, 167),
    (123, 154, 167),
    (146, 135, 117),
    (186, 172, 137),
    (134, 164, 154),
    (124, 184, 125),
    (186, 165, 156),
    (135, 138, 132),
    (184, 137, 167)
]


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    draw_scene(screen)

    pygame.display.update()

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_scene(screen):
    sky_height = draw_background(screen)
    number_of_houses = 8

    car_sizes = [
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7),
        (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 11),
        (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 10),
        (SCREEN_WIDTH // 7, SCREEN_HEIGHT // 17),
        (SCREEN_WIDTH // 7, SCREEN_HEIGHT // 17)
    ]
    car_positions = [
        (int(0.47 * SCREEN_WIDTH), 17 * SCREEN_HEIGHT // 20),
        (SCREEN_WIDTH // 20, 18 * SCREEN_HEIGHT // 20),
        (SCREEN_WIDTH // 2, 15 * SCREEN_HEIGHT // 20),
        (SCREEN_WIDTH // 4, 17 * SCREEN_HEIGHT // 20),
        (SCREEN_WIDTH // 24, 13 * SCREEN_HEIGHT // 17)
    ]

    draw_houses(screen, number_of_houses, sky_height)

    cars, smokes = make_a_car(car_sizes)
    draw_a_car(screen, cars, smokes, car_positions)


def draw_background(screen):
    """
    Draws the scene background of two colors
    :param screen: active screen
    :return: height of the sky on the background
    """
    sky_height = 2 * SCREEN_HEIGHT // 3
    earth_height = SCREEN_HEIGHT - sky_height

    rect(screen, SKY_COLOR, (0, 0, SCREEN_WIDTH, sky_height))
    rect(screen, SIDEWALK_COLOR, (0, sky_height, SCREEN_WIDTH, earth_height))
    rect(screen, BLACK, (0, sky_height - 20, SCREEN_WIDTH, 40))

    return sky_height


def draw_houses(screen, number_of_houses, sky_height):
    houses_width = SCREEN_WIDTH // 5
    houses_height = sky_height
    clouds_width = 2 * SCREEN_WIDTH // 3
    clouds_height = sky_height // 4

    houses_coord_range = estimate_range_coord(sky_height, houses_width, houses_height)
    clouds_coord_range = estimate_range_coord(sky_height, clouds_width,
                                              clouds_height, is_house=False
                                              )

    house_coordinates = rand_house_coord(houses_coord_range, number_of_houses)

    cloud = make_a_cloud(clouds_width, clouds_height)
    for x, y in house_coordinates:
        draw_cloud(screen, clouds_coord_range, cloud)

        used_house_color_number = randint(0, len(HOUSE_COLORS) - 1)
        color = HOUSE_COLORS[used_house_color_number]

        rect(screen, color, (x, y, houses_width, houses_height))
        rect(screen, BLACK, (x, y, houses_width, houses_height), PEN_WIDTH)


def estimate_range_coord(sky_height, width, height, is_house=True):
    x_min = -width // 2
    x_max = SCREEN_WIDTH - width // 2
    y_min = sky_height // 20
    if is_house:
        y_max = (2 * sky_height + SCREEN_HEIGHT) // 3 - height
    else:
        y_max = sky_height - 3 * height // 2

    return x_min, x_max, y_min, y_max


def rand_house_coord(coord_range, quantity):
    x_min, x_max, y_min, y_max = coord_range

    step_y = (y_max - y_min) // quantity
    coordinates = []
    for i in range(quantity):
        coordinates.append([])
        y_min += step_y
        coordinates[i].append(randint(x_min, x_max))
        coordinates[i].append(randint(y_min, y_max))

    return coordinates


def make_a_cloud(width, height):
    cloud = pygame.Surface((width, height), pygame.SRCALPHA)
    cloud.fill(WHITE)
    ellipse(cloud, CLOUD_COLOR, cloud.get_rect())

    return cloud


def draw_cloud(screen, coordinates_range, cloud):
    x_min, x_max, y_min, y_max = coordinates_range

    x = randint(x_min, x_max)
    y = randint(y_min, y_max)

    screen.blit(cloud, (x, y))


def draw_a_car(screen, cars, smokes, positions):
    for car, smoke, position in zip(cars, smokes, positions):
        x, y = position

        screen.blit(car, (x, y))

        smoke_width, smoke_height = smoke.get_size()
        x -= smoke_width
        while y > 0:
            screen.blit(smoke, (x, y))
            x -= smoke_width
            y -= smoke_height


def make_a_car(sizes):
    cars = []
    smokes = []
    for width, height in sizes:
        unit_len_x = width // 5
        unit_len_y = height // 3
        auto_door_frame_width = unit_len_x // 10

        car = pygame.Surface((width, height), pygame.SRCALPHA)
        car.fill(WHITE)

        make_car_muffler(car, unit_len_x, unit_len_y)
        make_car_body(car, unit_len_x, unit_len_y)
        make_car_windows(car, unit_len_x, unit_len_y, auto_door_frame_width)
        make_car_wheels(car, unit_len_x, unit_len_y)

        smoke = make_smoke(unit_len_x, unit_len_y)

        cars.append(car)
        smokes.append(smoke)

    return cars, smokes


def make_car_muffler(car, unit_len_x, unit_len_y):
    x = 0
    y = 2 * unit_len_y
    ellipse(car, BLACK, (x, y, unit_len_x // 3, unit_len_y // 7))


def make_car_body(car, unit_len_x, unit_len_y):
    coordinates_car = [
        (unit_len_x, 0),
        (3 * unit_len_x, 0),
        (3 * unit_len_x, unit_len_y),
        (5 * unit_len_x, unit_len_y),
        (5 * unit_len_x, 2 * unit_len_y),
        (0, 2 * unit_len_y),
        (0, unit_len_y),
        (unit_len_x, unit_len_y),
        (unit_len_x, 0)
    ]

    polygon(car, CAR_COLOR, coordinates_car)


def make_car_windows(car, unit_len_x, unit_len_y, auto_door_frame_width):
    window_width = unit_len_x - 2 * auto_door_frame_width
    window_height = unit_len_y - 2 * auto_door_frame_width

    window = pygame.Surface((window_width, window_height))
    window.fill(WHITE)

    car.blit(window, (unit_len_x + auto_door_frame_width, auto_door_frame_width))
    car.blit(window, (2 * unit_len_x + auto_door_frame_width, auto_door_frame_width))


def make_car_wheels(car, unit_len_x, unit_len_y):
    circle(car, BLACK, (unit_len_x, 2 * unit_len_y), 2 * unit_len_y // 3)
    circle(car, BLACK, (4 * unit_len_x, 2 * unit_len_y), 2 * unit_len_y // 3)


def make_smoke(width, height):
    smoke = pygame.Surface((width, height), pygame.SRCALPHA)
    smoke.fill(WHITE)

    ellipse(smoke, CLOUD_COLOR, (0, 0, width, height))

    return smoke


main()
