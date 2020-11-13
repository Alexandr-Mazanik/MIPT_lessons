FPS = 60

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

ground_height = SCREEN_HEIGHT // 6
ground_rect = ((0, SCREEN_HEIGHT - ground_height),
               (SCREEN_WIDTH, SCREEN_HEIGHT))

menu_font_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 18

num_of_evil_clouds = 15
field_for_movement_height = 3 * SCREEN_HEIGHT // 5
radius_of_evil_clouds = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 30
clouds_velocity = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 240
clouds_lifetime = 60

tank_speed = SCREEN_WIDTH // 200
tank_width = SCREEN_WIDTH // 5
tank_height = SCREEN_HEIGHT // 14
tank_wheel_radius = tank_width // 7
tank_turret_radius = tank_height // 2
tank_turret_speed = 1
tank_muzzle_length = tank_width // 2
tank_x0 = SCREEN_WIDTH // 3
tank_y0 = SCREEN_HEIGHT - 5 * ground_height // 4

bombs_radius = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 50
bombs_center_radius = bombs_radius // 3
bombs_speed = clouds_velocity
bombs_time = 3 * clouds_lifetime
number_of_bombs = 3 * num_of_evil_clouds

time_velocity_factor = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 500

rocket_length = tank_muzzle_length // 3
rocket_speed = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 60
rocket_radius = 3 * bombs_center_radius // 2
num_of_rockets = 4

creature_hp = 100
g = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 600
delta_r = 10
delta_alpha = 2

bomb_damage = creature_hp // 4
tank_bomb_damage = creature_hp // 2
rocket_damage = creature_hp

# ========================================================================

file_names = ['start_menu_text.txt', 'end_menu_text.txt']
hp_string = "Your HP is "
rockets = "Rockets "
bombs = "Bombs "
win_string = "Вы победили!!!"
loose_string = "Вы проиграли..."

# ========================================================================

if __name__ == "__main__":
    print("It's a config file")
