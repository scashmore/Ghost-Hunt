import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)

# background music
pygame.mixer.init()
pygame.mixer.music.load('Game/Assets/Ghost-Hunt-OST-Tennenkyara-wa-go-Aikyou.ogg')
pygame.mixer.music.play(-1, fade_ms=2000)

def demo():
    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("image")
    displayImage = pygame.image.load("Game\Assets\demoPlaceHolder.webp")
    while True:
        surface.fill((255, 255, 255))
        surface.blit(displayImage, (0, 0))
        
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()