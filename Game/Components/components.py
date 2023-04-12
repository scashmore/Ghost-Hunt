import pygame

# Game display
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))


# Text Object
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

# Buttons
def button(msg, textSize, x, y, width, height, color, hover, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        # print(mouse)
        # hover highlight
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else: 
        pygame.draw.rect(gameDisplay, color, (x,y,width,height))
    TextSurf, TextRect = text_objects(msg, textSize)
    TextRect.center = ((x+(width/2)),(y+(height/2)))
    gameDisplay.blit(TextSurf, TextRect)

# Fade
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0 , 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
