import sys
import pygame


# WINDOW
pygame.font.init()
HEIGHT, WIDTH = 750, 1500
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("data\\starwar_red (1).png")
pygame.display.set_icon(icon)

# BACKGROUND
BACKGROUND = pygame.transform.scale(pygame.image.load("data\\background.jpg"), (WIDTH, HEIGHT))

title_font = pygame.font.Font("space_invaders.ttf", 70)



def main(score):
    run = True
    while run:
        WINDOWS.blit(BACKGROUND, (0, 0))
        max_score = readFile("MaxScore.txt")
        if score > max_score:
            max_score = score
            writeFile("MaxScore.txt", score)
        score_label = title_font.render("Your Score: {}".format(score), True, (250, 141, 44))
        max_label = title_font.render("Highest Score: {}".format(max_score), True, (250, 141, 44))
        title_label = title_font.render("Game Over", True, (255, 255, 255))
        WINDOWS.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 150))
        WINDOWS.blit(score_label, (WIDTH / 2 - score_label.get_width() / 2, 250))
        WINDOWS.blit(max_label, (WIDTH / 2 - max_label.get_width() / 2, 350))
        pause_label1 = title_font.render("Press SPACE to restart", True, (250, 141, 44))
        pause_label2 = title_font.render("Press ESC to quit", True, (250, 141, 44))
        WINDOWS.blit(pause_label1, (WIDTH / 2 - pause_label1.get_width() / 2, 450))
        WINDOWS.blit(pause_label2, (WIDTH / 2 - pause_label2.get_width() / 2, 550))
        pygame.display.update()
        # Nhấn phím cách để bắt đầu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def readFile(file):
    f = open(file, "r")
    res = int(f.read())
    f.close()
    return res

def writeFile(file, maxx):
    f = open(file, "w")
    f.write(str(maxx))
    f.close()
