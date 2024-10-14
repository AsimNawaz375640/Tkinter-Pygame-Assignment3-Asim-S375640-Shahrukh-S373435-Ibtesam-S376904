import pygame


# Camera class
class Camera:
    def __init__(self, player):
        # Initial camera size, same as screen size
        self.camera = pygame.Rect(0, 0, 800, 600)
        self.player = player
        # Total width of the game world
        self.width = 1600
        # Total height of the game world
        self.height = 600

    def apply(self, entity):
        # Apply the camera offset to each entity
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Move the camera to follow the player
        # Keep the player centered on the x-axis
        x = -target.rect.x + int(800 / 2)
        # Keep the player centered on the y-axis
        y = -target.rect.y + int(600 / 2)

        # Limit scrolling to the bounds of the level
        # Left bound
        x = min(0, x)
        # Right bound
        x = max(-(self.width - 800), x)
        # Top bound
        y = min(0, y)
        # Bottom bound
        y = max(-(self.height - 600), y)

        self.camera = pygame.Rect(x, y, 800, 600)
