from time import sleep
import pygame

import introduction.introGame
import introduction.introLevel1
import introduction.introLevel2
import level2.terra
import introduction.introLevel3
import introduction.introLevel4
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
    introduction.introGame
    introduction.introLevel1
    sleep(1)
    introduction.introLevel2
    sleep(1)
    level2()
    sleep(1)
    introduction.introLevel3
    sleep(1)
    introduction.introLevel4
    level4()


main()
pygame.quit()
