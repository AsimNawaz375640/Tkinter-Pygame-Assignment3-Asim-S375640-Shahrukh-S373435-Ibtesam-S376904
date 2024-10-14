import pygame

# UI class for handling score, health, and game over screen
class UI:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font('assets/funky_font.otf', 36)
        self.score = 0

    def update_score(self, points):
        # Update the score based on points
        self.score += points

    def draw(self, screen):
        # Display health and score on the screen
        self.draw_health_bar(screen)
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    def draw_health_bar(self, screen):
        # Create a cool looking health bar
        health_ratio = self.player.health / 100
        pygame.draw.rect(screen, (0, 0, 0), (10, 50, 204, 24), 3)
        pygame.draw.rect(screen, (255, 0, 0), (12, 52, 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (12, 52, 200 * health_ratio, 20))

    def game_over(self, screen):
        # Display Game Over screen when player runs out of lives
        game_over_text = self.font.render("Game Over! Press R to Restart", True, (193, 18, 31))
        screen.blit(game_over_text, (screen.get_width() // 2 - 200, screen.get_height() // 2))
        pygame.display.flip()

    def handle_restart(self, event):
        # Handle game restart when the player presses 'Ctrl + R'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            return True
        return False
