import pygame

import Objects
import Laser

# Ảnh gà
RED_CHICKEN = pygame.image.load("data\\starwar_red (1).png")
BLUE_CHICKEN = pygame.image.load("data\\super_blue (1).png")
GREEN_CHICKEN = pygame.image.load("data\\solider_green (1).png")

# Laser của gà
RED_EGG = pygame.image.load("data\\red_egg (1).png")
BLUE_EGG = pygame.image.load("data\\blue_egg (1).png")
GREEN_EGG = pygame.image.load("data\\green_egg (1).png")


class Enemy(Objects.Objects):

    COLOR_MAP = {
                "red": (RED_CHICKEN, RED_EGG),
                "green": (GREEN_CHICKEN, GREEN_EGG),
                "blue": (BLUE_CHICKEN, BLUE_EGG)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.Chicken_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.Chicken_img)

    def move(self, vel):
        self.y += vel

    # Gà đẻ trứng
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser.Laser(self.x + 17, self.y + 20, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
