import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("ELEMENT")

# Colors
BEIGE = (255, 191, 128)
PINK = (172, 57, 57)
BLUE1 = (102, 153, 255)
BLUE2 = (153, 255, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.get_default_font()
font1 = pygame.font.SysFont(font, 40)
font2 = pygame.font.SysFont(font, 30)
font3 = pygame.font.SysFont("twcen", 20, bold=False, italic=False)
font_intro = pygame.font.SysFont("poorrichard", 90, bold=False, italic=False)
font_music = pygame.font.SysFont("arial", 20, bold=False, italic=False)

# Texts
fire = font_intro.render("F O G O", True, PINK)
textMusic = font_music.render("M = music on/off", True, BLACK)

text1 = font1.render("Olá, eu me chamo OLIVER", True, BLUE2)
text2 = font1.render("e vou te ajudar no próximo nível!", True, BLUE2)

text3 = font2.render("Você sabe o que é lixo eletrônico?", True, BLACK)
text4 = font2.render("São os aparelhos eletrônicos que são jogados fora ou não funcionam mais,", True, BLACK)
text5 = font2.render("como pilhas, computadores e celulares. Por serem muito tecnológicos, eles", True, BLACK)
text6 = font2.render("precisam ter um descarte diferente.", True, BLACK)
text7 = font2.render("Você pode ajudar a Sol a separar o lixo eletrônico do normal?", True, WHITE)
text8 = font2.render("Clique com o mouse em todos que encontrar.", True, WHITE)
text9 = font2.render("Pontuação...", True, WHITE)
text10 = font2.render("Boa sorte!!", True, BLUE2)

end = font3.render("pressione a tecla S para continuar", True, BLACK)

# Images
oliver = pygame.image.load("level3/assets/oliver.png")
oliver = pygame.transform.scale(oliver, (200, 200))

screen.fill(BEIGE)
screen.blit(fire, (300, 250))
pygame.display.update()
pygame.time.delay(2000)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            done = True
        screen.fill(BLUE1)
        screen.blit(textMusic, (10, 10))
        screen.blit(oliver, (660, 25))
        screen.blit(text1, (25, 70))
        screen.blit(text2, (25, 110))
        screen.blit(text3, (25, 210))
        screen.blit(text4, (25, 240))
        screen.blit(text5, (25, 270))
        screen.blit(text6, (25, 300))
        screen.blit(text7, (25, 380))
        screen.blit(text8, (25, 410))
        screen.blit(text9, (25, 440))
        screen.blit(text10, (25, 470))
        screen.blit(end, (570, 540))

        pygame.display.update()

pygame.quit()
