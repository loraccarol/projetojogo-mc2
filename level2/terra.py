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
    # Fonts
    font_1 = pygame.font.SysFont("poorrichard", 70, bold=False, italic=False)
    font_2 = pygame.font.SysFont("arial", 48, bold=False, italic=False)

    # Texts
    welcome = font_1.render("Nível 2", True, ORANGE)
    terra = font_1.render("T E R R A", True, ORANGE)
    instruction = font_2.render("Vamos reflorestar os biomas?", True, GREEN)

    # Images
    #plastic = pyga
    #tree = pygame.image.load("level2/images/tree.png")
    metal = pygame.image.load("level2/metal_pixel.png")

    def plot_symbols():
        tree_x = 15
        for i in range(0, 5):
            screen.blit(metal, (tree_x, 410))
            tree_x += 180

    def plot_green():
        teste = True
        while teste:
            screen.fill((0, 255, 0))
            plot_symbols()
            pygame.display.update()
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    teste = False
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    pos2 = pygame.mouse.get_pos()
                    if 59 < pos2[0] < 459:
                        # somar ou subtrair os pontos
                        print("AQUI")
                        plot_blue()
                        teste = False

    def plot_blue():
        teste = True
        while teste:
            screen.fill((0, 0, 255))
            plot_symbols()
            pygame.display.update()
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    teste = False
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    pos2 = pygame.mouse.get_pos()
                    if 59 < pos2[0] < 459:
                        # somar ou subtrair os pontos
                        print("AQUI")
                        teste = False

    start = True
    while start:
        for start_event in pygame.event.get():
            if start_event.type == pygame.QUIT:
                pygame.quit()
            else:
                screen.fill(BEIGE)
                screen.blit(terra, (300, 300))
                pygame.display.update()
                start = False

    pygame.time.delay(1000)
    screen.blit(welcome, (300, 500))
    pygame.display.update()
    pygame.time.delay(1000)
    active = True
    while active:
        #print(pygame.mouse.get_pos())
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pygame.quit()
            screen.fill((255, 0, 0))
            plot_symbols()
            #tree_x = 60
            #for i in range(0, 4):
            #    screen.blit(tree, (tree_x, 410))
            #    tree_x += 210
            #for event2 in pygame.event.get():
            if event1.type == pygame.MOUSEBUTTONDOWN:
                pos1 = pygame.mouse.get_pos()
                if 59 < pos1[0] < 459:
                    # somar ou subtrair os pontos
                    plot_green()
                    active = False
                if 400 < pos1[0] < 800:
                    print("OII")
                    plot_green()
                    active = False
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
