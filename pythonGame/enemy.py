import pygame

import random


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, level_number):
        super().__init__()
        # Load the enemy image
        self.image = pygame.image.load('assets/Enemy.png')
        # Keep a reference to the original image
        self.original_image = self.image
        self.rect = self.image.get_rect()

        # Calculate scaling factor based on level
        # Scale up by 20% each level
        scale_factor = 1 + (level_number - 1) * 0.2

        # Resize the enemy based on the level
        width = int(self.rect.width * scale_factor)
        height = int(self.rect.height * scale_factor)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        # Update rect after scaling
        self.rect = self.image.get_rect()
        # Random spawn point off-screen
        self.rect.x = random.randint(800, 1000)
        # Ground level
        self.rect.y = 500
        # Random speed for enemies
        self.speed_x = random.randint(3, 6)
        # Increase health per level
        self.health = 50 + (level_number - 1) * 10

    def update(self):
        # Move enemy to the left
        self.rect.x -= self.speed_x

        # Remove enemy if it goes off-screen
        if self.rect.x < 0:
            self.kill()

    def take_damage(self, amount):
        # Reduce enemy health by the damage amount
        self.health -= amount
        if self.health <= 0:
            # Remove enemy from game if health is zero or less
            self.kill()
