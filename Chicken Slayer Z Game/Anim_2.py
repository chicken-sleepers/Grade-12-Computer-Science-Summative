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

def main():
    """main() -> Image
    Plays a series of Pics to create a short movie
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
    
    background = pygame.image.load("Pic_1.png")
    story = 100
    pygame.display.set_icon(logo)
    running = True
    while running:                                                          
        clock.tick(300)                                                              #Game refreshes at 64 Pics per second
        for event in pygame.event.get():                                        
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    #if user hits esc or clicks the x on the top rightcorner program exits
                pygame.quit()
                sys.exit()
                running = False
            if event.type == KEYDOWN:                                               #Exit game
                if event.key == K_SPACE:
                    os.startfile('Stage 2.py')                                        #Skips animation and goes to game
                    

                                                                                    #Plays the animation                
        story += 1
        if story == 155:
            background = pygame.image.load("Pic_2.png")
        elif story == 160:
            background = pygame.image.load("Pic_3.png")
        elif story == 162:
            background = pygame.image.load("Pic_4.png")
        elif story == 163:
            background = pygame.image.load("Pic_5.png")
        elif story == 164:
            background = pygame.image.load("Pic_6.png")
        elif story == 200:
            background = pygame.image.load("Pic_7.png")
        elif story == 235:
            background = pygame.image.load("Pic_8.png")
        elif story == 295:
            background = pygame.image.load("Pic_9.png")
        elif story == 300:
            background = pygame.image.load("Pic_10.png")
        elif story == 305:
            background = pygame.image.load("Pic_11.png")
        elif story == 310:
            background = pygame.image.load("Pic_12.png")
        elif story == 315:
             os.startfile('Stage 2.py')

            
        
            
            
        screen.blit(background, (0, 0))                                             #background
        screen.blit(skip, (1100, 600))
        pygame.display.flip()                                                       #Updates game frames
        
    pygame.quit()                                                                       
    pygame.display.quit()
    
main()
            
