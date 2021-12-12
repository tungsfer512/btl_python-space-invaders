import pygame

# WINDOW
HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)


class Button:

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # pygame.mouse.set_cursor()
            if pygame.mouse.get_pressed()[0] is True and self.clicked is not True:
                self.clicked = True
        WINDOWS.blit(self.image, (self.rect.x, self.rect.y))
