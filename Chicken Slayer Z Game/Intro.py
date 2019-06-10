'''
Taha Ali
ICS4UR
Ms. Pais
March 29, 2019

The following block of code runs the animation for the game, which is seen after
clicking the start button on the main menu.

'''
import pygame
from pygame.locals import *
import sys       
import os
from os import path
import pygame,random,sys,time,os, webbrowser
from os import path

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
    
    pygame.display.set_caption("Chicken Slayerz")
    skip = pygame.image.load("Skipper.png")
    logo = pygame.image.load("icon.png")
    
    background = pygame.image.load("Frame_1.png")
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
                    import Stage_1                                       #Skips animation and goes to game
                    

                                                                                    #Plays the animation                
        story += 1
        if story == 110:
            background = pygame.image.load("Frame_2.png")
        elif story == 120:
            background = pygame.image.load("Frame_3.png")
        elif story == 130:
            background = pygame.image.load("Frame_4.png")
        elif story == 140:
            background = pygame.image.load("Frame_5.png")
        elif story == 145:
            background = pygame.image.load("Frame_6.png")
        elif story == 245:
            background = pygame.image.load("Frame_7.png")
        elif story == 285:
            background = pygame.image.load("Frame_8.png")
        elif story == 345:
            background = pygame.image.load("Frame_9.png")
        elif story == 385:
            background = pygame.image.load("Frame_10.png")
        elif story == 455:
            background = pygame.image.load("Frame_11.png")
        elif story == 495:
            background = pygame.image.load("Frame_12.png")
        elif story == 555:
            background = pygame.image.load("Frame_13.png")
        elif story == 565:
            background = pygame.image.load("Frame_14.png")
        elif story == 575:
            background = pygame.image.load("Frame_15.png")
        elif story == 580:
            background = pygame.image.load("Frame_16.png")
        elif story == 585:
             import Stage_1

            
        
            
            
        screen.blit(background, (0, 0))                                             #background
        screen.blit(skip, (1100, 600))
        pygame.display.flip()                                                       #Updates game frames
        
    pygame.quit()                                                                       
    pygame.display.quit()
    
main()
            
