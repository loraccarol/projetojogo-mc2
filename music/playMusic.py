import pygame

pygame.init()


def music_off():
    pygame.mixer.music.pause()
    music = False
    return music


def music_on():
    pygame.mixer.music.unpause()
    music = True
    return music
