from settings import *
import pygame, sys
from instances import *


WIN = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

running = True

#gameInstance = [Menu()]
gameInstance = "MENU"
menu = Menu()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
    WIN.fill((0,0,0))
    if gameInstance == "MENU":
        menu.draw(WIN)
        menu.update()



    pygame.display.update()
    pygame.display.flip()
