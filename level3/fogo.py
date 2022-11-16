import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("NÍVEL 3 - FOGO")

# Colors
BLACK = (255, 255, 255)

# Fonts
font_music = pygame.font.SysFont("arial", 20, bold=False, italic=False)
font = pygame.font.SysFont("twcen", 30, bold=False, italic=False)

# Texts
textMusic = font_music.render("M = music on/off", True, BLACK)
scoreboard = font.render("Placar:", True, BLACK)

# Images
sprite = pygame.image.load("level3/assets/sprite.png")

background = pygame.image.load("level3/assets/fogobackground.png")
background = pygame.transform.scale(background, (900, 600))

apple = pygame.image.load("level3/assets/apple.png")
apple = pygame.transform.scale(apple, (200, 200))
appleGrey = pygame.image.load("level3/assets/appleGrey.png")
appleGrey = pygame.transform.scale(appleGrey, (200, 200))

bottle = pygame.image.load("level3/assets/bottle.png")
bottle = pygame.transform.scale(bottle, (200, 200))
bottleGrey = pygame.image.load("level3/assets/bottleGrey.png")
bottleGrey = pygame.transform.scale(bottleGrey, (200, 200))

lamp = pygame.image.load("level3/assets/lamp.png")
lamp = pygame.transform.scale(lamp, (200, 200))
lampGrey = pygame.image.load("level3/assets/lampGrey.png")
lampGrey = pygame.transform.scale(lampGrey, (200, 200))

note = pygame.image.load("level3/assets/notebook.png")
note = pygame.transform.scale(note, (200, 200))
noteGrey = pygame.image.load("level3/assets/notebookGrey.png")
noteGrey = pygame.transform.scale(noteGrey, (200, 200))

phone = pygame.image.load("level3/assets/phone.png")
phone = pygame.transform.scale(phone, (200, 200))
phoneGrey = pygame.image.load("level3/assets/phoneGrey.png")
phoneGrey = pygame.transform.scale(phoneGrey, (200, 200))

drawer = pygame.image.load("level3/assets/drawer.png")
drawer = pygame.transform.scale(drawer, (200, 200))
drawerGrey = pygame.image.load("level3/assets/drawerGrey.png")
drawerGrey = pygame.transform.scale(drawerGrey, (200, 200))

tennis = pygame.image.load("level3/assets/tennis.png")
tennis = pygame.transform.scale(tennis, (200, 200))
tennisGrey = pygame.image.load("level3/assets/tennisGrey.png")
tennisGrey = pygame.transform.scale(tennisGrey, (200, 200))

toaster = pygame.image.load("level3/assets/toaster.png")
toaster = pygame.transform.scale(toaster, (200, 200))
toasterGrey = pygame.image.load("level3/assets/toasterGrey.png")
toasterGrey = pygame.transform.scale(appleGrey, (200, 200))

trashA = [lamp, phone, apple, note]
trashB = [tennis, drawer, bottle, toaster]


def get_frame(gId, colunas, altura, largura, espaco_h, espaco_v, margem, topo):
    global sprite
    linha = gId // colunas
    coluna = gId % colunas
    x = (coluna * (largura + espaco_h)) + margem
    y = (linha * (altura + espaco_v)) + topo
    return sprite.subsurface(pygame.Rect((x, y), (largura, altura)))


listaBottom = [0, 1, 2, 3, 4]
listaLeft = [5, 6, 7, 8, 9]
listaRight = [10, 11, 12, 13, 14]
listaTop = [15, 16, 17, 18, 19]

listaQuadros = listaRight
quadro = 0

vel = 10
mover = False
fps = pygame.time.Clock()
x = 50
y = 55
limit = ''


def plot_trash():
    x_a = 40
    for i in range(len(trashA)):
        screen.blit(trashA[i], (x_a, 80))
        x_a += 200
    x_b = 40
    for i in range(len(trashB)):
        screen.blit(trashB[i], (x_b, 350))
        x_b += 200


levelActive = True
while levelActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            levelActive = False
            #pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_UP or pygame.K_DOWN:
                mover = False
                quadro = 0
        if event.type == pygame.KEYDOWN:
            mover = True

    teclado = pygame.key.get_pressed()
    if teclado[pygame.K_RIGHT]:
        limit = 'right'
        x += vel
        listaQuadros = listaRight
    if teclado[pygame.K_LEFT]:
        limit = 'left'
        x -= vel
        listaQuadros = listaLeft
    if teclado[pygame.K_DOWN]:
        limit = 'down'
        y += vel
        listaQuadros = listaBottom
    if teclado[pygame.K_UP]:
        limit = 'up'
        y -= vel
        listaQuadros = listaTop

    screen.blit(background, (0, 0))
    screen.blit(textMusic, (10, 10))
    screen.blit(scoreboard, (730, 15))

    g_id = listaQuadros[quadro]
    frame = get_frame(g_id, 5, 40, 40, 0, 0, 0, 0)
    if mover:
        quadro += 1
    if quadro >= len(listaQuadros):
        quadro = 0

    if limit == 'right' and x >= 860:
        x = 860
    if limit == 'left' and x <= 0:
        x = 0
    if limit == 'up' and y <= 45:
        y = 45
    if limit == 'down' and y >= 560:
        y = 560

    screen.blit(frame, (x, y))

    if 80 < x < 200 and 89 < y < 272 and trashA[0] == lamp:
        print("oi")
        trashA.remove(lamp)
        trashA.insert(0, lampGrey)

    plot_trash()
    pygame.display.update()
    fps.tick(15)

pygame.quit()
