import pygame
import projectile

class EnemyProjectile(projectile.Projectile):
    def __init__(self, x, y):
        super().__init__(x, y, dx = 0, dy = -10)
        self.image = pygame.image.load("enemy-gook.png")
        