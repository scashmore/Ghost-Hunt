import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)

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