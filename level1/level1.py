import pygame
import random

import introduction.introLevel1
import music.playMusic

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('NÍVEL 1 - ÁGUA')

# Score
score = [0, 0, 0, 0]  # Cada posição guarda o total de pontos por nível

# Fonts
font = pygame.font.SysFont('sans', 40)
font_music = pygame.font.SysFont("arial", 20, bold=False, italic=False)

# Music
song = introduction.introLevel1.song
if song:
    pygame.mixer.music.load("music/agua_musica.mp3")
    pygame.mixer.music.play(-1)


def level1():
    background = pygame.image.load("level1/assets/ocean.png")
    background = pygame.transform.scale(background, SIZE)

    janela = pygame.display.set_mode((900, 600))

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("level1/assets/mergulhador.png")
            self.image = pygame.transform.scale(self.image, (340, 180))
            self.rect = self.image.get_rect()
            self.placar = 0

        def render(self, janela):
            janela.blit(self.image, self.rect)

        def update(self, tecla):
            if tecla[pygame.K_UP]:
                self.rect.move_ip(0, -5)
            if tecla[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
            if tecla[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_w:
                self.rect.right = screen_w
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= screen_h:
                self.rect.bottom = screen_h

    class Canudo(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("level1/assets/canudo.png")
            self.image = pygame.transform.scale(self.image, (80, 50))
            self.rect = self.image.get_rect(
                center=(
                    random.randint(screen_w + 20, screen_w + 100),
                    random.randint(0, screen_h),
                )
            )
            self.speed = random.randint(2, 5)

        def render(self, janela):
            janela.blit(self.image, self.rect)

        def update(self, player):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()
            if self.rect.colliderect(player.rect):
                player.placar += 1
                self.kill()

    ADDCANUDO = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDCANUDO, 500)
    player = Player()
    canudos = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    global song
    clock = pygame.time.Clock()
    jogoAtivo = True
    while jogoAtivo:
        screen.blit(background, (0, 0))
        clock.tick(20)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:
                if song:
                    song = music.playMusic.music_off()
                else:
                    pygame.mixer.music.load("music/agua_musica.mp3")
                    pygame.mixer.music.play(-1)
                    song = music.playMusic.music_on()

            elif evento.type == ADDCANUDO:
                new_canudo = Canudo()
                canudos.add(new_canudo)
                all_sprites.add(new_canudo)

        tecla = pygame.key.get_pressed()
        player.update(tecla)
        player.render(janela)
        for ponto in canudos:
            ponto.update(player)
            ponto.render(janela)
            if player.placar == 20:
                score[0] = player.placar
                jogoAtivo = False
        points = font.render('Placar: ' + str(player.placar), True, (255, 0, 0))
        janela.blit(points, (600, 50))
        textMusic = font_music.render("M = music on/off", True, (0, 0, 0))
        janela.blit(textMusic, (10, 10))
        canudos.update(player)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
        pygame.display.update()
        # if pygame.sprite.spritecollideany(player, canudos):

        pygame.display.flip()


def end():
    global song
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 153, 255)
    font1 = pygame.font.SysFont("arial", 40, bold=False, italic=False)
    text1 = font1.render("Pontuação final: " + str(score[0]), True, WHITE)
    text2 = font1.render("Siga para o próximo nível  =)", True, BLACK)
    screen.fill(BLUE)
    screen.blit(text1, (305, 250))
    screen.blit(text2, (250, 300))
    pygame.display.update()
    pygame.time.delay(2500)


def main():
    level1()
    end()


main()
pygame.quit()
