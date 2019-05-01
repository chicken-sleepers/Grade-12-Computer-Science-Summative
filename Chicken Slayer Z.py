import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((800,600))
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

x = (display_width * 0.40)
y = (display_height * 0.45)

x_change = 0
y_change = 0
graphics = 0

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                x_change = -5
                graphics = 1
            elif event.key == ord('d'):
                x_change = 5
                graphics = 2
            elif event.key == ord('w'):
                y_change = -5
                graphics = 3
            elif event.key == ord('s'):
                y_change = 5
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
