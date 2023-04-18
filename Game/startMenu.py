import pygame
import time
import random
from Components import components
from DemoLevel import demoLevel

pygame.init()

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)
darkGray = (34, 34, 34)
lightGray = (105, 105, 105)

bright_red = (225,0,0)
bright_green = (0,255,0)

largeText = pygame.font.Font('freesansbold.ttf',115)
smallText = pygame.font.Font('freesansbold.ttf',20)

pygame.display.set_caption('Ghost Hunt Demo')

# background music
pygame.mixer.init()
pygame.mixer.music.load('Game/Assets/ghost_hunt_opening_1_hd_-7802281804015965868.ogg')
pygame.mixer.music.play(-1, fade_ms = 2000)

clock = pygame.time.Clock()

# background imgae
displayImage = pygame.image.load("Game/Assets/anime_ghosthunt.jpg")

def exitGame():
    pygame.quit()
    quit()

def playGame():
    components.fade(600, 800)
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load('Game/Assets/Ghost-Hunt-OST-Tennenkyara-wa-go-Aikyou.ogg')
    pygame.mixer.music.play(-1, fade_ms=2000)
    demoLevel.demo()

# Start-up Menu
def gameIntro():
    intro = True
    while intro:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exitGame()
        components.gameDisplay.fill(black)
        components.gameDisplay.blit(pygame.transform.scale(displayImage, (960, 375)), ((components.display_width/2 - 960/2), (components.display_height/2 - 375/2)))
        
        # interactive buttons
        # Start
        components.button("Start", smallText, 150, 500, 100, 50, darkGray, lightGray, playGame)
        # Quit
        components.button("Exit", smallText, 550, 500, 100, 50, darkGray, lightGray, exitGame)

        pygame.display.update()
        clock.tick(60)
    
gameIntro()
