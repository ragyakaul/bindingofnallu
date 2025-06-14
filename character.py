import pygame


class Character(pygame.sprite.Sprite):
    rect: pygame.Rect = None
    image: pygame.Surface = None

    def __init__(self):
        super().__init__()
        self.image = None   # Base class does not load data but expects derived classes to define it
        self.rect = None
        self.projectiles = []
        self.health = 0
    
    def initialize_rect(self, x, y):
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (x, y) # Default position, can be overridden in derived classes
        else:
            self.rect = pygame.Rect(x, y, 0, 0)  # Fallback if no image is set

    def update(self, *args):
        """To be overriden: updates character state."""
        raise NotImplementedError("Update method must be implemented in derived classes.")
    
    def shoot(self, *args):
        """To be overriden: handles shooting logic."""
        raise NotImplementedError("Shoot method must be implemented in derived classes.")
    

    def draw(self, surface: pygame.Surface): # type hinting
        # Puts the image on the surface at the rect position
        if self.image and self.rect:
            surface.blit(self.image, self.rect)
    
    
            