import pygame
from enemy import Enemy
from collectible import Collectible
import random


# Level class
class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        # Timer to control enemy respawn rate
        self.spawn_timer = 0
        # Timer to control collectible respawn rate
        self.collectible_timer = 0
        # Limit the number of enemies per level
        self.max_enemies = 10
        # Set maximum level duration
        self.max_duration = 600
        # Timer to track how long the level has been running
        self.duration_timer = 0
        # Load level after initializing variables
        self.load_level()

    def load_level(self):
        # Load different levels with unique configurations
        if self.level_number == 1:
            # Start with 5 enemies in level 1
            self.spawn_enemies(5)
            self.spawn_collectibles(2)
        elif self.level_number == 2:
            # Start with 7 enemies in level 2
            self.spawn_enemies(7)
            self.spawn_collectibles(3)
        # Boss Level
        elif self.level_number == 3:
            self.spawn_boss()
            self.spawn_collectibles(1)

    def spawn_enemies(self, count):
        # Spawn a given number of regular enemies
        for _ in range(count):
            # Ensure enemy count limit
            if len(self.enemies) < self.max_enemies:
                # Pass level number to the enemy
                enemy = Enemy(self.level_number)
                self.enemies.add(enemy)

    def spawn_collectibles(self, count):
        # Spawn a given number of collectibles
        for _ in range(count):
            collectible = Collectible()
            self.collectibles.add(collectible)

    def spawn_boss(self):
        # Create a boss enemy with more health and different behavior
        # Scale boss based on the current level
        boss = Enemy(self.level_number)
        # Increased health for the boss
        boss.health = 200 + (self.level_number - 1) * 50
        self.enemies.add(boss)

    def update(self):
        # Update enemies and collectibles in the level
        self.enemies.update()
        self.collectibles.update()

        # Enemy respawn logic - respawn every 3 seconds for regular levels
        # No respawn in boss level
        if self.level_number < 3:
            self.spawn_timer += 1
            # 180 frames (~3 seconds)
            if self.spawn_timer > 180:
                # Limit the number of enemies
                if len(self.enemies) < self.max_enemies:
                    # Pass level number to the enemy
                    enemy = Enemy(self.level_number)
                    self.enemies.add(enemy)
                self.spawn_timer = 0

        # Collectible respawn logic - respawn every 5 seconds
        self.collectible_timer += 1
        # 300 frames (~5 seconds)
        if self.collectible_timer > 300:
            # Ensure max of 3 collectibles at a time
            if len(self.collectibles) < 3:
                self.spawn_collectibles(1)
            self.collectible_timer = 0

        # Level duration logic
        self.duration_timer += 1
        # If the max duration is reached, end the level
        if self.duration_timer >= self.max_duration:
            # Return True to signal that the level duration has been exceeded
            return True
            # Continue the level
        return False

    def draw(self, screen, camera):
        # Draw enemies and collectibles on the screen
        for enemy in self.enemies:
            screen.blit(enemy.image, camera.apply(enemy))
        for collectible in self.collectibles:
            screen.blit(collectible.image, camera.apply(collectible))

    def is_level_cleared(self):
        # Check if all enemies are defeated
        return len(self.enemies) == 0 and self.level_number == 3
