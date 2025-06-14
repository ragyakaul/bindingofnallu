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

while True:

    for event in pygame.event.get():
        # Quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Shooting Projectiles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.shoot(dx=0, dy=-10)
            elif event.key == pygame.K_s:
                player.shoot(dx=0, dy=10)
            elif event.key == pygame.K_a:
                player.shoot(dx=-10, dy=0)
            elif event.key == pygame.K_d:
                player.shoot(dx=10, dy=0)
   
    player.update()
    enemy.update(player)
    
   

    # Draw the background
    displaySurface.blit(background, (0, 0))
    # Draw the player
    player.draw(displaySurface)
    # Draw the enemy
    enemy.draw(displaySurface)

    # Draw bullets on top
    for bullet in player.projectiles[:]:
        bullet.update()
        bullet.draw(displaySurface)
        # Collision detection
        if bullet.rect.colliderect(enemy.rect):
            player.projectiles.remove(bullet)
            print("Enemy hit")
            if enemy.health > 0:
                enemy.health -= 1
            else:
                print("Enemy has been defeated!")
                pygame.quit()
                sys.exit()
            

    # Enemy projectiles
    for p in enemy.projectiles:
        p.draw(displaySurface)
        # Check if it hits player
        if p.rect.colliderect(player.rect):
            enemy.projectiles.remove(p)
            print("Player hit by enemy projectile!")
            if player.health > 0:
                player.health -=1
            else:
                print("Player has been defeated!")
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
    