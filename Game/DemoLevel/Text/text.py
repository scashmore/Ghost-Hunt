import pygame

# Dialogue Box
class Dialogue(pygame.sprite.DirtySprite):
    def __init__(self, screen, portrait, text, textColor):
        super().__init__()
        self.screen = screen
        self.text = text
        self.textColor = textColor
        self.portrait = portrait
        self.font = pygame.font.SysFont("Arial", 20)
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.maxWidth, self.maxHeight = [self.width - 20, (self.height // 4) - 15 ]
        self.count = 0
        return

    def textBox(self):
        font = self.font
        words = [word.split(' ') for word in self.text.splitlines()]
        space = font.size(' ')[0]
        # Come back for typewriter effect
        # counter = 0
        # speed = 3
        # snip = font.render(text, True, (225,225,225))
        # done = False
        portrait = pygame.image.load(self.portrait)
        self.screen.blit(portrait, (480, 35))
        pygame.draw.rect(self.screen, (0,0,0), (5, self.height - (self.height // 4) - 5, self.width - 10, self.height // 4), border_radius=20)
        pos = [30, self.height + 25 - self.height // 4]
        x, y = pos
        for line in words:
            for word in line:
                wordSurface = font.render(word, True, self.textColor)
                wordWidth, wordHeight = wordSurface.get_size()
                if x + wordWidth >= self.maxWidth:
                    x = pos[0]
                    y += wordHeight
                self.screen.blit(wordSurface, (x, y))
                x += wordWidth + space
            x = pos[0]
            y += wordHeight

    def update(self, text, portrait):
        print(text)
        self.text = text
        self.portrait = portrait