import pygame
from ..Text import text
from ..Buttons import buttons

black = (0,0,0)
darkGray = (34, 34, 34)
white = (255,255,255)
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

wrong = 0

Monk = "Game\Assets\placeholder.png"

NaruNormal = "Game/Assets/NaruImages/NaruPortraitNormal.png"
NaruOpen = "Game/Assets/NaruImages/NaruPortraitNormalOpenMouth.png"
NaruSmile = "Game/Assets/NaruImages/NaruPortraitSmile.png"
NaruSurprised = "Game/Assets/NaruImages/NaruPortraitSurprised.png"
NaruAngry = "Game/Assets/NaruImages/NaruPortraitAngryEyesClosed.png"

MaiNormal = "Game\Assets\MaiImages\MaiPortraitNormal.png"
MaiOpen = "Game\Assets\MaiImages\MaiPortraitNormalOpenMouth.png"
MaiSmile = "Game\Assets\MaiImages\MaiPortraitSmile.png"
MaiSurprised = "Game\Assets\MaiImages\MaiPortraitSurprised.png"
MaiAngry = "Game\Assets\MaiImages\MaiPortraitAngryEyesClosed.png"

questions = [
    ["Currently, what month is it?", ["November...", "May!","...I think it's November"]],
    ["Where is the location of our next investigation?", ["Rokuryou High School.","Yuuei High School.", "Yuasa High School."]],
    ["Monk specifically talked about this cursed item in a classroom. So far, all students that have used it got dragged by a train.", ["A desk.","A sharpener.", "A book."]],
    ["Which spirit was called upon and is now suspected to be the one responsible for possessing the students?", ["Kokkuri-san.","Orikiri-sama.", "Inari-sama."]],
    ["I mentioned this during Minnie's excorcism--in which direction does the demon gate lie?", ["East.","Southeast.", "NorthEast."]],
    ["What type of camera do we use to pick up temerature fluctuations?", ["Infrared camera.","Thermography camera.", "Ultra-high sensitivity camera."]]
]

# opening dialouge
oD = [
    ["Then it's a plan! Thanks for looking into this, Naru. I'll meet you guys there tomorrow.", "Monk"],
    ["See ya!", "Monk"],
    ["Where you paying attention properly this time?", "Naru"],
    ["This time?!", "Mai"],
    ["What does that mean? Of course I was!", "Mai"],
    ["Is that so?", "Naru"],
    ["Yes! I'll prove it to you!", "Mai"],
    ["~", "Naru"],
    ["Then let's start off easy.", "Naru"],
    # question 1
    ["Currently, what month is it?", "Naru", ["November...", "Is this a joke...? If so... May!","...I think it's November"]],
]

Q1op1 = [
    ["Good. It would have been rediculous for you to get that wrong.", "Naru"],
    # itlics
    ["This guy really grates my nerves...", "Mai"],
    ["Where is the location of our next investigation?", "Naru", ["Rokuryou High School.","Yuuei High School.", "Yuasa High School."]],
]

Q1op2 = [
    ["You don't have to go to such lenghts to prove your idiocy.", "Naru"],
    # itlics
    ["It was a joke!", "Mai"],
    # larger font
    ["A joke!", "Mai"],
    # itlaics
    ["Oh, who am I kidding? He doesn't understand those things...", "Mai"],
    ["Where is the location of our next investigation?", "Naru", ["Rokuryou High School.","Yuuei High School.", "Yuasa High School."]],
]

Q1op3 = [
    ["That's right. I'll ignore the fact you soundned unsure", "Naru"],
    # ittlicts
    ["This guy...", "Mai"],
    ["Where is the location of our next investigation?", "Naru", ["Rokuryou High School.","Yuuei High School.", "Yuasa High School."]],
]

Q2op1 = []

Q2op2 = []

Q3op1 = []

Q3op2 = []

Q4op1 = []

Q4op2 = []

background = pygame.image.load("Game\Assets\Maps\Map002.png")

