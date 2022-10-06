import pygame

pygame.init()

# Tela
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Padrão")


done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pygame.display.update()

pygame.quit()