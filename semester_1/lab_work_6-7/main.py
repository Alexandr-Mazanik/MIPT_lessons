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

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_ESCAPE:
                    finished = True
                if key == pygame.K_SPACE and menu_is_active:
                    menu_is_active = False

        game_scenario(screen, menu_is_active)

    pygame.quit()


def game_scenario(screen, menu_is_active):
    if menu_is_active:
        draw_menu(screen)
    else:
        draw_game(screen)


def draw_menu(screen):
    pass


def draw_game(screen):
    pass


main()
