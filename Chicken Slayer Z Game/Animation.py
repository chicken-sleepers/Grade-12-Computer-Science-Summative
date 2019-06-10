'''
Taha Ali
ICS4UR
Ms. Pais
May 10, 2019

The following block of code runs the animation for the game, which is seen after
clicking the start button on the main menu.

'''
import pygame
from pygame.locals import *
import sys       
import os
from os import path
import pygame,random,sys,time,os

def main():
    """main() -> Image
    Plays a series of frames to create a short movie
    >>>main()
    video plays
    """
    pygame.init()                                                                   #Initializes python                                                                      
    pygame.display.init()                                                                               
    
    screensize = (1400, 700)

    screen = pygame.display.set_mode((screensize))                                                      

    clock = pygame.time.Clock()                                                     #function for speed of game defined as clock             
    
    pygame.display.set_caption("Chicken Escape")
    skip = pygame.image.load("Skipper.png")
    logo = pygame.image.load("icon.png")
    
    background = pygame.image.load("1.png")
    story = 100
    pygame.display.set_icon(logo)
    running = True
    while running:                                                          
        clock.tick(300)                                                              #Game refreshes at 64 frames per second
        for event in pygame.event.get():                                        
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    #if user hits esc or clicks the x on the top rightcorner program exits
                pygame.quit()
                sys.exit()
                running = False
            if event.type == KEYDOWN:                                               #Exit game
                if event.key == K_SPACE:
                    import Stage_3                                        #Skips animation and goes to game
                    
                                                                                    #Plays the animation                
        story += 1
        if story == 115:
            background = pygame.image.load("3.png")
        elif story == 120:
            background = pygame.image.load("3.png")
        elif story == 121:
            background = pygame.image.load("4.png")
        elif story == 122:
            background = pygame.image.load("5.png")
        elif story == 123:
            background = pygame.image.load("6.png")
        elif story == 124:
            background = pygame.image.load("7.png")
        elif story == 125:
            background = pygame.image.load("8.png")

        elif story == 145:
            background = pygame.image.load("9.png")
        elif story == 205:
            background = pygame.image.load("10.png")
        elif story == 255:
            background = pygame.image.load("11.png")
        elif story == 260:
            background = pygame.image.load("12.png")
        elif story == 265:
            background = pygame.image.load("13.png")
        elif story == 270:
            background = pygame.image.load("14.png")
        elif story == 275:
            import Stage_3
 
            
        
            
            
        screen.blit(background, (0, 0))                                             #background
        screen.blit(skip, (1100, 0))
        pygame.display.flip()                                                       #Updates game frames
        
    pygame.quit()                                                                       
    pygame.display.quit()
    
main()
            
