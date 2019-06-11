import pygame, time, math
pygame.init()

#-----Display-----#
win = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("Stage 3")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#-----Images-----#
stageimage = pygame.image.load("Backgrounds/stagethree.png")
moveRight = pygame.image.load("Player/taharights3.png")
moveLeft = pygame.image.load("Player/tahalefts3.png")
moveUp = pygame.image.load("Player/tahajumps3.png")
moveDown = pygame.image.load("Player/tahacrouchs3.png")
standing = pygame.image.load("Player/tahastands3.png")
blast = pygame.image.load("Player/energyblasts3.png")
ahmedboss = pygame.image.load("Bosses/Ahmedboss.png")
eggblast = pygame.image.load("Bosses/eggblasts3.png")

clock = pygame.time.Clock()

#-----Player-----#
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.vel = 20
        self.left = False
        self.right = False
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.life = 10

    def draw(self, win):
        if self.left:
            win.blit(moveLeft, (self.x, self.y))
        elif self.right:
            win.blit(moveRight, (self.x, self.y))
        else:
            win.blit(standing, (self.x, self.y))

        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.life -= 1

class player_projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 50

    def draw(self, win):
        win.blit(blast, (self.x, self.y))

#-----Boss-----#
class boss:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.life = 50

    def move(self):
        self.y += self.vel

    def draw(self, win):
        self.move()
        win.blit(ahmedboss, (self.x, self.y))

        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.life -= 1

class boss_projectile(object):
    def __init__(self, x, y, angle):
        self.angle = angle
        self.x = x
        self.y = y
        self.vel = 25

    def draw(self, win):
        win.blit(eggblast, (self.x, self.y))

#-----Window Update-----#
def redraw_window():
    win.blit(stageimage, (0,0))
    taha.draw(win)
    ahmed.draw(win)

    for energyblast in blast_list:
        energyblast.draw(win)

    for eggenergyblast in eggblast_list:
        eggenergyblast.draw(win)

    lifepoints(taha.life, 20, 10, green)
    hpbar(taha.life, 20, 50, green)
    lifepoints(ahmed.life, 1200, 610, red)
    hpbar(ahmed.life, 1200, 650, red)
    
    pygame.display.update()

#-----User Interface-----#
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def display_message(message,x,y):
    Largetext = pygame.font.SysFont("comicsansbold", 60)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = (x, y)
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def message(message):
    Largetext = pygame.font.SysFont("comicsansms", 30)
    TextSurf, TextRect = text_objects(message, Largetext)
    TextRect.center = ((1400/2), (700/2))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)

def lifepoints(life, width, height, colour):
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render('Health: '+str(life),True,colour)
    win.blit(text,(width, height))

def gamewin():
    win.fill(white)
    display_message('Level Complete!',700,100)
    message('YOU WIN!!!')
    import Main_Menu
    time.sleep(4)

def gamelose():
    win.fill(white)
    display_message('Level Failed!',700,100)
    message('YOU LOSE!!!')
    import Main_Menu
    time.sleep(4)

def hpbar(life, width, height, colour):
    bar = '█ '
    savehp = bar*life
    font = pygame.font.SysFont("comicsansms", 25)
    text=font.render(str(savehp),True,colour)
    win.blit(text,(width, height))
    return

#-----mainloop-----#
taha = player(50, 350, 60, 125)
ahmed = boss (1000, 350, 260, 240)
blast_list = []
eggblast_list = []
blast_reload = 0
                 
run = True
while run:
    clock.tick(120)

    if blast_reload > 0:
        blast_reload += 1
    if blast_reload > 4:
        blast_reload = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for energyblast in blast_list:
        if energyblast.y - 12 < ahmed.hitbox[1] + ahmed.hitbox[3] and energyblast.y + 12 > ahmed.hitbox[1]:
            if energyblast.x + 35 > ahmed.hitbox[0] and energyblast.x - 35 < ahmed.hitbox[0] + ahmed.hitbox[2]:
                ahmed.hit()
                blast_list.pop(blast_list.index(energyblast))
                
        if energyblast.x < 1400:
            energyblast.x += energyblast.vel
        else:
            blast_list.pop(blast_list.index(energyblast))

    for eggenergyblast in eggblast_list:
        if eggenergyblast.y - 10 < taha.hitbox[1] + taha.hitbox[3] and eggenergyblast.y + 10 > taha.hitbox[1]:
            if eggenergyblast.x + 10 > taha.hitbox[0] and eggenergyblast.x - 10 < taha.hitbox[0] + taha.hitbox[2]:
                taha.hit()
                eggblast_list.pop(eggblast_list.index(eggenergyblast))
                
        if eggenergyblast.x > 0 and eggenergyblast.x < 1400 and eggenergyblast.y > 0 and eggenergyblast.y < 700:
            eggenergyblast.y -= eggenergyblast.vel * math.sin(eggenergyblast.angle)
            eggenergyblast.x -= eggenergyblast.vel * math.cos(eggenergyblast.angle)
        else:
            eggblast_list.pop(eggblast_list.index(eggenergyblast))
                 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and blast_reload == 0:
        if len(blast_list) < 3:
            blast_list.append(player_projectile(round(taha.x + taha.width // 2), round(taha.y + taha.width // 2)))

        blast_reload = 1
    
    if taha.right == True or taha.left == True:
        taha.width = 105
        taha.height = 80
    else:
        taha.width = 60
        taha.height = 125

    if keys[pygame.K_d] and taha.x < 700:
        taha.x += taha.vel
        taha.right = True
        taha.left = False
    elif keys[pygame.K_a] and taha.x > taha.vel:
        taha.x -= taha.vel
        taha.left = True
        taha.right = False
    else:
        taha.right = False
        taha.left = False
    if keys[pygame.K_w] and taha.y > taha.vel:
        taha.y -= taha.vel
    if keys[pygame.K_s] and taha.y < 550:
        taha.y += taha.vel

    if ahmed.y > 700 - ahmed.height:
        ahmed.vel = -10

    if ahmed.y < 0:
        ahmed.vel = 10

    if len(eggblast_list) < 1:
        eggblast_list.append(boss_projectile(round(ahmed.x), round(ahmed.y + ahmed.width // 2), 0.261799))
        eggblast_list.append(boss_projectile(round(ahmed.x), round(ahmed.y + ahmed.width // 2), -0.261799))
        eggblast_list.append(boss_projectile(round(ahmed.x), round(ahmed.y + ahmed.width // 2), 0))

    if ahmed.life <= 0:
        gamewin()
        pygame.quit()
        quit()
    if taha.life <= 0:
        gamelose()
        pygame.quit()
        quit()

    redraw_window()
    
pygame.quit()

