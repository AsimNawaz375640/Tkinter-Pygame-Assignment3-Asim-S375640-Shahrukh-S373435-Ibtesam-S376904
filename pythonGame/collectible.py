import pygame
import random

# Collectible class
class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the health image
        self.image = pygame.image.load('assets/Health.png')
        self.rect = self.image.get_rect()
        # Random position on screen
        self.rect.x = random.randint(300, 700)
        self.rect.y = random.randint(100, 400)
        # Randomly choose collectible type
        self.type = random.choice(['health', 'life'])

    def apply_effect(self, player):
        # Apply the effect of the collectible to the player
        if self.type == 'health':
            # Add health but cap at 100
            player.health = min(player.health + 20, 100)
        elif self.type == 'life':
            # Add an extra life
            player.lives += 1
            # Remove collectible once applied
        self.kill()
