import sys
import pygame

import mainRun
import Button

# WINDOW
pygame.font.init()

HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)

# BACKGROUND
BACKGROUND = pygame.transform.scale(pygame.image.load("data\\background.jpg"), (WIDTH, HEIGHT))

# BUTTONS
start_btn = pygame.image.load("data\\start_btn.png")
exit_btn = pygame.image.load("data\\exit_btn.png")

# title_font = pygame.font.SysFont("Calibri", 70)


#Button
start_butt = Button.Button(WIDTH / 2 - start_btn.get_width() / 2, 350, start_btn)
exit_butt = Button.Button(WIDTH / 2 - exit_btn.get_width() / 2, 550, exit_btn)


def main():
    title_font = pygame.font.Font("space_invaders.ttf", 44)
    run = True
    while run:
        # Hiện màn hình
        WINDOWS.blit(BACKGROUND, (0, 0))
        # Hiện chữ
        title_label = title_font.render("CHICKEN INVADERS", True, (255, 255, 255))
        WINDOWS.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 150))
        # hiển thị nút
        start_butt.draw()
        exit_butt.draw()
        pygame.display.update()
        # Nhấn phím cách để bắt đầu
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if start_butt.clicked:
                mainRun.main()
            if exit_butt.clicked:
                sys.exit()
        start_butt.clicked = False
        exit_butt.clicked = False
    sys.exit()

main()
