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

bright_red = (225,0,0)
bright_green = (0,255,0)

largeText = pygame.font.Font('freesansbold.ttf',115)
smallText = pygame.font.Font('freesansbold.ttf',20)

pygame.display.set_caption('Ghost Hunt Demo')

# background music
pygame.mixer.init()
pygame.mixer.music.load('Game/Assets/ghost_hunt_opening_1_hd_-7802281804015965868.ogg')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

def exitGame():
    pygame.quit()
    quit()

def playGame():
    demoLevel.demo()

# Start-up Menu
def game_intro():
    intro = True
    while intro:
        
        # background imgae
        pygame.display.set_caption("background image") 
        displayImage = pygame.image.load("Game/Assets/anime_ghosthunt.jpg")

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exitGame()
        components.gameDisplay.fill(black)
        components.gameDisplay.blit(pygame.transform.scale(displayImage, (960, 375)), ((components.display_width/2 - 960/2),(components.display_height/2 - 375/2)))
        
        # interactive buttons

        # Start
        components.button("Start", smallText, 150, 450, 100, 50, green, bright_green, playGame)
        # Quit
        components.button("Exit", smallText, 550, 450, 100, 50, red, bright_red, exitGame)

        pygame.display.update()
        clock.tick(15)
    
game_intro()
