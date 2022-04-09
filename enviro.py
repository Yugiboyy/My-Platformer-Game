
class SimplePlatform:
    def __init__(self, img, pos):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = pos

    def draw(self, surf):
        surf.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        pass

    def checkCorners(self):
        pass
