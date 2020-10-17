import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    finished = False
    menu_is_active = True
    menu_text = make_menu_text()

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

        game_scenario(screen, menu_is_active, menu_text)

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


def game_scenario(screen, menu_is_active, menu_text):
    if menu_is_active:
        draw_menu(screen, menu_text)
    else:
        draw_game(screen)


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


def draw_game(screen):
    screen.fill(BLACK)
    pygame.display.update()


main()
