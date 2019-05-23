#_________________________________________________________________Libraries_________________________________________________________________#
import pygame,random,sys,time,os

#_____________________________________________________________Display Settings______________________________________________________________#
pygame.init()

display_width = 1400
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#_______________________________________________________________Image/Music_________________________________________________________________#
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chicken Slayer Z')
clock = pygame.time.Clock()

#**************************************************************Player Image*****************************************************************#
playerstand = pygame.image.load('Player\.tahastand.png')
playerright = pygame.image.load('Player\.taharight.png')
playerleft = pygame.image.load('Player\.tahaleft.png')
playerjump = pygame.image.load('Player\.tahajump.png')
playercrouch = pygame.image.load('Player\.tahacrouch.png')
playercharge = pygame.image.load('Player\.tahacharge.png')
playershoot = pygame.image.load('Player\.tahashoot.png')
energyblast = pygame.image.load('Player\energyblast.png')
stageimage = pygame.image.load('Backgrounds\stagethree.png')

#**************************************************************Enemy Image*******************************************************************#
chickenboss = pygame.image.load('Bosses\Ahmedboss.png')
bossshoot = pygame.image.load('Bosses\eggblast.png')

#**************************************************************Crash Music*******************************************************************#


#___________________________________________________________PreAssigned Variables____________________________________________________________#
x = 0
y = 0
graphics = 0
player_height = 260
player_width = 218

blastspeed = 80
blastx = 0
blasty = 0
blastwidth = 142
blastheight = 56

boss_height = 300
boss_width = 333
bossx = (display_width - boss_width)
bossy = 0
bossspeed = 15

eggwidth = 61
eggheight = 46
eggx = (display_width - boss_width - eggwidth)
eggy = 0
eggspeed = 30

plife = 10
blife = 11

#_________________________________________________________________Image Functions____________________________________________________________#
def player_stand(x,y):
    gameDisplay.blit(playerstand,(x,y))
    
def player_right(x,y):
    gameDisplay.blit(playerright,(x,y))

def player_left(x,y):
    gameDisplay.blit(playerleft,(x,y))

def player_jump(x,y):
    gameDisplay.blit(playerjump,(x,y))

def player_crouch(x,y):
    gameDisplay.blit(playercrouch,(x,y))

def player_charge(x,y):
    gameDisplay.blit(playercharge, (x,y))

def player_shoot(x,y):
    gameDisplay.blit(playershoot, (x,y))

def energy_blast(x,y):
    gameDisplay.blit(energyblast, (x,y))

def boss(x,y):
    gameDisplay.blit(chickenboss, (x,y))

def boss_shoot(x,y):
    gameDisplay.blit(bossshoot, (x,y))

def stage_background(x,y):
    gameDisplay.blit(stageimage, (x,y))

#_____________________________________________________________Interface Functions____________________________________________________________#
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def display_message(message,x,y):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def message(message):
    Largetext = pygame.font.SysFont("comicsansms", 30)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def lifepoints(life, width, height, colour):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('Health: '+str(life),True,colour)
    gameDisplay.blit(text,(width, height))

def win():
    gameDisplay.fill(white)
    display_message('Level Complete!',700,100)
    message('YOU WIN!!!')
    time.sleep(4)

def lose():
    gameDisplay.fill(white)
    display_message('Level Failed!',700,100)
    message('YOU LOSE!!!')
    time.sleep(4)

def hpbar(life, width, height, colour):
    bar = '█ '
    savehp = bar*life
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render(str(savehp),True,colour)
    gameDisplay.blit(text,(width, height))
    return
    
#_________________________________________________________________Game Function______________________________________________________________#
def game(display_width, graphics, plife, blife, player_width, blastx, blasty, blastspeed, boss_width, bossx, bossy, bossspeed, eggx, eggy, eggspeed):
    
#-------------------------------------------------------Preassigned Game Loop Variables------------------------------------------------------#
    x = (display_width * 0.10)
    y = (display_height * 0.30)

    x_change = 0
    y_change = 0

    exit_game = False

#-------------------------------------------------------------------Game Loop----------------------------------------------------------------#
    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||KeyBoard Controls||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    x_change = -20
                    graphics = 1
                elif event.key == ord('d'):
                    x_change = 20
                    graphics = 2
                elif event.key == ord('w'):
                    y_change = -20
                    graphics = 3
                elif event.key == ord('s'):
                    y_change = 20
                    graphics = 4
                elif event.key == ord(' '):
                    graphics = 5

            if event.type == pygame.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    x_change = 0
                    graphics = 0
                if event.key == ord('w') or event.key == ord('s'):
                    y_change = 0
                    graphics = 0
                if event.key == ord(' '):
                    graphics = 6

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Display Control|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
        x += x_change
        y += y_change

        if x < 0:
            x = 0
        elif x > (display_width*0.4) - player_width:
            x = (display_width*0.4) - player_width

        if y < 0:
            y = 0
        elif y > (display_height) - player_height:
            y = (display_height) - player_height

        stage_background(0,0)

        if graphics == 0:
            player_stand(x,y)
        elif graphics == 1:
            player_left(x,y)
        elif graphics == 2:
            player_right(x,y)
        elif graphics == 3:
            player_jump(x,y)
        elif graphics == 4:
            player_crouch(x,y)
        elif graphics == 5:
            player_charge(x,y)
        elif graphics == 6:
            blastx = (x+232)
            blasty = (y+63)
            player_shoot(x,y)
            graphics = 0
            
        energy_blast(blastx,blasty)
        blastx += blastspeed

        boss(bossx,bossy)
        bossy += bossspeed

        if bossy > 400:
            bossspeed = -30
        if bossy < 0:
            bossspeed = 30

        eggy = (bossy + 100)
        boss_shoot(eggx,eggy)
        eggx -= eggspeed

        if eggx < 0:
            eggx = (display_width - boss_width - eggwidth)

        if bossx < blastx + blastwidth:
            if bossy > blasty and bossy < blasty + blastheight or bossy + boss_height > blasty and bossy + boss_height < blasty + blastheight:
                blasty = 1450
                blife -= 1
                if blife <= 0:
                    win()
                    pygame.quit()
                    quit()
 
        if x + player_width > eggx:
            if y > eggy and y < eggy + eggheight or y + player_height > eggy and y + player_height < eggy + eggheight:
                eggx = (display_width - boss_width)
                plife -= 1
                if plife <= 0:
                    lose()
                    pygame.quit()
                    quit()
                    

        lifepoints(plife, 20, 10, green)
        hpbar(plife, 20, 50, green)
        lifepoints(blife, 1200, 610, red)
        hpbar(blife, 1200, 650, red)
        
        pygame.display.update()

        clock.tick(120)

#______________________________________________________________Program Output_____________________________________________________________#
while True:
    game(display_width, graphics, plife, blife, player_width, blastx, blasty, blastspeed, boss_width, bossx, bossy, bossspeed, eggx, eggy, eggspeed)
    pygame.quit()
    quit()
