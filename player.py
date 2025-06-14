import pygame
import settings
import projectile
from character import Character
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT



# Defining the Player class
class Player(Character): 

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nel.png").convert_alpha()
        self.initialize_rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        self.health = 10
        
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def shoot(self, dx=0, dy=-10):
        if dx == 0 and dy == 0:
            raise ValueError("Projectile must have a non-zero velocity in either x or y direction.")
        bullet = projectile.Projectile(self.rect.centerx, self.rect.centery, dx, dy)
        self.projectiles.append(bullet)

