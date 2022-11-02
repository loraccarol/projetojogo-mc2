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

# Score
score = [0, 0, 0, 0]  # Cada posição guarda o total de pontos por nível


def level1():
    pass


def level2():
    # Fonts
    font_1 = pygame.font.SysFont("poorrichard", 90, bold=False, italic=False)
    font_2 = pygame.font.SysFont("arial", 48, bold=False, italic=False)

    # Texts
    #welcome = font_1.render("Nível 2", True, ORANGE)
    terra = font_1.render("T E R R A", True, ORANGE)
    instruction = font_2.render("Vamos reflorestar os biomas?", True, GREEN)

    # Images
    plastic = pygame.image.load("level2/images/plastico_pixel.png")
    glass = pygame.image.load("level2/images/vidro_pixel.png")
    paper = pygame.image.load("level2/images/papel_pixel.png")
    metal = pygame.image.load("level2/images/metal_pixel.png")
    organic = pygame.image.load("level2/images/organico_pixel.png")
    images = (metal, plastic, organic, paper, glass)

    def plot_symbols():
        firstPosition = 25
        for i in range(len(images)):
            screen.blit(images[i], (firstPosition, 400))
            firstPosition += 175

    def plot_green():
        green = True
        while green:
            screen.fill((0, 255, 0))
            plot_symbols()
            pygame.display.update()
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    pygame.quit()
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = pygame.mouse.get_pos()
                    if 25 < pos1[0] < 175 and 400 < pos1[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_blue()
                        green = False
                    if 200 < pos1[0] < 350 and 400 < pos1[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_blue()
                        green = False
                    if 375 < pos1[0] < 525 and 400 < pos1[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_blue()
                        green = False
                    if 550 < pos1[0] < 700 and 400 < pos1[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_blue()
                        green = False
                    if 725 < pos1[0] < 875 and 400 < pos1[1] < 550:  # Opção correta - vidro
                        score[1] += 5  # Pontuação
                        print(score[1])
                        plot_blue()
                        green = False

    def plot_blue():
        blue = True
        while blue:
            screen.fill((0, 0, 255))
            plot_symbols()
            pygame.display.update()
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    pygame.quit()
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    pos2 = pygame.mouse.get_pos()
                    if 25 < pos2[0] < 175 and 400 < pos2[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_yellow()
                        blue = False
                    if 200 < pos2[0] < 350 and 400 < pos2[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_yellow()
                        blue = False
                    if 375 < pos2[0] < 525 and 400 < pos2[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_yellow()
                        blue = False
                    if 550 < pos2[0] < 700 and 400 < pos2[1] < 550:  # Opção correta - papel
                        score[1] += 5  # Pontuação
                        print(score[1])
                        plot_yellow()
                        blue = False
                    if 725 < pos2[0] < 875 and 400 < pos2[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_yellow()
                        blue = False

    def plot_yellow():
        yellow = True
        while yellow:
            screen.fill((255, 255, 0))
            plot_symbols()
            pygame.display.update()
            for event3 in pygame.event.get():
                if event3.type == pygame.QUIT:
                    pygame.quit()
                if event3.type == pygame.MOUSEBUTTONDOWN:
                    pos3 = pygame.mouse.get_pos()
                    if 25 < pos3[0] < 175 and 400 < pos3[1] < 550:  # Opção correta - metal
                        score[1] += 5  # Pontuação
                        print(score[1])
                        plot_brown()
                        yellow = False
                    if 200 < pos3[0] < 350 and 400 < pos3[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_brown()
                        yellow = False
                    if 375 < pos3[0] < 525 and 400 < pos3[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_brown()
                        yellow = False
                    if 550 < pos3[0] < 700 and 400 < pos3[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_brown()
                        yellow = False
                    if 725 < pos3[0] < 875 and 400 < pos3[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        plot_brown()
                        yellow = False

    def plot_brown():
        pass

    intro = True
    while intro:
        for intro_event in pygame.event.get():
            if intro_event.type == pygame.QUIT:
                pygame.quit()
            else:
                screen.fill(BEIGE)
                screen.blit(terra, (280, 250))
                pygame.display.update()
                intro = False

    pygame.time.delay(2000)
    #plotar o bichinho aqui
    #screen.blit(welcome, (300, 500))
    #pygame.display.update()
    #pygame.time.delay(1000)
    levelActive = True
    while levelActive:
        #print(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill((255, 0, 0))  # Red
            plot_symbols()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 25 < pos[0] < 175 and 400 < pos[1] < 550:  # Opção errada
                    score[1] -= 5  # Pontuação
                    print(score[1])
                    plot_green()
                    levelActive = False
                if 200 < pos[0] < 350 and 400 < pos[1] < 550:  # Opção correta - plástico
                    score[1] += 5  # Pontuação
                    print(score[1])
                    plot_green()
                    levelActive = False
                if 375 < pos[0] < 525 and 400 < pos[1] < 550:  # Opção errada
                    score[1] -= 5  # Pontuação
                    print(score[1])
                    plot_green()
                    levelActive = False
                if 550 < pos[0] < 700 and 400 < pos[1] < 550:  # Opção errada
                    score[1] -= 5  # Pontuação
                    print(score[1])
                    plot_green()
                    levelActive = False
                if 725 < pos[0] < 875 and 400 < pos[1] < 550:  # Opção errada
                    score[1] -= 5  # Pontuação
                    print(score[1])
                    plot_green()
                    levelActive = False
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
