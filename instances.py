from imagesimport import *
from settings import *
from enviro import *

platform = []
for i in range(9):
    platform.append(SimplePlatform(tiles[1], GRID[i][9]))

class Menu:
    def __init__(self):
        pass

    def draw(self, surf):
        surf.blit(backgrounds[0],(0,0))

        for i in platform:
            i.draw(surf)


    def update(self):
        pass
