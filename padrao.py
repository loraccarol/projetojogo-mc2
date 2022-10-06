import pygame

pygame.init()

# Screen
screen_w = 900
screen_h = 600
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Default")

def level1():
    print("oi")
    pass

def level2():
    print("oi2")
    pass

def level3():
    print("oi3")
    pass

def level4():
    print("oi4")
    pass

def main():
    pass

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pygame.display.update()

pygame.quit()