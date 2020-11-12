import math
from random import randint

import pygame

import config
import colors

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
screen.fill(colors.SKY_BLUE)


class Game:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self._game_finished = False

        self.game_loop = GameLoop()
        self.menu = Menu()

    def main_loop(self):
        while not self._game_finished:
            self._clock.tick(config.FPS)

            if self.menu.is_active or self.game_loop.is_over:
                self.menu.is_active = True
                self.menu.draw(self.game_loop.is_over)
            else:
                self.game_loop.loop()

            self.event_handling()
            pygame.display.update()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_finished = True
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_q or key == pygame.K_ESCAPE:
                    self._game_finished = True
                elif key == pygame.K_p and self.menu.is_active:
                    self.menu.is_active = False
                elif key == pygame.K_r and self.game_loop.is_over:
                    self.game_loop.is_over = False
                elif (key == pygame.K_SPACE and not self.game_loop.is_over
                      and not self.menu.is_active):
                    self.game_loop.is_over = True


class GameLoop:
    def __init__(self):
        self.is_over = False

    def loop(self):
        print("loop")

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    self.is_over = True


class Menu:
    def __init__(self):
        font_size = min(config.SCREEN_WIDTH, config.SCREEN_HEIGHT) // 18
        file_names = ['start_menu_text.txt', 'end_menu_text.txt']
        texts = []
        self._text_surf = [[], []]
        self.is_active = True

        font = pygame.font.Font(None, font_size)

        for filename in file_names:
            with open(filename) as text_file:
                texts.append(text_file.readlines())
        for i, text in enumerate(texts):
            for string in text:
                self._text_surf[i].append(font.render(string.strip(), False, colors.BLACK))

    def draw(self, game_over):
        x0 = config.SCREEN_WIDTH // 30
        y0 = config.SCREEN_HEIGHT // 10
        print("menu")
        screen.fill(colors.SKY_BLUE)
        for i, string in enumerate(self._text_surf[game_over]):
            screen.blit(string, (x0, y0 + 2 * i * string.get_height()))

    def event_handling(self, game_over, game_loop):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_p and not game_over:
                    self.is_active = False
                elif key == pygame.K_r and game_over:
                    game_loop.is_over = False


def main():
    game = Game()
    game.main_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
