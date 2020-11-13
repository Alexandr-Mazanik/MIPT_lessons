import math
from random import randint
from abc import ABC, abstractmethod
from enum import Enum

import pygame

import config
import colors

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
screen.fill(colors.SKY_BLUE)


class GameObject(ABC):
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        self.hp = config.creature_hp
        self.is_alive = True
        self.color = colors.GRAY

    def hit(self, damage):
        self.hp -= damage
        self.color = colors.DARK_RED

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def act(self, creatures):
        pass


class Projectile(Enum):
    NONE = 0
    BOMB = 1
    ROCKET = 2


class Tank(GameObject):
    def __init__(self, x0, y0, muzzle_length):
        GameObject.__init__(self, x0, y0)
        self.color = colors.DARK_GREEN
        self.turret_angel = 90
        self.muzzle_length = muzzle_length
        self.active_projectile = Projectile.NONE
        self.num_of_rockets = config.num_of_rockets
        self.num_of_bombs = config.number_of_bombs
        self.start_pos_muzzle = (self.x + config.tank_width // 2,
                                 self.y - config.tank_turret_radius // 3)

        self.increase_time = False
        self.time = 0

    def move(self):
        pass

    def draw(self):
        self.color = colors.DARK_GREEN
        strings = []
        font_size = config.menu_font_size
        font = pygame.font.Font(None, font_size)
        strings.append(config.hp_string + str(self.hp))
        strings.append(config.rockets + str(self.num_of_rockets))
        strings.append(config.bombs + str(self.num_of_bombs))

        pygame.draw.circle(screen, self.color,
                           (self.x + config.tank_width // 2,
                            self.y), config.tank_turret_radius)
        pygame.draw.circle(screen, colors.BLACK,
                           (self.x + config.tank_width // 2,
                            self.y), config.tank_turret_radius, 1)
        pygame.draw.rect(screen, self.color,
                         ((self.x, self.y),
                          (config.tank_width, config.tank_height)))
        pygame.draw.rect(screen, colors.BLACK,
                         ((self.x, self.y),
                          (config.tank_width, config.tank_height)), 1)
        for sign in (-1, 1, 0):
            pygame.draw.circle(screen, colors.BLACK,
                               (self.x + int(config.tank_width * (1 / 2 + sign / 3)),
                                self.y + config.tank_height),
                               config.tank_wheel_radius)

        self.start_pos_muzzle = (self.x + config.tank_width // 2,
                                 self.y - config.tank_turret_radius // 3)
        pygame.draw.line(screen, colors.BLACK,
                         self.start_pos_muzzle,
                         self.calc_end_pos_muzzle(self.start_pos_muzzle), 6)

        for i, string in enumerate(strings):
            string_surf = font.render(string, False, colors.BLACK)
            screen.blit(string_surf,
                        (config.delta_r, config.delta_r + i * string_surf.get_height()))

    def act(self, creatures):
        if self.increase_time:
            self.time += 1

        x, y = self.calc_end_pos_muzzle(self.start_pos_muzzle)
        if self.active_projectile == Projectile.ROCKET and self.num_of_rockets > 0:
            creatures.append(Rocket(x, y, self.turret_angel, Tank))
            self.num_of_rockets -= 1
        elif self.active_projectile == Projectile.BOMB and self.num_of_bombs > 0:
            creatures.append(Bomb(x, y, True, Tank, self.turret_angel, self.time))
            self.time = 0
            self.num_of_bombs -= 1
        self.active_projectile = Projectile.NONE

    def calc_end_pos_muzzle(self, start_pos):
        x = int(start_pos[0] + self.muzzle_length * math.cos(math.radians(self.turret_angel)))
        y = int(start_pos[1] - self.muzzle_length * math.sin(math.radians(self.turret_angel)))

        return x, y

    def check_sides(self):
        if self.x <= 0:
            self.x += config.delta_r
            return True
        elif self.x >= config.SCREEN_WIDTH - config.tank_width:
            self.x -= config.delta_r
            return True
        else:
            return False

    def check_turret_angel(self):
        if self.turret_angel <= 0:
            self.turret_angel += config.delta_alpha
            return True
        elif self.turret_angel >= 180:
            self.turret_angel -= config.delta_alpha
            return True
        else:
            return False


class Cloud(GameObject):
    def __init__(self, x0, y0):
        GameObject.__init__(self, x0, y0)
        self.color = colors.WHITE
        self._time = 0
        self._direction = 0
        self._velocity = config.clouds_velocity
        self._x_velocity = self._y_velocity = 0

    def move(self):
        if self._time % config.clouds_lifetime == 0:
            self._direction = randint(0, 360)
            self._x_velocity = int(self._velocity * math.cos(math.radians(self._direction)))
            self._y_velocity = int(self._velocity * math.sin(math.radians(self._direction)))
        self.x += self._x_velocity
        self.y += self._y_velocity

        self.check_sides()

        self._time += 1

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), config.radius_of_evil_clouds)
        pygame.draw.circle(screen, colors.BLACK,
                           (self.x, self.y), config.radius_of_evil_clouds, 1)

    def act(self, creatures):
        if self.hp <= 0:
            self.is_alive = False
        if self._time % config.bombs_time == 0 and self.is_alive:
            creatures.append(Bomb(self.x, self.y, False, Cloud))

    def check_sides(self):
        if self.x <= 0:
            self.x += config.delta_r
            self._x_velocity = -self._x_velocity
        elif self.x >= config.SCREEN_WIDTH:
            self.x -= config.delta_r
            self._x_velocity = -self._x_velocity
        elif self.y <= 0:
            self.y += config.delta_r
            self._y_velocity = -self._y_velocity
        elif self.y >= config.field_for_movement_height:
            self.y -= config.delta_r
            self._y_velocity = -self._y_velocity


