import pygame
import time
from .Characters import player
from .Camera import camera
from .Text import text

pygame.init()
black = (0,0,0)
white = (255,255,255)

# background music
pygame.mixer.init()
pygame.mixer.music.load('Game/Assets/Ghost-Hunt-OST-Tennenkyara-wa-go-Aikyou.ogg')
pygame.mixer.music.play(-1, fade_ms=2000)

clock = pygame.time.Clock()
displayImage = "Game\Assets\Maps\Map002.png" 

# Camera
cameraGroup = camera.CameraGroup(displayImage)

# Player
user = player.Mai(cameraGroup)
playerGroup = pygame.sprite.Group()
playerGroup.add(user)
steps = 2     


def demo():

    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("SPR Level Demo")
    while True:
        surface.fill((255, 255, 255))
        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Keyboard presses for move position
            if  event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_LEFT]):
                    user.control(-steps, 0)
                if (keys[pygame.K_RIGHT]):
                    user.control(steps, 0)
                if (keys[pygame.K_UP]):
                    user.control(0, -steps)
                if (keys[pygame.K_DOWN]):
                    user.control(0, steps)
            if  event.type == pygame.KEYUP:
                    user.control(0, 0)
            pygame.display.update()

        cameraGroup.update(4)
        cameraGroup.customDraw(user)

        # text.textBox(surface, (0,0,0), "This is supposed to be a really long block of text. Hopefully it is and hopefully it is wrapping, as that is the idea here.", (225,225,225))

        clock.tick(60)
        pygame.display.flip()
        
        # for event in pygame.event.get():
        #     # print(event)
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()
        #     pygame.display.update()