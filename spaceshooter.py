import pygame
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

player_img = pygame.image.load("player.png")
player_x = screen_width // 2
player_y = screen_height - 64
player_x_change = 0

enemy_img = pygame.image.load("enemy.png")
enemies = []
num_enemies = 6
for _ in range(num_enemies):
    enemy_x = random.randint(0, screen_width - 64)
    enemy_y = random.randint(50, 200)
    enemy_x_change = 4
    enemy_y_change = 40
    enemies.append((enemy_img, enemy_x, enemy_y, enemy_x_change, enemy_y_change))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    # Ensure player stays within the screen boundaries

    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the player
    screen.blit(player_img, (player_x, player_y))

    # Draw and update enemies
    for enemy in enemies:
        enemy_img, enemy_x, enemy_y, enemy_x_change, enemy_y_change = enemy
        screen.blit(enemy_img, (enemy_x, enemy_y))

        # Add enemy movement and collision logic

    pygame.display.update()
