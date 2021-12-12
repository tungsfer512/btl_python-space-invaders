import pygame

import Objects
import Laser

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# WINDOW
HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)

# Ảnh tàu người chơi
YELLOW_SPACE_Chicken = pygame.image.load("data\\ship (1).png")

# Laser của người chơi
YELLOW_LASER = pygame.image.load("data\\yellow_bullet (1).png")

# Chèn âm thanh
# bullet_sound = pygame.mixer.Sound("sound\\laser.wav")
explosionSound = pygame.mixer.Sound("sound\\quad.wav")
boss_sound = pygame.mixer.Sound("sound\\explosion.wav")
# game_over = pygame.mixer.Sound("sound\\game-over.wav")


class Player(Objects.Objects):
    score: int

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.Chicken_img = YELLOW_SPACE_Chicken
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.Chicken_img)
        self.max_health = health
        self.score = 0

    # Đạn bay lên hết màn hình thì biến mất hoặc chạm vào gà thì gà và đạn đều biến mất
    def move_lasers(self, vel, objs):
        self.cooldown()
        self.score = 0
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        explosionSound.play()
                        objs.remove(obj)
                        self.score = 5
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # Đạn bay lên hết màn hình hoặc chạm vào boss thì biến mất. Đạn chạm vào boss 5 lần thì boss và đạn đều biến mất
    def move_lasers_boss(self, vel, objs):
        self.cooldown()
        self.score = 0
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= 10
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        if obj.health <= 0:
                            boss_sound.play()
                            objs.remove(obj)
                            self.score = 10

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    # Thanh máu
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.Chicken_img.get_height() - 20, self.Chicken_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.Chicken_img.get_height() - 20,
                                               self.Chicken_img.get_width() * (self.health / self.max_health), 10))

    # Bắn
    def shoot(self):
        laser = Laser.Laser(self.x + 90, self.y, self.laser_img)
        self.lasers.append(laser)
