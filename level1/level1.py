import pygame
import random

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Default")


def level1():
    background = pygame.image.load("assets/ocean.png")
    background = pygame.transform.scale(background, SIZE)

    janela = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('Pontos')
    font = pygame.font.SysFont('sans', 40)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("assets/mergulhador.png")
            self.image = pygame.transform.scale(self.image, (340, 180))
            self.rect = self.image.get_rect()
            self.placar = 0

            self.listaBaixo = [0, 1, 2, 3, 4]
            self.listaEsq = [5, 6, 7, 8, 9]
            self.listaDir = [10, 11, 12, 13, 14]
            self.listaCima = [15, 16, 17, 18, 19]

            self.paradoBaixo = [0]
            self.paradoEsq = [5]
            self.paradoDir = [10]
            self.paradoCima = [1]

            self.listaQuadros = self.listaDir

            self.quadro = 0

        def render(self, janela):
            janela.blit(self.image, self.rect)

        def update(self, tecla):
            if tecla[pygame.K_UP]:
                self.rect.move_ip(0, -5)
                self.listaQuadros = self.listaCima
            if tecla[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
                self.listaQuadros = self.listaBaixo
            if tecla[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.listaQuadros = self.listaDir
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
            self.image = pygame.image.load("assets/canudo.png")
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
                if player.placar == 50:
                    pygame.quit()
                self.kill()

    ADDCANUDO = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDCANUDO, 500)
    player = Player()
    canudos = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    jogoAtivo = True
    while jogoAtivo:
        screen.blit(background, (0, 0))
        clock.tick(20)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogoAtivo = False

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
        score = font.render('Placar: ' + str(player.placar), True, (255, 0, 0))
        janela.blit(score, (600, 50))
        canudos.update(player)

        # gid = player.listaQuadros[player.quadro]
        # frame = player.get_frame(gid, 5, 40, 40, 0, 0, 0, 0)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
        pygame.display.update()
        # if pygame.sprite.spritecollideany(player, canudos):

        pygame.display.flip()


def main():
    level1()


main()
pygame.quit()
