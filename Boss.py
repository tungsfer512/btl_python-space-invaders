import pygame

import Objects
import Laser

# WINDOW
HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)

# BOSS
RED_SPACE_BOSS = pygame.image.load("data\\starwar_red_boss.png")
BLUE_SPACE_BOSS = pygame.image.load("data\\super_blue_boss.png")

# Laser của boss
RED_EGG = pygame.image.load("data\\red_egg (1).png")
BLUE_EGG = pygame.image.load("data\\blue_egg (1).png")


class Boss(Objects.Objects):

    COLOR_MAP = {
        "red_boss": (RED_SPACE_BOSS, RED_EGG),
        "blue_boss": (BLUE_SPACE_BOSS, BLUE_EGG)
    }

    def __init__(self, x, y, color, health=50):
        super().__init__(x, y, health)
        self.Chicken_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.Chicken_img)
        self.vel = 2

    def move(self):
        self.x += self.vel

    # Boss đẻ trứng
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser.Laser(self.x + 50, self.y + 80, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
