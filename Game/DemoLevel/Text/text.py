import pygame
# Dialogue Box
def textBox(screen, color, text, textColor):
    font = pygame.font.SysFont("Arial", 20)
    # font = textFont.render(text, True, textColor)
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    maxWidth, maxHeight = [screen.get_width() - 20, (screen.get_height() // 4) - 15 ]
    # Come back for typewriter effect
    # counter = 0
    # speed = 3
    # snip = font.render(text, True, (225,225,225))
    # done = False
    pygame.draw.rect(screen, color, (5, screen.get_height() - (screen.get_height() // 4) - 5, screen.get_width() - 10, screen.get_height() // 4), border_radius=20)
    pos = [30, screen.get_height() + 25 - screen.get_height() // 4]
    x, y = pos
    for line in words:
        for word in line:
            wordSurface = font.render(word, True, textColor)
            wordWidth, wordHeight = wordSurface.get_size()
            if x + wordWidth >= maxWidth:
                x = pos[0]
                y += wordHeight
            screen.blit(wordSurface, (x, y))
            x += wordWidth + space
        x = pos[0]
        y += wordHeight

def drawText(text, font, textColor, x, y, screen):
    font = font.render(text, True, textColor)
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))