class Bomb(GameObject):
    def __init__(self, x0, y0, gravity, spawned_by, direction=0, time=0):
        GameObject.__init__(self, x0, y0)
        self.spawned_by = spawned_by
        if self.spawned_by == Cloud:
            self.color = colors.GRAY
        else:
            self.color = colors.YELLOW
        self._gravity = gravity

        self.direction = direction
        velocity = time * config.time_velocity_factor
        self.x_velocity = int(velocity * math.cos(math.radians(self.direction)))
        self.y_velocity = int(velocity * math.sin(math.radians(self.direction)))

    def move(self):
        if not self._gravity:
            self.y += config.bombs_speed
        else:
            self.gravity()
        self.check_ground()

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), config.bombs_radius)
        pygame.draw.circle(screen, colors.BLACK,
                           (self.x, self.y), config.bombs_radius, 1)
        pygame.draw.circle(screen, colors.RED,
                           (self.x, self.y), config.bombs_center_radius)

    def act(self, creatures):
        pass

    def check_ground(self):
        if self.y >= config.SCREEN_HEIGHT - config.ground_height:
            self.is_alive = False

    def gravity(self):
        self.x += self.x_velocity
        self.y -= self.y_velocity

        self.y_velocity -= config.g


class Rocket(GameObject):
    def __init__(self, x0, y0, direction, spawned_by):
        GameObject.__init__(self, x0, y0)
        self.spawned_by = spawned_by
        self.direction = direction
        self.velocity = config.rocket_speed
        self.x_velocity = self.y_velocity = 0

    def move(self):
        self.x_velocity = int(self.velocity * math.cos(math.radians(self.direction)))
        self.y_velocity = int(self.velocity * math.sin(math.radians(self.direction)))

        self.x += self.x_velocity
        self.y -= self.y_velocity

    def draw(self):
        pygame.draw.circle(screen, colors.RED,
                           (self.x, self.y), config.rocket_radius)
        pygame.draw.circle(screen, colors.BLACK,
                           (self.x, self.y), config.rocket_radius, 1)
        pygame.draw.line(screen, colors.BLACK, (self.x, self.y),
                         self.calc_end_pos(), 4)

    def act(self, creatures):
        pass

    def calc_end_pos(self):
        x = int(self.x + config.rocket_length * math.cos(math.radians(self.direction)))
        y = int(self.y - config.rocket_length * math.sin(math.radians(self.direction)))

        return x, y


class Game:
    def __init__(self):
        self._game_finished = False

        self.game_loop = GameLoop()
        self.menu = Menu()

    def main_loop(self):
        clock = pygame.time.Clock()
        while not self._game_finished:
            clock.tick(config.FPS)

            if self.menu.is_active or self.game_loop.is_over:
                self.menu.is_active = True
                self.menu.draw(self.game_loop.is_over, self.game_loop.win)
            else:
                self.game_loop.loop()

            self.event_handling()
            pygame.display.update()
            self.game_keys_pressed()

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
                    del self.game_loop
                    self.game_loop = GameLoop()
                    self.game_loop.is_over = False
                elif key == pygame.K_SPACE and not self.menu.is_active:
                    self.game_loop.is_over = True
                elif key == pygame.K_j and not self.menu.is_active:
                    self.game_loop.tank.active_projectile = Projectile.ROCKET
                elif key == pygame.K_i and not self.menu.is_active:
                    self.game_loop.tank.increase_time = True
            elif event.type == pygame.KEYUP:
                key = event.key
                if key == pygame.K_i and not self.menu.is_active:
                    self.game_loop.tank.active_projectile = Projectile.BOMB
                    self.game_loop.tank.increase_time = False

    def game_keys_pressed(self):
        keys = pygame.key.get_pressed()

        if not self.game_loop.tank.check_sides() and not self.menu.is_active:
            if keys[pygame.K_a]:
                self.game_loop.tank.x -= config.tank_speed
            elif keys[pygame.K_d]:
                self.game_loop.tank.x += config.tank_speed
        if not self.game_loop.tank.check_turret_angel() and not self.menu.is_active:
            if keys[pygame.K_w]:
                self.game_loop.tank.turret_angel += config.tank_turret_speed
            elif keys[pygame.K_s]:
                self.game_loop.tank.turret_angel -= config.tank_turret_speed


