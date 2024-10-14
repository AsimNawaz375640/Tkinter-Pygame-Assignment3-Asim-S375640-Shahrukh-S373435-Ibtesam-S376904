import pygame
from player import Player
from projectile import Projectile
from enemy import Enemy
from collectible import Collectible
from level import Level
from camera import Camera
from ui import UI

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side-Scrolling 2D Game")
clock = pygame.time.Clock()

# Load the background image from assets
background = pygame.image.load('assets/background.png')


# Function to show splash screen
def splash_screen():
    screen.fill((0, 0, 0))

    font = pygame.font.Font('assets/funky_font.otf', 60)
    title_text = font.render("Welcome to the Game!", True, (0, 255, 0))

    # Center the title text
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(title_text, title_rect)

    # Load the font for the prompt text
    prompt_font = pygame.font.Font('assets/funky_font.otf', 36)

    # Manually split lines since Pygame does not support multi-line rendering in one go
    prompts = [
        "Press ENTER to Start",
        "Press Z to Shoot",
        "Press Space to Jump",
        "Use Left/Right Arrow Keys to Move"
    ]

    # Draw each line of the prompt text with a small vertical gap between lines
    y_offset = 50
    for index, prompt in enumerate(prompts):
        prompt_text = prompt_font.render(prompt, True, (255, 255, 255))
        prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset + index * 40))
        screen.blit(prompt_text, prompt_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False


# Function to show level transition screen
def level_transition_screen(level_num):
    screen.fill((0, 0, 0))
    font = pygame.font.Font('assets/funky_font.otf', 48)
    level_text = font.render(f"Level {level_num}", True, (255, 255, 0))
    screen.blit(level_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    # Wait for 2 seconds
    pygame.time.wait(2000)


# Game Loop
def game_loop():
    # Initialize game components
    # Show splash screen at the start
    splash_screen()

    player = Player('assets/Player.png')
    level = Level(1)
    camera = Camera(player)
    ui = UI(player)
    projectiles = pygame.sprite.Group()

    running = True
    # Flag to check if the player has won the game
    game_won = False
    # Flag to check if the player has lost the game
    game_over = False

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle game over scenario
        if game_over:
            # Display game over screen
            ui.game_over(screen)
            for event in pygame.event.get():
                # Restart if 'R' is pressed
                if ui.handle_restart(event):
                    player.lives = 3
                    player.health = 100
                    level = Level(1)
                    ui.score = 0
                    projectiles.empty()
                    game_won = False
                    # Reset game_over flag
                    game_over = False
                    # Skip rest of the loop if the game is over
            continue

        # If game is won, display victory message and stop updating the game
        if game_won:
            victory_text = ui.font.render("You Won! Press Ctrl + R to Restart", True, (0, 0, 0))
            screen.blit(victory_text, (screen.get_width() // 2 - 200, screen.get_height() // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if ui.handle_restart(event):
                    player.lives = 3
                    player.health = 100
                    level = Level(1)
                    ui.score = 0
                    projectiles.empty()
                    # Reset game_won flag for restart
                    game_won = False
                    # Skip the rest of the game logic if the player has won
            continue

        # Handle player input
        keys = pygame.key.get_pressed()
        # 'Z' key to shoot
        if keys[pygame.K_z]:
            projectile = player.shoot()
            projectiles.add(projectile)

        # Update game components and check if the level is cleared
        # This will return True if the max level duration is reached
        level_complete = level.update()
        projectiles.update()
        player.update(keys)
        camera.update(player)

        # Collision detection between projectiles and enemies
        for projectile in projectiles:
            enemies_hit = pygame.sprite.spritecollide(projectile, level.enemies, False)
            for enemy in enemies_hit:
                # Apply damage to the enemy
                enemy.take_damage(25)
                # Remove projectile after hit
                projectile.kill()

        # Collision detection between player and enemies (reduce health)
        enemies_touching = pygame.sprite.spritecollide(player, level.enemies, False)
        for enemy in enemies_touching:
            # Reduce health by 10 each time player collides with enemy
            player.take_damage(10)

        # Check if player is out of lives
        if player.lives <= 0:
            # Set the game_over flag
            game_over = True

        # Collision detection between player and collectibles
        collectibles_hit = pygame.sprite.spritecollide(player, level.collectibles, True)
        for collectible in collectibles_hit:
            # Apply the collectible's effect to the player
            collectible.apply_effect(player)
            # Increase score for each collectible collected
            ui.update_score(10)

        # Transition to the next level if the current level is complete and player is not in game over
        if (level_complete or level.is_level_cleared()) and not game_over:
            if level.level_number < 3:
                level = Level(level.level_number + 1)
                # Show level transition screen
                level_transition_screen(level.level_number)
            else:
                # Set the game_won flag to True to stop the game and show the victory message
                game_won = True

        # Draw everything
        screen.blit(background, (0, 0))  # Draw the background
        for sprite in projectiles:
            screen.blit(sprite.image, camera.apply(sprite))
        level.draw(screen, camera)
        screen.blit(player.image, camera.apply(player))
        ui.draw(screen)

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    game_loop()
