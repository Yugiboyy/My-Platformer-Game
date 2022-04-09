from util import *

img = Img()

oakwoodtile = img.getImg("oak_woods_v1.0/oak_woods_tileset.png")
backgrounds = img.getallImg("oak_woods_v1.0/background")
backgrounds[0] = img.resizeImg(backgrounds[0], (800, 600))
oak = Tileset(oakwoodtile)
#21 16
tiles = []
for i in range(0, int(oak.get_rect()[2]/24)):
    for a in range(0, int(oak.get_rect()[3]/24)):
        tiles.append(img.resizeImg(oak.getTile(i*24, a*24, 24, 24),(64,64)))
