import pygame

import music.playMusic

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("ELEMENTS - MENU")

score = [0, 0, 0, 0]

# Colors
BEIGE = (255, 191, 128)
PINK = (172, 57, 57)
BLUE = (148, 184, 184)
GREEN = (19, 58, 19)

# Fonts
font1 = pygame.font.SysFont("poorrichard", 80, bold=False, italic=False)
font2 = pygame.font.SysFont("poorrichard", 30, bold=False, italic=False)
font3 = pygame.font.SysFont("arial", 22, bold=False, italic=False)
font_music = pygame.font.SysFont("arial", 20, bold=False, italic=False)

# Texts
title = font1.render("E L E M E N T S", True, PINK)
text = font2.render("pressione a tecla S para continuar", True, (115, 77, 38))
intro1 = font3.render("Olá, somos um grupo de amigos e precisamos de você para tornar a Terra "
                      "um planeta melhor!", True, GREEN)
intro2 = font3.render("Ajude a nossa amiga Sol a realizar os desafios ambientais dos próximos níveis!", True, GREEN)
intro3 = font3.render("Vamos te auxiliar ao longo dessa jornada! Boa sorte !!", True, GREEN)
textMusic = font_music.render("M = music on/off", True, (0, 0, 0))

# Images
elements = pygame.image.load("introduction/assets/elements-pixel-art.png")
elements = pygame.transform.scale(elements, (350, 308))
crush = pygame.image.load("level1/assets/crush.png")
crush = pygame.transform.scale(crush, (200, 200))
oliver = pygame.image.load("level3/assets/oliver.png")
oliver = pygame.transform.scale(oliver, (200, 200))
rebeca = pygame.image.load("level2/assets/rebeca.png")
rebeca = pygame.transform.scale(rebeca, (200, 200))
lucia = pygame.image.load("level4/assets/lucia.png")
lucia = pygame.transform.scale(lucia, (200, 200))
sol = pygame.image.load("introduction/assets/sol.png")
sol = pygame.transform.scale(sol, (120, 188))

# Music
pygame.mixer.music.load("music/411165__inspectorj__piano-bach-fantasia-a-h6-ms.mp3")
pygame.mixer.music.play(-1)
song = True

startGame = True
while startGame:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            pygame.quit()
        if event1.type == pygame.KEYUP and event1.key == pygame.K_m:
            if song:
                song = music.playMusic.music_off()
            else:
                song = music.playMusic.music_on()
        if event1.type == pygame.KEYUP and event1.key == pygame.K_s:
            startGame = False
    screen.fill(BEIGE)
    screen.blit(textMusic, (10, 10))
    screen.blit(title, (230, 30))
    screen.blit(elements, (270, 160))
    screen.blit(text, (265, 530))
    pygame.display.update()

startAnimals = True
while startAnimals:
    for event2 in pygame.event.get():
        if event2.type == pygame.QUIT:
            pygame.quit()
        if event2.type == pygame.KEYUP and event2.key == pygame.K_m:
            if song:
                song = music.playMusic.music_off()
            else:
                song = music.playMusic.music_on()
        if event2.type == pygame.KEYUP and event2.key == pygame.K_s:
            startAnimals = False
    screen.fill(BLUE)
    screen.blit(textMusic, (10, 10))
    screen.blit(crush, (25, 35))
    screen.blit(oliver, (225, 35))
    screen.blit(rebeca, (445, 35))
    screen.blit(lucia, (670, 47))
    screen.blit(sol, (55, 370))
    screen.blit(intro1, (65, 280))
    screen.blit(intro2, (115, 320))
    screen.blit(intro3, (220, 360))
    screen.blit(text, (265, 530))
    pygame.display.update()

#pygame.mixer.music.stop()
pygame.quit()
