# import pygame
# from ..Characters import player

# tilemap = [
#  'wwwwwwwwwwwwwwwwwww',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w.........P.....w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'w...............w',
#  'wwwwwwwwwwwwwwwwwwwww']

# class Block(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.game = game
#         self.layer = blockLayer
#         self.groups = self.game.allSprites, self.blocks
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.x = x*64
#         self.y = y*64
#         self.width = 64
#         self.height = 64

#         self.image = pygame.Surface([self.width, self.height])
#         self.image.fill((0, 0, 0))

#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

# def createMap():
#     for i, row in enumerate(tilemap):
#         for j, column in enumerate(row):
#             if column == "w":
#                 Block(j, i)
#             if column == "P":
#                 player.Mai()

