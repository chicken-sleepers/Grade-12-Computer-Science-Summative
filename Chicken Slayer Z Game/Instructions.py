#_________________________________________________________________Libraries_________________________________________________________________#
import pygame,random,sys,time,os
from os import path

#_____________________________________________________________Display Settings______________________________________________________________#
pygame.init()

display_width = 1400
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (196,43,43)
deep_red = (69,7,31)
purple_red = (86,16,67)

#_______________________________________________________________Image/Music_________________________________________________________________#
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chicken Slayer Z')
clock = pygame.time.Clock()

backgroundimg = pygame.image.load('Backgrounds\instruc.png')
controlimg = pygame.image.load('Backgrounds\playercontrols.png')

#_________________________________________________________________Image Functions____________________________________________________________#
def background_display(x,y):
    gameDisplay.blit(backgroundimg, (x,y))

def control(x,y):
    gameDisplay.blit(controlimg, (x,y))

#_________________________________________________________________File Functions_____________________________________________________________#
def mainmenu_file():
    import Main_Menu
#_____________________________________________________________Interface Functions____________________________________________________________#
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
    
def display_message(message):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/12))
    gameDisplay.blit(TextSurf, TextRect)

    
def instruction_background_display(x,y):
    gameDisplay.blit(instructionimg, (x,y))

def text_display(msg, x, y, size):
    medium_text = pygame.font.SysFont("comicsansms", size)
    textSurf, textRect = text_objects(msg, medium_text)
    textRect.center = ((x), (y))
    gameDisplay.blit(textSurf, textRect)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "back":
                mainmenu_file()
                
            if action == "quit":
                pygame.quit()
                quit()
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    Smalltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, Smalltext)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)
    
#_________________________________________________________________Game Function______________________________________________________________#
def instructions():

    start = True
    while start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background_display(0,0)
        text_display("This game is not affiliated with Nintendo", 690, 625,10)
        text_display("Copyright © ATV.Inc 2018", 690, 640,10)
        display_message('How to Play')
        text_display("Movement:",690,130,30)
        text_display("Use W (Up), A (Left), S(Down), D (Right) for movement and space to fire energy blasts",690,175,25)
        control(600,200)
        text_display("Objective:",690,375,30)
        text_display('Your goal is to save the world from the evil Chicken Invaders',690,415,25)
        text_display('Defeat each Invader to progress further towards the King Invader',690,455,25)
        text_display('Defeat the King Invader to save the chickens!!!',690,495,25)
        text_display('You and the Enemy start with 10 Health Points and each energy blast/egg deals 1 Damage',690,535,25)
        text_display('So avoid the eggs and defeat the boss to win!!!',690,575,25)
        button("Main Menu",110, 625, 125, 30, deep_red, bright_red,"back")
        button("Quit",1150, 625, 125, 30, deep_red, bright_red,"quit")
        
        pygame.display.update()
        clock.tick(60)

#______________________________________________________________Program Output_____________________________________________________________#
while True:
    instructions()
    pygame.quit()
    quit()
