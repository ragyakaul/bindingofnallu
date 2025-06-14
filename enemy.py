import pygame
import random
import enemyprojectile
import settings
from character import Character

class Enemy(Character):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy-honey.png").convert_alpha()
        self.initialize_rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        self.speed = 2
        self.health = 100

    def update(self, player):
        if self.rect.x < player.rect.x:  # Enemy to the left of player
            self.rect.x += self.speed  # Move right towards player
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        
        if self.rect.y < player.rect.y:  # Enemy to the bottom of player
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

        self.shoot()  # Randomly shoot projectiles
        for p in self.projectiles: # Update projectiles
            p.update()

        self.projectiles = [p for p in self.projectiles if p.rect.top <= settings.SCREEN_HEIGHT]   # Clean up off-screen projectiles

    
    def shoot(self):
        if random.randint(0, 100) < 2:
            projectile = enemyprojectile.EnemyProjectile(self.rect.centerx, self.rect.bottom)
            self.projectiles.append(projectile)



        