import pygame
from .spriteSheet import *

sheet = SpriteSheet("Game/Assets/GH_Sprites_Lin_Naru_Mai_v2.png")

class Mai(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        down = sheet.image_at((198, 2, 35, 47))
        left = sheet.image_at((197, 50, 35, 47))
        right = sheet.image_at((198, 98, 35, 47))
        up = sheet.image_at((198, 145, 35, 47))
        leftAni1 = sheet.image_at((149, 50, 35, 47))
        leftAni2 = sheet.image_at((245, 50, 35, 47))
        rightAni1 = sheet.image_at((150, 98, 35, 47))
        rightAni2 = sheet.image_at((246, 98, 35, 47))
        upAni1 = sheet.image_at((150, 145, 35, 47))
        upAni2 = sheet.image_at((246, 145, 35, 47))
        downAni1 = sheet.image_at((150, 2, 35, 47))
        downAni2 = sheet.image_at((246, 2, 35, 47))
        super().__init__()
        self.images = [down, left, right, up]
        self.imagesLeft = [leftAni1, left, leftAni2, left]
        self.imagesRight = [rightAni1, right, rightAni2, right]
        self.imagesUp = [upAni1, up, upAni2, up]
        self.imagesDown = [downAni1, down, downAni2, down]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 200
        self.movex = 0
        self.movey = 0
        self.frame = 0

    def control(self, x, y):
        self.movex = x
        self.movey = y
        

    def update(self, ani):
        self.rect.x = self.rect.x + self.movex 
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.imagesLeft[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.imagesRight[self.frame//ani]

        # moving up
        if self.movey < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.imagesUp[self.frame//ani]

        # moving down
        if self.movey > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.imagesDown[self.frame//ani]
        
