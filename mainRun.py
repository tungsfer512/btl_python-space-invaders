import sys

import pygame
import random

import Objects
import Player
import Enemy
import Boss
import endGame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

pygame.font.init()

# WINDOW
HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)

# Ảnh gà
RED_CHICKEN = pygame.image.load("data\\starwar_red (1).png")
BLUE_CHICKEN = pygame.image.load("data\\super_blue (1).png")
GREEN_CHICKEN = pygame.image.load("data\\solider_green (1).png")

# BOSS
RED_SPACE_BOSS = pygame.image.load("data\\starwar_red_boss.png")
BLUE_SPACE_BOSS = pygame.image.load("data\\super_blue_boss.png")

# Ảnh tàu người chơi
YELLOW_SPACE_Chicken = pygame.image.load("data\\ship (1).png")

# Laser của gà
RED_EGG = pygame.image.load("data\\red_egg (1).png")
BLUE_EGG = pygame.image.load("data\\blue_egg (1).png")
GREEN_EGG = pygame.image.load("data\\green_egg (1).png")

# Laser của người chơi
YELLOW_LASER = pygame.image.load("data\\yellow_bullet (1).png")

# BACKGROUND
BACKGROUND = pygame.transform.scale(pygame.image.load("data\\background.jpg"), (WIDTH, HEIGHT))

# BUTTONS
start_btn = pygame.image.load("data\\start_btn.png")
exit_btn = pygame.image.load("data\\exit_btn.png")

# chèn âm thanh
# bullet_sound = pygame.mixer.Sound("sound/laser.wav")
explosionSound = pygame.mixer.Sound("sound\\quad.wav")
boss_sound = pygame.mixer.Sound("sound\\explosion.wav")
# game_over = pygame.mixer.Sound("sound/game-over.wav")

background_sound = pygame.mixer.Sound("sound\\HipHop.wav")
background_sound.play(-1)
background_sound.set_volume(0.03)


def main():
    run = True

    FPS = 60
    level = 19

    lives = 5

    # Font chữ
    main_font = pygame.font.Font("space_invaders.ttf", 35)
    # lost_font = pygame.font.SysFont("Calibri", 60)
    lost_font = pygame.font.Font('space_invaders.ttf', 60)

    # Mảng gà + số lượng gà mỗi level + tốc độ đẻ trứng
    enemies = []
    wave_length = 5
    enemy_vel = 1
    # Tốc độ di chuyển + bắn của người chơi
    laser_vel = 5
    boss_vel = 2
    player = Player.Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0
    score = 0

    def pause():
        pauseds = True

        while pauseds:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if events.key == pygame.K_SPACE:
                        pauseds = False
            # WINDOWS.fill((255, 255, 255))
            pause_label = lost_font.render("PAUSE!!!", True, (255, 0, 0))
            pause_label1 = main_font.render("Press SPACE to continue", True, (250, 141, 44))
            pause_label2 = main_font.render("Press ESC to quit", True, (250, 141, 44))
            WINDOWS.blit(pause_label, (WIDTH // 2 - pause_label.get_width() // 2, HEIGHT // 2 - 200))
            WINDOWS.blit(pause_label1, (WIDTH // 2 - pause_label1.get_width() // 2, HEIGHT//2 - 30))
            WINDOWS.blit(pause_label2, (WIDTH // 2 - pause_label2.get_width() // 2, HEIGHT // 2 + 30))
            pygame.display.update()
            clock.tick(FPS)

    # reset màn hình FPS lần / giây
    def redraw_window():
        WINDOWS.blit(BACKGROUND, (0, 0))
        # background_sound.play()
        # Hiển thị sô mạng còn lại + level
        lives_label = main_font.render(f"Lives: {lives}", True, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", True, (255, 255, 255))
        score_lable = main_font.render(f"Score: {score}", True, (255, 255, 255))
        WINDOWS.blit(lives_label, (10, 10))
        WINDOWS.blit(score_lable, (WIDTH // 2 - score_lable.get_width() // 2, 10))
        WINDOWS.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        # Hiển thị gà và người chơi
        for enemys in enemies:
            enemys.draw(WINDOWS)

        player.draw(WINDOWS)
        # Nếu thua in ra "You lost..."
        # if lost:
        #     # background_sound.pause()
        #     # game_over.play()
        #     lost_label = lost_font.render("GAME OVER", True, (255, 255, 255))
        #     WINDOWS.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
        # # background_sound.pause()
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # Nếu hết máu và còn mạng --> hồi sinh
        if lives > 0 and player.health <= 0:
            player.health = 100
            lives -= 1
        # Nếu hết mạng --> thua
        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
                endGame.main(score)
            else:
                continue
        # Nếu mảng enermies rỗng --> hết level --> sang level mới
        # Nếu là level 5, 10, 15, 20, ... thì có boss (số lượng boss = level//5)
        # Mỗi ván mới cộng thêm 5 gà
        if len(enemies) == 0:
            level += 1
            if level % 10 != 0:
                wave_length += 5
                for i in range(wave_length):
                    enemy = Enemy.Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                        random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)
            else:
                enemy_vel += 1
                boss_vel += 1
                for i in range(level // 10):
                    boss = Boss.Boss(random.randrange(130, WIDTH - 130), 0, random.choice(["red_boss", "blue_boss"]))
                    enemies.append(boss)

        # Thoát game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pause()
            # Nếu nhấn chuột trái thì bắn (left-middle-right = 1-2-3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.shoot()

        '''
        # Di chuyển bằng các phím mũi tên
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        # Bắn liên tục
        player.shoot()
        '''
        # Di chuyển bằng chuột
        mx, my = pygame.mouse.get_pos()
        player.x = mx - player.get_width()//2
        player.y = my - player.get_height()//2

        score += player.score
        # Xét xem đang ở level boss hay level thường
        if level % 10 != 0:
            for enemy in enemies:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()
                if Objects.collide(enemy, player):
                    player.health -= 10
                    explosionSound.play()
                    enemies.remove(enemy)
                    score += 5
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)
            player.move_lasers(-laser_vel, enemies)
        else:
            for enemy in enemies:
                if enemy.x + enemy.get_width() >= WIDTH - 10 or enemy.x <= 10:
                    enemy.vel *= -1
                    enemy.y += enemy.get_height()

                enemy.move()
                enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 75) == 1:
                    enemy.shoot()
                if Objects.collide(enemy, player):
                    boss_sound.play()
                    player.health -= 50
                    enemies.remove(enemy)
                    score += 10
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 2
                    enemies.remove(enemy)
            player.move_lasers_boss(-laser_vel, enemies)
            score += player.score
            pygame.display.update()
