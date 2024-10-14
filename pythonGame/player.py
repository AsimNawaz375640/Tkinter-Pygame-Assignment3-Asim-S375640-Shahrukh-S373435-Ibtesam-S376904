import pygame
from projectile import Projectile


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        # Load the player image from assets
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.speed_x = 5
        self.speed_y = 0
        # Increased jump speed for higher jumps
        self.jump_speed = -20
        self.gravity = 0.6
        self.health = 100
        self.lives = 3
        self.on_ground = False

    def update(self, keys):
        # Apply gravity
        self.speed_y += self.gravity
        # Ground level
        if self.rect.y >= 500:
            self.rect.y = 500
            self.speed_y = 0
            self.on_ground = True

        # Handle movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x

        # Handle jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.speed_y = self.jump_speed
            self.on_ground = False

        # Apply vertical movement
        self.rect.y += self.speed_y

    def shoot(self):
        # Create a new projectile and return it
        return Projectile(self.rect.right, self.rect.centery)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.lives -= 1
            # Reset health when a life is lost
            self.health = 100
            if self.lives <= 0:
                # Player is out of lives and removed from the game
                self.kill()
