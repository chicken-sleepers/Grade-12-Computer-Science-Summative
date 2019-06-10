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
                quit()
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
        display_message('SAVE THE WORLD FOR REAL!!!')
        text_display("The Problem:",690,130,30)
        text_display("No human technology can fully replace “nature’s technology”, perfected over hundreds of millions of years ",690,175,25)
        text_display("in delivering key services to sustain life on Earth. A productive, diverse natural world and a stable climate",690,215,25)
        text_display(" have been the basic assets at the foundation of the success of our civilisation, and will continue to be so ",690,255,25)
        text_display("in future. A fundamental issue in the previous technological revolutions has been the lightness with which we ",690,295,25)
        text_display("have taken for granted the natural environment rather than valuing it as a condition necessary to development.",690,335,25)
        #https://www.weforum.org/agenda/2018/01/it-s-time-to-bring-our-planet-back-from-the-brink-together-now/
        text_display("How You Can Help!!!",690,375,30)
        text_display('Reuse, Reduce, Recycle --> Cut down on what you throw away. This conserves natural resources and landfill space.',690,415,25)
        text_display('Conserve Water --> The less water you use, the less runoff and wastewater that eventually end up in the ocean.',690,455,25)
        text_display('Shop wisely --> Buy less plastic and bring a reusable shopping bag.',690,495,25)
        text_display('Plant a tree --> Trees provide food and oxygen. They help save energy, clean the air, and help combat climate change.',690,535,25)
        text_display('Volunteer --> Volunteer for cleanups in your community. You can get involved in protecting your watershed, too.',690,575,25)
        #https://oceanservice.noaa.gov/ocean/earthday.html
        button("Main Menu",110, 625, 125, 30, deep_red, bright_red,"back")
        button("Quit",1150, 625, 125, 30, deep_red, bright_red,"quit")
        
        pygame.display.update()
        clock.tick(60)

#______________________________________________________________Program Output_____________________________________________________________#
while True:
    instructions()
    pygame.quit()
    quit()
