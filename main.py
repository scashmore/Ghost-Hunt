import pygame
from Components import components

pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.init()


black = (0,0,0)
white = (255,255,255)
dark_gray = (34, 34, 34)
light_gray = (105, 105, 105)

large_text = pygame.font.Font('freesansbold.ttf',115)
small_text = pygame.font.Font('freesansbold.ttf',20)

class GameState():
    def __init__(self):
        self.state = 'start_menu'
        self.song = 'Assets/ghost_hunt_opening_1_hd_-7802281804015965868.ogg'
        self.playing = False
    
    def exit_game(self):
        pygame.quit()
        quit()

    def state_manager(self): 
        if self.state == 'start_menu':
            self.song = 'Assets/ghost_hunt_opening_1_hd_-7802281804015965868.ogg'
            self.start_menu()
        if self.state == 'trivia':
            self.song = 'Assets/Ghost-Hunt-OST-Tennenkyara-wa-go-Aikyou.ogg'
            self.trivia()

    def fade(self): 
        components.fade(600, 800)
        pygame.mixer.music.fadeout(2000)
        self.playing = False
        
    def update(self, state):
        self.fade()
        self.state = state

    def start_menu(self):
        # background imgae
        display_image = pygame.image.load("Assets/anime_ghosthunt.jpg")

        # background music
        if not self.playing:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(-1)
            self.playing = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
        components.game_display.fill(black)
        components.game_display.blit(pygame.transform.scale(display_image, (960, 375)), ((components.display_width/2 - 960/2), (components.display_height/2 - 375/2)))
        
        # interactive buttons
        # Start
        components.button("Start", small_text, 150, 500, 100, 50, dark_gray, light_gray, self.update, 'trivia')
        # Quit
        components.button("Exit", small_text, 550, 500, 100, 50, dark_gray, light_gray, self.exit_game, None)
        
    def trivia(self):
        pygame.mouse.set_visible(False)

        # background imgae
        display_image = pygame.image.load("Assets/Maps/Map002.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
                
        components.game_display.fill(black)
        components.game_display.blit(display_image, (0,0))
        
        if not self.playing:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(-1)
            self.playing = True


pygame.display.set_caption('Ghost Hunt Demo')

game_display = pygame.display.set_mode((960, 600))

clock = pygame.time.Clock()

game_state = GameState()


while True:
    game_state.state_manager()

    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)