def triviaGame():

    run = True
    textboxes = [
        [Monk, oD[0][0]],
        [Monk, oD[1][0]],
        [NaruNormal, oD[2][0]],
        [MaiAngry, oD[3][0]],
        [MaiOpen, oD[4][0]],
        [NaruOpen, oD[5][0]],
        [MaiSmile, oD[6][0]],
        [NaruSmile, oD[7][0]],
        [NaruOpen, oD[8][0]],
        [NaruOpen, oD[9][0]]
    ]

    i = 0
    dialogue = text.Dialogue(surface, textboxes[i][0], textboxes[i][1], white)
    textGroup = pygame.sprite.Group()
    textGroup.add(dialogue)

    while run:
        surface.fill((255, 255, 255))
        pygame.mouse.set_visible(False)
        keys = pygame.key.get_pressed()
        surface.blit(background, (0,0))
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYUP) and (keys[pygame.K_SPACE]):
                i+=1
                if i == 3:
                    dialogue.update(textboxes[i][1], textboxes[i][0], False, False, 40)
                elif i < len(textboxes):
                    dialogue.update(textboxes[i][1], textboxes[i][0], False, False, 20) 
                else:
                    pass
                    # dialogue.kill() 
            pygame.display.update() 
        if i >= 9:
            pygame.mouse.set_visible(True)
            font = pygame.font.SysFont("Arial", 20)
            buttons.button(oD[9][2][0], font, 250, 150, 300, 50, black, darkGray, correct1)
            buttons.button(oD[9][2][1], font, 250, 210, 300, 50, black, darkGray, wrong1)
            buttons.button(oD[9][2][2], font, 250, 270, 300, 50, black, darkGray, hesitantCorrect1)
        if i < len(textboxes):
            textGroup.update(textboxes[i][1], textboxes[i][0], False, False, 20)
            dialogue.textBox()
        elif i >= len(textboxes):
            i = len(textboxes) - 1
        
        
        clock.tick(30)
        pygame.display.flip()

def correct1():
    
    textboxes = [
        [NaruSmile, Q1op1[0][0]],
        [MaiAngry, Q1op1[1][0]],
        [NaruOpen, Q1op1[2][0]],
    ]

    i = 0
    dialogue = text.Dialogue(surface, textboxes[i][0], textboxes[i][1], white)
    textGroup = pygame.sprite.Group()
    textGroup.add(dialogue)

    while True:
        surface.fill((255, 255, 255))
        pygame.mouse.set_visible(False)
        keys = pygame.key.get_pressed()
        surface.blit(background, (0,0))
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYUP) and (keys[pygame.K_SPACE]):
                i+=1
                if i == 1:
                    dialogue.update(textboxes[i][1], textboxes[i][0], False, True, 20) 
                elif i < len(textboxes):
                    dialogue.update(textboxes[i][1], textboxes[i][0], False, False, 20) 
                else:
                    pass
                    # dialogue.kill() 
            pygame.display.update() 
        if i >= 2:
            pygame.mouse.set_visible(True)
            font = pygame.font.SysFont("Arial", 20)
            buttons.button(Q1op1[2][2][0], font, 250, 150, 300, 50, black, darkGray, wrong2)
            buttons.button(Q1op1[2][2][1], font, 250, 210, 300, 50, black, darkGray, wrong2)
            buttons.button(Q1op1[2][2][2], font, 250, 270, 300, 50, black, darkGray, correct2)
        if i < len(textboxes):
            textGroup.update(textboxes[i][1], textboxes[i][0], False, False, 20)
            dialogue.textBox()
        elif i >= len(textboxes):
            i = len(textboxes) - 1
        
        clock.tick(30)
        pygame.display.flip()

def hesitantCorrect1():
    while True:
        surface.blit(background, (0,0))

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
        
        clock.tick(30)
        pygame.display.flip()

def wrong1():
    while True:
        surface.blit(background, (0,0))

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
        
        clock.tick(30)
        pygame.display.flip()

def correct2():
    while True:
        surface.blit(background, (0,0))

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
        
        clock.tick(30)
        pygame.display.flip()

def wrong2():
    while True:
        surface.blit(background, (0,0))

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
        
        clock.tick(30)
        pygame.display.flip()

