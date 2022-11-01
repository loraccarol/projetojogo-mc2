from time import sleep
import pygame
import random

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Nível 04 - Ar")

# images
bg = pygame.image.load("level4/images/space.jpg")

spaceship = pygame.image.load("level4/images/spaceship.png")
spaceship = pygame.transform.scale(spaceship, (50, 50))
spaceship_rect = spaceship.get_rect()

meteor = pygame.image.load("level4/images/meteor.png")
meteor = pygame.transform.scale(meteor, (40, 34))

explosion = pygame.image.load("level4/images/explosao.png")

def get_frame (gId, columns, height, width, space_h, space_v, margin, top):
    global explosion
    linha = gId // columns #linha onde se encontra o frame desejado
    coluna = gId % columns #coluna onde se encontra o frame desejado
    x = (coluna * (width + space_h)) + margin
    y = (linha * (height + space_v)) + top
    
    return explosion.subsurface(pygame.Rect((x,y),(width,height)))

list = [0, 1, 2, 3, 4, 5, 6]
frame_list = list
initial_frame = 0
move = True

meteor_list = []

for i in range(25):
    meteor_rect = meteor.get_rect()
    meteor_rect.x = random.randrange(0, screen_w)
    meteor_rect.y = random.randrange(-1000, 10)
    meteor_list.append(meteor_rect)
    fps = pygame.time.Clock()   

vel = 10
spaceship_rect.x = 260
spaceship_rect.y = 140

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bg, (0, 0))
    screen.blit(spaceship, spaceship_rect)

    gid = frame_list[initial_frame]
    frame = get_frame(gid, 5, 40, 40, 0, 0, 0, 0)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        spaceship_rect.x -= vel
    if pressed[pygame.K_RIGHT]:
        spaceship_rect.x += vel
    if pressed[pygame.K_UP]:
        spaceship_rect.y -= vel
    if pressed[pygame.K_DOWN]:
        spaceship_rect.y += vel

    if spaceship_rect.x < 0:
        spaceship_rect.x = 0
    if spaceship_rect.x > screen_w - 50:
        spaceship_rect.x = screen_w - 50
    if spaceship_rect.y < 0:
        spaceship_rect.y = 0
    if spaceship_rect.y > screen_h - 50:
        spaceship_rect.y = screen_h - 50

    for i in range(len(meteor_list)):
        screen.blit(meteor, meteor_list[i])

        meteor_list[i][1] += 4
        if meteor_list[i][1] > screen_w:

            meteor_rect.y = random.randrange(-50, -10)
            meteor_list[i][1] = meteor_rect.y

            meteor_rect.x = random.randrange(0, screen_w)
            meteor_list[i][0] = meteor_rect.x
        
        if spaceship_rect.collidelist(meteor_list) >= 0:
            if move:
                initial_frame = initial_frame + 1
            if initial_frame >= len(frame_list):
                initial_frame = 0
            screen.blit(frame, (spaceship_rect.x, spaceship_rect.y))

    pygame.display.update()
    fps.tick(25)

pygame.quit()
