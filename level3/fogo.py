import pygame

import level2.terra
import introduction.introLevel3
import music.playMusic

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("NÍVEL 3 - FOGO")

# Colors
BLUE = (102, 153, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font_music = pygame.font.SysFont("arial", 20, bold=False, italic=False)
font = pygame.font.SysFont("twcen", 30, bold=False, italic=False)
font1 = pygame.font.SysFont("arial", 40, bold=False, italic=False)

# Texts
textMusic = font_music.render("M = music on/off", True, BLUE, 1)
scoreboard = font.render("Placar:", True, BLUE, 1)
text1 = font1.render("Pontuação final: ", True, WHITE)
text2 = font1.render("Siga para o próximo nível  =)", True, BLACK)
text_end = font1.render("Parabéns, você recolheu todos os lixos eletrônicos !", True, BLUE, 1)

# Score
score = level2.terra.score

# Images
sprite = pygame.image.load("level3/assets/sprite.png")
# sprite_teste = pygame.image.load("level3/assets/sprite-teste.png")

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
toasterGrey = pygame.transform.scale(toasterGrey, (200, 200))

trashA = [lamp, phone, apple, note]
trashB = [tennis, drawer, bottle, toaster]

# Music
song = introduction.introLevel3.song
if song:
    pygame.mixer.music.load("music/fogo_musica.mp3")
    pygame.mixer.music.play(-1)


def plot_trash():
    x_a = 40
    for i in range(len(trashA)):
        screen.blit(trashA[i], (x_a, 80))
        x_a += 200
    x_b = 40
    for i in range(len(trashB)):
        screen.blit(trashB[i], (x_b, 350))
        x_b += 200


def end(pts_end):
    global song
    pygame.time.delay(2500)
    end_level = True
    while end_level:
        for event_end in pygame.event.get():
            if event_end.type == pygame.QUIT:
                pygame.quit()
            if event_end.type == pygame.KEYDOWN and event_end.key == pygame.K_m:
                if song:
                    song = music.playMusic.music_off()
                else:
                    pygame.mixer.music.load("music/fogo_musica.mp3")
                    pygame.mixer.music.play(-1)
                    song = music.playMusic.music_on()
        screen.fill(BLUE)
        screen.blit(text1, (305, 250))
        screen.blit(text2, (250, 300))
        points_end = font1.render(pts_end, True, WHITE)
        screen.blit(points_end, (550, 250))
        pygame.display.update()
        pygame.time.delay(2500)
        break


def get_frame(gId, colunas, altura, largura, espaco_h, espaco_v, margem, topo):
    global sprite
    linha = gId // colunas
    coluna = gId % colunas
    x = (coluna * (largura + espaco_h)) + margem
    y = (linha * (altura + espaco_v)) + topo
    return sprite.subsurface(pygame.Rect((x, y), (largura, altura)))


listaBottom = [12, 13, 14, 15]
listaLeft = [8, 9, 10, 11]
listaRight = [4, 5, 6, 7]
listaTop = [16, 17, 18, 19]

'''
listaBottom = [0, 1, 2, 3, 4]
listaLeft = [5, 6, 7, 8, 9]
listaRight = [10, 11, 12, 13, 14]
listaTop = [15, 16, 17, 18, 19]'''

listaQuadros = listaRight
quadro = 0

vel = 10
mover = False
fps = pygame.time.Clock()
x = 20
y = 55
limit = ''

pts = str(score[2])
points = font.render(pts, True, BLUE, 1)
count = 0
levelActive = True
while levelActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if song:
                song = music.playMusic.music_off()
            else:
                pygame.mixer.music.load("music/fogo_musica.mp3")
                pygame.mixer.music.play(-1)
                song = music.playMusic.music_on()
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

    g_id = listaQuadros[quadro]
    frame = get_frame(g_id, 4, 50, 50, 0, 0, 0, 0)
    # frame = get_frame(g_id, 5, 40, 40, 0, 0, 0, 0)
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
    if limit == 'down' and y >= 550:
        y = 550

    screen.blit(background, (0, 0))
    screen.blit(textMusic, (10, 10))
    screen.blit(scoreboard, (730, 15))
    screen.blit(frame, (x, y))

    if 80 < x < 200 and 89 < y < 272 and trashA[0] == lamp:  # Alteração nos lixos e pontuação
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(500)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        count += 1
        score[2] += 10  # Ganha 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashA.remove(lamp)
        trashA.insert(0, lampGrey)

    if 320 < x < 438 and 80 < y < 260 and trashA[1] == phone:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        count += 1
        score[2] += 10  # Ganha 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashA.remove(phone)
        trashA.insert(1, phoneGrey)

    if 505 < x < 590 and 123 < y < 260 and trashA[2] == apple:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        score[2] -= 10  # Perde 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashA.remove(apple)
        trashA.insert(2, appleGrey)

    if 670 < x < 810 and 125 < y < 230 and trashA[3] == note:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        count += 1
        score[2] += 10  # Ganha 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashA.remove(note)
        trashA.insert(3, noteGrey)

    if 50 < x < 227 and 425 < y < 512 and trashB[0] == tennis:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        score[2] -= 10  # Perde 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashB.remove(tennis)
        trashB.insert(0, tennisGrey)

    if 290 < x < 392 and 362 < y < 528 and trashB[1] == drawer:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        count += 1
        score[2] += 10  # Ganha 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashB.remove(drawer)
        trashB.insert(1, drawerGrey)

    if 510 < x < 568 and 390 < y < 536 and trashB[2] == bottle:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        score[2] -= 10  # Perde 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashB.remove(bottle)
        trashB.insert(2, bottleGrey)

    if 703 < x < 773 and 397 < y < 517 and trashB[3] == toaster:
        pygame.mixer.music.load("music/efeitoSonoro_fogo.mp3")
        pygame.mixer.music.play(0)
        pygame.time.delay(400)
        if song:
            pygame.mixer.music.load("music/fogo_musica.mp3")
            pygame.mixer.music.play(-1)
            song = music.playMusic.music_on()
        else:
            song = music.playMusic.music_off()
        count += 1
        score[2] += 10  # Ganha 10 pontos
        pts = str(score[2])
        points = font.render(pts, True, BLUE, 1)
        trashB.remove(toaster)
        trashB.insert(3, toasterGrey)

    if count >= 5:  # Contador para sair do nível
        screen.blit(background, (0, 0))
        screen.blit(text_end, (80, 280))
        pygame.display.update()
        end(pts)
        break

    plot_trash()
    screen.blit(points, (830, 15))
    pygame.display.update()
    fps.tick(15)

pygame.quit()
