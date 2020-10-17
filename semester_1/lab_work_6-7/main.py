import pygame
from random import randint

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
    max_speed, min_speed = 20, 10
    x = randint(radius, SCREEN_WIDTH - radius)
    y = randint(radius, SCREEN_HEIGHT - radius)
    v_x = randint(min_speed, max_speed)
    v_y = randint(min_speed, max_speed)
    record = {'x': x,
              'y': y,
              'radius': radius,
              'v_x': v_x,
              'v_y': v_y}

    return record


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
    pass


main()
