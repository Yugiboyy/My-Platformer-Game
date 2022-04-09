import os
import pygame

pygame.init()

# Don't mind this it will just help to load images in our game
# If you want me to explain it well tell me xd
class Img:
	def __init__(self):

		self.game_dir = os.path.dirname(__file__)
		self.img_dir = os.path.join(self.game_dir, "Assests")

	def getImg(self, directory):
		return pygame.image.load(os.path.join(self.img_dir, directory))

	def readfolder(self, folder_dir):
		return os.listdir(os.path.join(self.img_dir, folder_dir))

	def resizeImg(self, img, size):
		self.img = pygame.transform.scale(img, size)
		return self.img

	def getallImg(self, path):
		self.assests_dir = self.readfolder(path)
		self.assests = {}
		for i in range(0,len(self.assests_dir)):
			self.assests_dir[i] = path +"/" +self.assests_dir[i]
			self.assests[i] = self.getImg(self.assests_dir[i])
			#print(self.button_assests_dir[i])
		return self.assests

class Tileset:
	def __init__(self, tileset):
		self.tileset = tileset

	def getTile(self, x, y, w, h):
		self.img = self.tileset.subsurface(x, y, w,h)
		return self.img

	def readlvl(self, path):
		self.levels = []
		self.level = {}
		for i in os.listdir(path):
			self.levels.append(path + "/"+i)

		for i in range(len(self.levels)):
			with open(self.levels[i], "r") as file:
				lvl = file.readlines()
				for a in range(len(lvl)):
					lvl[a] = (lvl[a].strip("\n")).strip()
				self.level[i] = lvl

		return self.level


	def get_rect(self):
		return self.tileset.get_rect()

class Font:
	def __init__(self):
		pass

	def draw(self, font, text, color, pos, surf):
		self.text = self.font.render(text, False, color)
		self.rect = self.text.get_rect()
		self.rect.center = pos
		surf.blit(self.text, self.rect)

	def load_font(self, path, size):
		self.font = pygame.font.Font(path, size)
		return self.font
