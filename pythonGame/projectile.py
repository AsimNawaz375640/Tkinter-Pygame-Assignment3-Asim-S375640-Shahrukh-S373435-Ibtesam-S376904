import pygame

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        # Red color for projectile
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Speed of projectile
        self.speed_x = 10

    def update(self, *args):
        # Move projectile to the right
        self.rect.x += self.speed_x

        # Remove projectile if it goes off-screen
        # Assuming screen width is 800
        if self.rect.x > 800:
            self.kill()

