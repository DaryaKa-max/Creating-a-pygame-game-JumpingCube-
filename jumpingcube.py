# Importing libraries
import pygame
import random
import sys
#Set variables for our field
WIDTH = 1000
HEIGHT = 800
FPS = 25
xCord = 280
yCord = 402
radius = 50
DRxCord = 1
DRyCord = 1
direct = DRxCord 
cours = DRyCord 
jumpCount = 12
isJump = False
size = (WIDTH, HEIGHT)

#Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
####################################################################################################
#Set the classes for the movement of our squares
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 425)

    def update(self):
        self.rect.x -= 11
        if self.rect.right < 0:
                self.rect.left = 1000

class Rect2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 95))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 402)
        
    def update(self):
        self.rect.x -= 11
        if self.rect.right < 0:
                self.rect.left = 1000

class Rect3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 200))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (650, 350)
        
    def update(self):
        self.rect.x -= 11
        if self.rect.right < 0:
                self.rect.left = 1000
#################################################################################################################
#Create a main window with dimensions and title 
pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode(size)
pygame.display.set_caption("JumpingCube")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
#Setting values for our classes
player = Player()
all_sprites.add(player)

player_s = Rect2()
all_sprites.add(player_s)

player_e = Rect3()
all_sprites.add(player_e)
#Setting the game loop 
running = True
while running:
    #Keeping the cycle at the correct speed 
    clock.tick(FPS)
    #Process (event) input 
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()
    
################################################################
#We set the condition for the movement of our ball
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        xCord -= 3
    if keys[pygame.K_d]:
        xCord += 3
    if not(isJump): 
        if keys[pygame.K_UP]:
            y -= 3
        if keys[pygame.K_DOWN]:
            yCord += 3
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -12:
            yCord -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 12
            isJump = False
##############################################################
    #Рендеринг 
    surface.fill(BLACK)
    all_sprites.draw(surface)
    #How to create the ball and line in the window
    pygame.draw.line(surface, WHITE, [0, 450], [1000, 450], 4)
    pygame.draw.circle(surface, (255, 255, 255), (xCord, yCord), radius)
    #After drawing everything, flip the screen 
    pygame.display.flip()
#Exit
pygame.quit()

#P.S This game is simple :) There is no scoring for players here yet. This is for training!