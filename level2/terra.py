import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Nível 02 - Terra")

# Colors
BEIGE = (255, 191, 128)
ORANGE = (255, 71, 26)


def level1():
    pass


def level2():
    font = pygame.font.SysFont("poorrichard", 70, bold=False, italic=False)
    welcome = font.render("Nível 2", True, ORANGE)
    terra = font.render("T E R R A", True, ORANGE)

    def init():
        screen.fill(BEIGE)
        screen.blit(welcome, (335, 260))
        pygame.display.update()
        pygame.time.delay(2000)
        screen.fill(BEIGE)
        screen.blit(terra, (320, 260))
        pygame.display.update()

    init()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False


def level3():
    pass


def level4():
    pass


def main():
    # Chamar método de abertura do jogo
    level2()


main()
pygame.quit()
