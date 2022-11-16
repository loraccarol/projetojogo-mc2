import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("NÍVEL 2 - TERRA")

# Colors
GREEN = (0, 204, 0)
BLUE = (0, 51, 204)
YELLOW = (255, 255, 26)
BROWN = (204, 102, 0)
RED = (255, 26, 26)
BLUE1 = (102, 153, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("twcen", 30, bold=False, italic=False)
font1 = pygame.font.SysFont("arial", 40, bold=False, italic=False)

# Texts
scoreboard = font.render("Placar:", True, BLACK)
text1 = font1.render("Pontuação final: ", True, WHITE)
text2 = font1.render("Siga para o próximo nível  =)", True, BLACK)

# Images
plastic = pygame.image.load("level2/assets/plastico_pixel.png")
glass = pygame.image.load("level2/assets/vidro_pixel.png")
paper = pygame.image.load("level2/assets/papel_pixel.png")
metal = pygame.image.load("level2/assets/metal_pixel.png")
organic = pygame.image.load("level2/assets/organico_pixel.png")
images = (metal, plastic, organic, paper, glass)

# Score
score = [0, 0, 0, 0]  # Cada posição guarda o total de pontos por nível


def level2():
    def plot_symbols():
        firstPosition = 25
        for i in range(len(images)):
            screen.blit(images[i], (firstPosition, 400))
            firstPosition += 175

    def plot_green():
        pts2 = str(score[1])
        points2 = font.render(pts2, True, BLACK)
        green = True
        while green:
            screen.fill(GREEN)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))      # Placar
            screen.blit(points2, (810, 40))         # Pontuação
            pygame.display.update()
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    pygame.quit()
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = pygame.mouse.get_pos()
                    if 25 < pos1[0] < 175 and 400 < pos1[1] < 550:   # Opção errada
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
        pts3 = str(score[1])
        points3 = font.render(pts3, True, BLACK)
        blue = True
        while blue:
            screen.fill(BLUE)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))     # Placar
            screen.blit(points3, (810, 40))        # Pontuação
            pygame.display.update()
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    pygame.quit()
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    pos2 = pygame.mouse.get_pos()
                    if 25 < pos2[0] < 175 and 400 < pos2[1] < 550:   # Opção errada
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
        pts4 = str(score[1])
        points4 = font.render(pts4, True, BLACK)
        yellow = True
        while yellow:
            screen.fill(YELLOW)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))     # Placar
            screen.blit(points4, (810, 40))        # Pontuação
            pygame.display.update()
            for event3 in pygame.event.get():
                if event3.type == pygame.QUIT:
                    pygame.quit()
                if event3.type == pygame.MOUSEBUTTONDOWN:
                    pos3 = pygame.mouse.get_pos()
                    if 25 < pos3[0] < 175 and 400 < pos3[1] < 550:   # Opção correta - metal
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
        pts5 = str(score[1])
        points5 = font.render(pts5, True, BLACK)
        brown = True
        while brown:
            screen.fill(BROWN)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))     # Placar
            screen.blit(points5, (810, 40))        # Pontuação
            pygame.display.update()
            for event4 in pygame.event.get():
                if event4.type == pygame.QUIT:
                    pygame.quit()
                if event4.type == pygame.MOUSEBUTTONDOWN:
                    pos4 = pygame.mouse.get_pos()
                    if 25 < pos4[0] < 175 and 400 < pos4[1] < 550:   # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        end()
                        brown = False
                    if 200 < pos4[0] < 350 and 400 < pos4[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        end()
                        brown = False
                    if 375 < pos4[0] < 525 and 400 < pos4[1] < 550:  # Opção correta - orgânico
                        score[1] += 5  # Pontuação
                        print(score[1])
                        end()
                        brown = False
                    if 550 < pos4[0] < 700 and 400 < pos4[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        end()
                        brown = False
                    if 725 < pos4[0] < 875 and 400 < pos4[1] < 550:  # Opção errada
                        score[1] -= 5  # Pontuação
                        print(score[1])
                        end()
                        brown = False

    def end():
        pts6 = str(score[1])
        points6 = font.render(pts6, True, (0, 0, 0))
        end_level = True
        while end_level:
            screen.fill(BROWN)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))     # Placar
            screen.blit(points6, (810, 40))        # Pontuação
            pygame.display.update()
            for event5 in pygame.event.get():
                if event5.type == pygame.QUIT:
                    pygame.quit()
            pygame.time.delay(1000)
            screen.fill(BLUE1)
            screen.blit(text1, (305, 250))
            screen.blit(text2, (250, 300))
            points6 = font1.render(pts6, True, WHITE)
            screen.blit(points6, (550, 250))
            pygame.display.update()
            pygame.time.delay(2500)
            break
            # return score[1]

    pts1 = str(score[1])
    points1 = font.render(pts1, True, BLACK)
    levelActive = True
    while levelActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(RED)
            plot_symbols()
            screen.blit(scoreboard, (715, 40))     # Placar
            screen.blit(points1, (810, 40))        # Pontuação
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 25 < pos[0] < 175 and 400 < pos[1] < 550:   # Opção errada
                    score[1] -= 5  # Pontuação
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


level2()
pygame.quit()
