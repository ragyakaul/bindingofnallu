import pygame
import settings


# Defining the Player class
class Player(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    image: pygame.Surface = None

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nel.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)

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
