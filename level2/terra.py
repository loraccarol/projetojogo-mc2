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
GREEN = (102, 153, 0)


def level1():
    pass


def level2():
    font_1 = pygame.font.SysFont("poorrichard", 70, bold=False, italic=False)
    font_2 = pygame.font.SysFont("arial", 48, bold=False, italic=False)
    welcome = font_1.render("Nível 2", True, ORANGE)
    terra = font_1.render("T E R R A", True, ORANGE)
    instruction = font_2.render("Vamos reflorestar os biomas?", True, GREEN)

    bioma1 = pygame.image.load("images/bioma1.png")
    bioma2 = pygame.image.load("images/bioma2.png")
    bioma3 = pygame.image.load("images/bioma3.png")
    bioma4 = pygame.image.load("images/bioma4.png")
    tree = pygame.image.load("images/tree.png")

    def init():
        screen.fill(BEIGE)
        screen.blit(welcome, (335, 260))
        pygame.display.update()
        pygame.time.delay(2000)
        screen.fill(BEIGE)
        screen.blit(terra, (320, 260))
        pygame.display.update()
        pygame.time.delay(2000)
        screen.fill((255, 187, 153))
        screen.blit(instruction, (180, 260))
        pygame.display.update()
        pygame.time.delay(2000)

    init()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        screen.blit(bioma1, (0, 0))
        tree_x = 60
        for i in range(0, 4):
            screen.blit(tree, (tree_x, 410))
            tree_x += 210

        pygame.display.update()


def level3():
    pass


def level4():
    pass


def main():
    # Chamar método de abertura do jogo
    level2()


main()
pygame.quit()
