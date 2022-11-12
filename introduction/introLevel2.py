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

# Texts
earth = font_intro.render("T E R R A", True, PINK)

text1 = font1.render("Olá, eu me chamo REBECA", True, BLUE2)
text2 = font1.render("e vou te ajudar no próximo nível!", True, BLUE2)

text3 = font2.render("Você conhece a coleta seletiva?", True, BLACK)
text4 = font2.render("Ela permite que o lixo seja descartado", True, BLACK)
text5 = font2.render("corretamente, e que ele possa seguir para a reciclagem!", True, BLACK)
text6 = font2.render("Ajude a Sol com os símbolos da coleta seletiva!", True, WHITE)
text7 = font2.render("Conforme a cor que estiver na tela, use o mouse para clicar no símbolo correto.", True, WHITE)
text8 = font2.render("Em cada acerto, você soma 5 pontos. Mas em cada erro, você perde 5 também.", True, WHITE)
text9 = font2.render("BOA SORTE!!", True, WHITE)

end = font3.render("pressione alguma tecla para continuar", True, BLACK)

# Images
rebeca = pygame.image.load("level2/assets/rebeca.png")
rebeca = pygame.transform.scale(rebeca, (200, 200))

screen.fill(BEIGE)
screen.blit(earth, (280, 250))
pygame.display.update()
pygame.time.delay(2000)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            done = True
        screen.fill(BLUE1)
        screen.blit(rebeca, (650, 40))
        screen.blit(text1, (25, 50))
        screen.blit(text2, (25, 90))
        screen.blit(text3, (25, 200))
        screen.blit(text4, (25, 230))
        screen.blit(text5, (25, 260))
        screen.blit(text6, (25, 340))
        screen.blit(text7, (25, 370))
        screen.blit(text8, (25, 400))
        screen.blit(text9, (25, 430))
        screen.blit(end, (550, 540))

        pygame.display.update()

pygame.quit()
