import pygame

import Objects


# Trứng or laser
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    # Vẽ trứng/laser lên màn hình
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # Di chuyển laser
    def move(self, vel):
        self.y += vel

    # Laser đã đi hết màn hình chưa???
    def off_screen(self, height):
        return not(0 <= self.y <= height)

    # Kiểm tra va chạm của 2 đối tượng
    def collision(self, obj):
        return Objects.collide(self, obj)
