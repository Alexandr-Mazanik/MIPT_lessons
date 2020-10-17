import pygame
from random import randint
import math

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
FPS = 30

BALLS = []

WHITE = (255, 255, 255)
WHITE_ALPHA = (255, 255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
PURPLE = (128, 0, 128)
AQUA = (0, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    finished = False
    menu_is_active = True
    number_of_balls = 10

    menu_text = make_menu_text()
    balls_surfaces = make_balls(number_of_balls)

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if (key == pygame.K_q or
                        key == pygame.K_ESCAPE or
                        key == pygame.K_BACKSPACE):
                    finished = True
                if key == pygame.K_SPACE and menu_is_active:
                    menu_is_active = False
                if key == pygame.K_p and not menu_is_active:
                    menu_is_active = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click(event.pos)

        game_scenario(screen, menu_is_active, menu_text,
                      number_of_balls, balls_surfaces)

    pygame.quit()


def make_menu_text():
    """
    Gets menu text from file and creates surfaces
    :return: list of surfaces of strings
    """
    font_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 18
    text = []

    font = pygame.font.Font(None, font_size)
    with open('menu_text.txt') as text_file:
        text_strings = text_file.readlines()

    for string in text_strings:
        text.append(font.render(string, True, RED))

    return text


def make_balls(number_of_balls):
    """
    makes surfaces of balls
    :param number_of_balls: number of balls
    :return: list of surfaces of balls
    """
    balls = []
    colors = [WHITE, GREEN, RED, BLUE,
              YELLOW, BROWN, PURPLE, AQUA]
    for i in range(number_of_balls):
        size = randint(min(SCREEN_WIDTH, SCREEN_HEIGHT) // 17,
                       min(SCREEN_WIDTH, SCREEN_HEIGHT) // 10)
        ball = pygame.Surface((size, size), pygame.SRCALPHA)
        ball.fill(WHITE_ALPHA)
        pygame.draw.ellipse(ball,
                            colors[randint(0, len(colors)-1)],
                            ((0, 0), (size, size)))
        balls.append(ball)
        BALLS.append(add_ball_dict(size // 2))

    return balls


def add_ball_dict(radius):
    """
    calculates init params for balls
    :param radius: a radius of the ball
    :return: the record
    """
    x, y, v_x, v_y = randomize_data(radius)
    record = {'x': x,
              'y': y,
              'radius': radius,
              'v_x': v_x,
              'v_y': v_y}

    return record


def randomize_data(radius):
    """
    calculates a random position and speed
    :param radius: the radius of the ball
    :return: x and y random coordinates,
             v_x and v_y random speed
    """
    min_speed = -min(SCREEN_WIDTH, SCREEN_HEIGHT) // 100
    max_speed = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 100
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    v_x = randint(min_speed, max_speed)
    v_y = randint(min_speed, max_speed)

    return x, y, v_x, v_y


def game_scenario(screen, menu_is_active, menu_text,
                  number_of_balls, balls_surfaces):
    if menu_is_active:
        draw_menu(screen, menu_text)
    else:
        draw_game(screen, number_of_balls, balls_surfaces)


def draw_menu(screen, text):
    """
    Draws a menu
    :param screen: an active screen
    :param text: the text of the menu
    :return: none
    """
    x0_text = SCREEN_WIDTH // 7
    y0_text = SCREEN_HEIGHT // 3
    for i, string in enumerate(text):
        screen.blit(string, [x0_text, y0_text + 2 * i * string.get_height()])

    pygame.display.update()


def draw_game(screen, number_of_balls, balls_surfaces):
    screen.fill(BLACK)

    for i, (ball, data) in enumerate(zip(balls_surfaces, BALLS)):
        x, y = convert_coord(data['x'], data['y'], data['radius'])
        screen.blit(ball, (x, y))
        calc_new_data(i)

    pygame.display.update()


def convert_coord(x_center, y_center, radius):
    """
    Convert coordinates from central point to top left point
    :param x_center: x coordinate of the center
    :param y_center: y coordinate of the center
    :param radius: the radius of the ball
    :return: coordinates of top left point of the surface
    """
    x = x_center - radius
    y = y_center - radius

    return x, y


def calc_new_data(i):
    """
    calculates a new data for a ball positions
    :param i: a number of the ball
    :return: none
    """
    hit_the_wall, wall = is_touch(i)  # 'wall' is blow wall number

    if hit_the_wall:
        reflection(i, wall)

    BALLS[i]['x'] += BALLS[i]['v_x']
    BALLS[i]['y'] += BALLS[i]['v_y']


def is_touch(i):
    """
    checks if the wall was touched
    :param i: number of the ball
    :return: True, if a wall was hit
             1 - left wall or right wall
             2 - top wall or bottom wall,
             -1 - if a wall wasn't hit
    """
    x, y = BALLS[i]['x'], BALLS[i]['y']
    if x < 0 or x > SCREEN_WIDTH:
        return True, 1
    elif y < 0 or y > SCREEN_HEIGHT:
        return True, 2
    else:
        return False, -1


def reflection(i, wall):
    """
    change a speed of the ball
    :param i: number of the ball
    :param wall: 1 - left wall or right wall, 2 - top wall or bottom wall
    :return: none
    """
    if wall == 1:
        BALLS[i]['v_x'] = -BALLS[i]['v_x']
        BALLS[i]['x'] += BALLS[i]['v_x']
    elif wall == 2:
        BALLS[i]['v_y'] = -BALLS[i]['v_y']
        BALLS[i]['y'] += BALLS[i]['v_y']


def mouse_click(position):
    """
    mouse click handling
    :param position: a position of the mouseclick
    :return: none
    """
    x, y = position
    distance, nearest_ball = find_the_nearest_ball(x, y)

    if is_hit(distance, nearest_ball):
        change_data(nearest_ball)


def find_the_nearest_ball(x, y):
    """
    finds an index of the nearest ball to the mouse click position
    :param x: x coordinate of the mouseclick
    :param y: y coordinate of the mouseclick
    :return: a distance to the nearest ball
    and an index of the nearest ball to the mouseclick position
    """
    minimal_distance = max(SCREEN_WIDTH, SCREEN_HEIGHT)
    nearest_ball_num = -1
    for i, data in enumerate(BALLS):
        delta_x = abs(data['x'] - x)
        delta_y = abs(data['y'] - y)
        distance = math.sqrt(delta_x**2 + delta_y**2)
        if distance < minimal_distance:
            minimal_distance = distance
            nearest_ball_num = i

    return minimal_distance, nearest_ball_num


def is_hit(distance, ball_num):
    return distance < BALLS[ball_num]['radius']


def change_data(ball_num):
    """
    changes coordinates and speed of the ball after hitting
    :param ball_num: number of the ball
    :return: none
    """
    new_x, new_y, new_v_x, new_v_y = randomize_data(BALLS[ball_num]['radius'])

    BALLS[ball_num]['x'] = new_x
    BALLS[ball_num]['y'] = new_y
    BALLS[ball_num]['v_x'] = new_v_x
    BALLS[ball_num]['v_y'] = new_v_y


main()
