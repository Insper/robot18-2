import math
import pygame

# COLORS
BLACK = (0, 0, 0)

# SPRITES
BACKGROUND_FILE='sparse_obstacles.bmp'
ARROW_THICK = 2
ARROW_WIDTH = 20
ARROW_HEIGHT = 4
ARROW_END_LEN = 12
ROBOT_RADIUS = 15
ROBOT_COLOR = (0, 150, 0)
ROBOT_ARROW_COLOR = (255, 255, 255)
ARROW_COLOR = (0, 0, 255)
LASER_COLOR = (255, 0, 0)

# MOVEMENT
DELTA_LINEAR = 1.2
DELTA_ANGULAR = 0.1

# KEY BINDINGS
SPEED_DELTAS = {
    pygame.K_w: (0, DELTA_LINEAR),
    pygame.K_s: (0, -DELTA_LINEAR),
    pygame.K_a: (1, -DELTA_ANGULAR),
    pygame.K_d: (1, DELTA_ANGULAR),
}
