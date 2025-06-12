import pygame
import sys

import pygame.locals

pygame.init()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)


# Creating a display screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
displaySurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("BindingOfNalluBackground.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


# Defining the Player class
class Player(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    image: pygame.Surface = None

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nel.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.locals.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.locals.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.locals.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.locals.K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface : pygame.Surface):
        surface.blit(self.image, self.rect)



class Projectile:
    rectHeight = 10
    rectWidth = 20
    def __init__(self, x, y, speed=-7):
        self.rect = pygame.Rect(x, y, self.rectHeight, self.rectWidth)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, (196, 164, 132), self.rect)

player = Player()
projectiles = []

while True:

    for event in pygame.event.get():
        # Quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Shooting Projectiles
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            projectiles.append(Projectile(player.rect.centerx - 5, player.rect.top))
    
   
    player.update()
   

    # Draw the background
    displaySurface.blit(background, (0, 0))

    # Draw the player
    player.draw(displaySurface)

    
    # Draw bullets on top
    for bullet in projectiles:
        bullet.update()
        bullet.draw(displaySurface)
    
    pygame.display.update()
    clock.tick(60)
    