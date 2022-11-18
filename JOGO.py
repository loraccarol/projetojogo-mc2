from time import sleep
import pygame


import introduction.introGame
import introduction.introLevel1
import level1.level1
import introduction.introLevel2
import level2.terra
import introduction.introLevel3
import level3.fogo
import introduction.introLevel4
import level4.ar

pygame.init()


def level1():
    level1.level1


def level2():
    level2.terra


def level3():
    level3.fogo


def level4():
    level4.ar


def main():
    introduction.introGame
    sleep(1)
    introduction.introLevel1
    sleep(1)
    level1()
    introduction.introLevel2
    level2()
    introduction.introLevel3
    level3()
    introduction.introLevel4
    level4()


main()
pygame.quit()