class GameLoop:
    def __init__(self):
        self.is_over = False
        self.win = False
        self._num_of_clouds = config.num_of_evil_clouds
        self.game_creatures = []

        for i in range(self._num_of_clouds):
            cloud_x, cloud_y = randomize_init_coord()
            self.game_creatures.append(Cloud(cloud_x, cloud_y))

        self.tank = Tank(config.tank_x0, config.tank_y0, config.tank_muzzle_length)
        self.game_creatures.append(self.tank)

    def loop(self):
        self.move_objects()
        self.act_objects()
        self.check_contacts()
        self.draw_scenario()

        self.check_end()

    def move_objects(self):
        for creature in self.game_creatures:
            if creature.is_alive:
                creature.move()

    def draw_scenario(self):
        draw_background()
        for creature in self.game_creatures:
            if creature.is_alive:
                creature.draw()

    def act_objects(self):
        for creature in self.game_creatures:
            if creature.is_alive:
                creature.act(self.game_creatures)

    def check_contacts(self):
        for body_1 in self.game_creatures:
            if type(body_1) == Bomb and body_1.is_alive:
                for body_2 in self.game_creatures:
                    if type(body_2) == Tank:
                        if is_contact(body_1, body_2):
                            self.tank.hit(config.bomb_damage)
                            body_1.is_alive = False
                    elif type(body_2) == Cloud and body_2.is_alive:
                        if is_contact(body_1, body_2):
                            body_2.hit(config.tank_bomb_damage)
                            body_1.is_alive = False
            elif type(body_1) == Rocket and body_1.is_alive:
                for body_2 in self.game_creatures:
                    if type(body_2) == Cloud and body_2.is_alive:
                        if is_contact(body_1, body_2):
                            body_2.hit(config.rocket_damage)
                            body_1.is_alive = False

    def check_end(self):
        if (self.tank.hp <= 0 or
                self.tank.num_of_bombs == self.tank.num_of_rockets == 0):
            self.is_over = True
            self.win = False

        num_of_dead_clouds = 0
        for creature in self.game_creatures:
            if type(creature) == Cloud and not creature.is_alive:
                num_of_dead_clouds += 1
        if num_of_dead_clouds == config.num_of_evil_clouds:
            self.is_over = True
            self.win = True


class Menu:
    def __init__(self):
        self.is_active = True
        self._text_surf = [[], []]

        self.read_texts_from_file()

    def read_texts_from_file(self):
        texts = []

        font_size = config.menu_font_size
        font = pygame.font.Font(None, font_size)

        for filename in config.file_names:
            with open(filename) as text_file:
                texts.append(text_file.readlines())
        for i, text in enumerate(texts):
            for string in text:
                self._text_surf[i].append(font.render(string.strip(), False, colors.BLACK))

    def draw(self, game_over, is_win):
        x0 = config.SCREEN_WIDTH // 30
        y0 = config.SCREEN_HEIGHT // 10
        win_text_x0 = self._text_surf[1][0].get_width() + 2 * x0

        font_size = config.menu_font_size
        font = pygame.font.Font(None, font_size)

        draw_background()
        for i, string in enumerate(self._text_surf[game_over]):
            screen.blit(string, (x0, y0 + 2 * i * string.get_height()))
        if game_over:
            if is_win:
                string_surf = font.render(config.win_string, False, colors.BLACK)
                screen.blit(string_surf, (win_text_x0, y0))
            else:
                string_surf = font.render(config.loose_string, False, colors.BLACK)
                screen.blit(string_surf, (win_text_x0, y0))


def main():
    game = Game()
    game.main_loop()

    pygame.quit()


def randomize_init_coord():
    x = randint(0, config.SCREEN_WIDTH)
    y = randint(0, config.field_for_movement_height)

    return x, y


def draw_background():
    screen.fill(colors.SKY_BLUE)
    pygame.draw.rect(screen, colors.GREEN, config.ground_rect)


def is_contact(body_1, body_2):
    if type(body_2) == Tank and body_1.spawned_by == Cloud:
        if (body_2.x <= body_1.x <= body_2.x + config.tank_width and
                body_1.y >= body_2.y):
            return True
    elif type(body_2) == Cloud and body_1.spawned_by == Tank:
        if (math.sqrt((body_1.x - body_2.x) ** 2 + (body_1.y - body_2.y) ** 2) <=
                config.radius_of_evil_clouds + config.bombs_radius):
            return True
    else:
        return False


if __name__ == "__main__":
    main()
