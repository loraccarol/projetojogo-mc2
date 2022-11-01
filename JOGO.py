from time import sleep
import pygame

import level2.terra
import teste.teste
import level4.ar

pygame.init()

def level1():
    pass

def level2():
    level2.terra()
    pass

def level3():
    pass

def level4():
    level4.ar()

def main():
    # Chamar método de abertura do jogo
    level2()
    sleep(1)
    teste.teste()
    level4()


main()
pygame.quit()
