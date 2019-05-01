import pygame

pygame.init()

display_width = 1200
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

graphics = 0
player_height = 260
player_width = 218

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chicken Slayer Z')
clock = pygame.time.Clock()

playerstand = pygame.image.load('tahastand.png')
playerright = pygame.image.load('taharight.png')
playerleft = pygame.image.load('tahaleft.png')
playerjump = pygame.image.load('tahajump.png')
playercrouch = pygame.image.load('tahacrouch.png')

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

def game(graphics):
    x = (display_width * 0.10)
    y = (display_height * 0.30)

    x_change = 0
    y_change = 0

    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    x_change = -10
                    graphics = 1
                elif event.key == ord('d'):
                    x_change = 10
                    graphics = 2
                elif event.key == ord('w'):
                    y_change = -10
                    graphics = 3
                elif event.key == ord('s'):
                    y_change = 10
                    graphics = 4

            if event.type == pygame.KEYUP:
                if event.key == ord('a') or event.key == ord('d'):
                    x_change = 0
                    graphics = 0
                if event.key == ord('w') or event.key == ord('s'):
                    y_change = 0
                    graphics = 0

        x += x_change
        y += y_change

        if x < 0:
            x = 0
        elif x > (display_width*0.5) - player_width:
            x = (display_width*0.5) - player_width

        if y < 0:
            y = 0
        elif y > (display_height) - player_height:
            y = (display_height) - player_height

        gameDisplay.fill(white)

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
            
        pygame.display.update()

        clock.tick(60)
while True:
    game(graphics)
    pygame.quit()
    quit()
