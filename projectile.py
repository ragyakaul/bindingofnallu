
import pygame


class Projectile:
    rectHeight = 10
    rectWidth = 20
    def __init__(self, x, y, dx=0, dy=-10):
        self.image = pygame.image.load("eye-gook.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = dx
        self.dy = dy
        if dx == 0 and dy == 0:
            raise ValueError("Projectile must have a non-zero velocity in either x or y direction.")
    def update(self):
        self.rect.y += self.dy
        self.rect.x += self.dx
    
    def draw(self, surface):
       surface.blit(self.image, self.rect)