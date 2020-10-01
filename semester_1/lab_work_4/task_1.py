import pygame
from pygame.draw import *
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 30

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (184, 184, 184)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(GRAY)

    x, y = int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)
    emotion_radius = int(min(SCREEN_WIDTH, SCREEN_HEIGHT) / 3)
    width = 3

    emotion_coord = (x, y)
    draw_emotion(screen, emotion_coord, emotion_radius, width)
    pygame.display.update()

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_emotion(screen, emotion_coord, emotion_radius, width):
    """
    Draws an angry emotion in position x, y, where x and y are coordinates
    of the center
    :param screen: active screen
    :param emotion_coord: tuple of x and y coordinates
    :param emotion_radius: radius of the emotion
    :param width: width of border
    :return: none
    """

    x, y = emotion_coord
    circle(screen, YELLOW, (x, y), emotion_radius)
    circle(screen, BLACK, (x, y), emotion_radius, width)

    draw_lips(screen, emotion_coord, emotion_radius)
    draw_eyes(screen, emotion_coord, emotion_radius, width)


def draw_lips(screen, emotion_coord, emotion_radius):
    """
    Draws lips of the emotion. Anchor point top left
    :param screen: active screen
    :param emotion_coord: coordinates of the emotion
    :param emotion_radius: radius of the emotion
    :return: none
    """

    x0, y0 = emotion_coord
    width = 1*emotion_radius
    height = 0.13*emotion_radius
    x = int(x0 - 0.5*width)
    y = int(y0 + 0.45*emotion_radius)
    rect(screen, BLACK, (x, y, width, height))


def draw_eyes(screen, emotion_coord, emotion_radius, width):
    """
    Draws eyes. Anchor points are on the center of each eye
    :param screen: active screen
    :param emotion_coord: coordinates of the emotion
    :param emotion_radius: radius if the emotion
    :param width: width of the border
    :return: none
    """

    x0, y0 = emotion_coord
    distance_between_eyes = int(0.9 * emotion_radius)
    left_eye_x = int(x0 - distance_between_eyes/2)
    right_eye_x = int(x0 + distance_between_eyes/2)
    eye_y = int(y0 - 0.25 * emotion_radius)

    left_eye_radius = int(0.22 * emotion_radius)
    right_eye_radius = int(0.15 * emotion_radius)
    pupil_radius = int(0.07 * emotion_radius)

    circle(screen, RED, (left_eye_x, eye_y), left_eye_radius)
    circle(screen, BLACK, (left_eye_x, eye_y), left_eye_radius, width)
    circle(screen, BLACK, (left_eye_x, eye_y), pupil_radius)

    circle(screen, RED, (right_eye_x, eye_y), right_eye_radius)
    circle(screen, BLACK, (right_eye_x, eye_y), right_eye_radius, width)
    circle(screen, BLACK, (right_eye_x, eye_y), pupil_radius)

    draw_eyebrows(screen, emotion_coord, emotion_radius,
                  distance_between_eyes, eye_y,
                  left_eye_radius, right_eye_radius,
                  left_eye_x, right_eye_x)


def draw_eyebrows(screen, emotion_coord, emotion_radius,
                  distance_between_eyes, eye_y,
                  left_eye_radius, right_eye_radius,
                  left_eye_x, right_eye_x):
    """
    Draws eyebrows. Anchor point is bottom right for left eyebrow
    and bottom left for right eyebrow
    :param screen: active screen
    :param emotion_coord: coordinates of the emotion
    :param emotion_radius: radius of the emotion
    :param distance_between_eyes: distance between centers of eyes
    :param eye_y: y coordinate of the center of the eye
    :param left_eye_radius: the radius of the left eye
    :param right_eye_radius: the radius of the right eye
    :param left_eye_x: x coordinate of the left eye
    :param right_eye_x: x coordinate of the right eye
    :return: none
    """

    x0, y0 = emotion_coord
    eyebrow_width = int(0.13 * emotion_radius)
    distance_between_eyebrows = int(0.3*distance_between_eyes)
    left_eyebrow_x = int(x0 - distance_between_eyebrows/2)
    right_eyebrow_x = int(x0 + distance_between_eyebrows / 2)

    eyebrow_y = eye_y
    left_eyebrow_length = -int(0.9 * emotion_radius)
    right_eyebrow_length = int(1 * emotion_radius)
    left_eyebrow_angle = -math.atan(left_eye_radius / (left_eyebrow_x - left_eye_x))
    right_eyebrow_angle = math.atan(right_eye_radius / (right_eye_x - right_eyebrow_x))

    left_anchor_point = (left_eyebrow_x, eyebrow_y)
    right_anchor_point = (right_eyebrow_x, eyebrow_y)
    left_eyebrow_coordinates = calc_eyebrow_coordinates(left_anchor_point,
                                                        left_eyebrow_length,
                                                        left_eyebrow_angle,
                                                        eyebrow_width
                                                        )
    right_eyebrow_coordinates = calc_eyebrow_coordinates(right_anchor_point,
                                                         right_eyebrow_length,
                                                         right_eyebrow_angle,
                                                         eyebrow_width
                                                         )

    polygon(screen, BLACK, left_eyebrow_coordinates)
    polygon(screen, BLACK, right_eyebrow_coordinates)


def calc_eyebrow_coordinates(anchor_point, length, angle, width):
    """
    Calculates points of eyebrow
    :param anchor_point: a bottom right (bottom left) point
    :param length: eyebrow length x
    :param angle: brow angle
    :param width: eyebrow thickness
    :return: coordinates
    """
    x1, y1 = anchor_point

    x2 = x1 + length
    y2 = int(y1 - length * math.tan(angle))

    x3 = x2
    y3 = y2 - width

    x4 = x1
    y4 = y1 - width

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


main()
