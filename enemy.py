import pygame
import settings

class Enemy(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    image: pygame.Surface = None

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy-robot-cleaner.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (settings.SCREEN_WIDTH/3, settings.SCREEN_HEIGHT/2)
        self.speed = 2

    def update(self, player):
        # Enemy to the left of player
        if self.rect.x < player.rect.x:
            # Move right towards player
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        
        # Enemy to the bottom of player
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


        