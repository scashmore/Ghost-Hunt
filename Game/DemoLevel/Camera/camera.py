import pygame

class CameraGroup(pygame.sprite.Group):
    
    def __init__(self, map):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.halfW = self.displaySurface.get_size()[0] // 2
        self.halfH = self.displaySurface.get_size()[1] // 2
        self.groundSurface = pygame.image.load(map)
        self.groundRect = self.groundSurface.get_rect(topleft = (0, 0))
    
    def centerCamera(self, target):
        self.offset.x = target.rect.centerx - self.halfW
        self.offset.y =  target.rect.centery - self.halfH
    
    def customDraw(self,user):
        self.centerCamera(user)
        groundOffset = self.groundRect.topleft - self.offset
        self.displaySurface.blit(self.groundSurface, groundOffset)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)