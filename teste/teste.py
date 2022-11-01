import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("teste")

lucia = pygame.image.load("level4/images/arara pixel.png")
lucia = pygame.transform.scale(lucia, (100,100))

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True

    screen.fill((0,0,0))
    screen.blit(lucia, (750, 30))

    font = pygame.font.get_default_font()
    fontesys = pygame.font.SysFont(font, 30)
    text = fontesys.render("Olá amigos! Vamos aprender um pouco mais sobre lixo espacial?", 1, (255, 255, 255))
    text2 = fontesys.render("O lixo espacial...", 1, (255, 255, 255))
    text3 = fontesys.render("E para ajudar...", 1, (255, 255, 255))
    screen.blit(text, (20,30))
    screen.blit(text2, (20,60))
    screen.blit(text3, (20,90))

    pygame.display.update()

pygame.quit()