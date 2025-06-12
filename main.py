import pygame
import sys
import player
import projectile
import settings
import enemy
import pygame.locals

pygame.init()

# Creating a display screen
displaySurface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

background = pygame.image.load("background.jpg").convert_alpha()
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

clock = pygame.time.Clock()


player = player.Player()
enemy = enemy.Enemy()
projectiles = []

while True:

    for event in pygame.event.get():
        # Quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Shooting Projectiles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                projectiles.append(projectile.Projectile(player.rect.centerx - 5, player.rect.top, dy =-10))
            elif event.key == pygame.K_s:
                projectiles.append(projectile.Projectile(player.rect.centerx - 5, player.rect.bottom, dy=10))
            elif event.key == pygame.K_a:
                projectiles.append(projectile.Projectile(player.rect.left, player.rect.centery, dx=-10, dy=0))
            elif event.key == pygame.K_d:
                projectiles.append(projectile.Projectile(player.rect.right, player.rect.centery, dx=10, dy=0))
   
    player.update()
   

    # Draw the background
    displaySurface.blit(background, (0, 0))

    # Draw the player
    player.draw(displaySurface)

    # Draw the enemy
    enemy.update(player)
    enemy.draw(displaySurface)

    # Draw bullets on top
    for bullet in projectiles:
        bullet.update()
        bullet.draw(displaySurface)
    
    pygame.display.update()
    clock.tick(60)
    