import pygame
from ..Text import text

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

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
    ["Then it's a plan! Thanks for looking into this, Naru. I'll meet you guys there tomorrow.", ["Monk"]],
    ["See ya!", ["Monk"]],
    ["Where you paying attention properly this time?", ["Naru"]],
    ["This time?!", ["Mai"]],
    ["What does that mean? Of course I was!", ["Mai"]],
    ["Is that so?", ["Naru"]],
    ["Yes! I'll prove it to you!", ["Mai"]],
    ["~", ["Naru"]],
    ["Then let's start off easy.", ["Naru"]],
]

def triviaGame(surface, map):
    run = True
    background = pygame.image.load(map)
    textboxes = [
        [Monk, oD[0][0]],
        [Monk, oD[1][0]],
        [NaruNormal, oD[2][0]],
        [MaiAngry, oD[3][0]],
        [MaiOpen, oD[4][0]],
        [NaruOpen, oD[5][0]],
        [MaiSmile, oD[6][0]],
        [NaruSmile, oD[7][0]],
        [NaruOpen, oD[8][0]]
    ]

    i = 0
    dialogue = text.Dialogue(surface, textboxes[i][0], textboxes[i][1], white)
    textGroup = pygame.sprite.Group()
    textGroup.add(dialogue)

    while run:
        keys = pygame.key.get_pressed()
        surface.blit(background, (0,0))
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYUP) and (keys[pygame.K_SPACE]):
                i+=1
                if i < len(textboxes):
                    dialogue.update(textboxes[i][1], textboxes[i][0]) 
                else:
                    dialogue.kill() 
            pygame.display.update() 
        if i < len(textboxes):
            textGroup.update(textboxes[i][1], textboxes[i][0])
            dialogue.textBox()   
        else:
            run == False
        
        
        clock.tick(30)
        pygame.display.flip()