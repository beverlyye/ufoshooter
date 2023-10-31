import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario-Style Game")

# Player variables
player_x = 100
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
player_velocity_x = 0
player_velocity_y = 0
jumping = False
on_ground = True
jump_count = 10

# Level
level_data = [
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "XXXXXXXXXXXXX                 ",
]

level_width = len(level_data[0])
level_height = len(level_data)
tile_size = SCREEN_WIDTH // level_width

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        player_velocity_x = 5
    else:
        player_velocity_x = 0

    if not jumping and on_ground:
        if keys[pygame.K_SPACE]:
            jumping = True
    if jumping:
        player_velocity_y = -jump_count
        jump_count -= 1

    # Apply gravity
    player_velocity_y += GRAVITY

    # Collision detection with the ground
    if player_y + PLAYER_HEIGHT + player_velocity_y > SCREEN_HEIGHT:
        player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
        jumping = False
        on_ground = True
        jump_count = 10
    else:
        on_ground = False

    # Update player position
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Draw the level
    for row in range(level_height):
        for col in range(level_width):
            if level_data[row][col] == "X":
                pygame.draw.rect(screen, GROUND_COLOR, (col * tile_size, row * tile_size, tile_size, tile_size))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()
sys.exit()





import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario-Style Game")

# Player variables
player_x = 100
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
player_velocity_x = 0
player_velocity_y = 0
jumping = False
on_ground = True
jump_count = 10

# Level
level_data = [
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "                              ",
    "XXXXXXXXXXXXX                 ",
]

level_width = len(level_data[0])
level_height = len(level_data)
tile_size = SCREEN_WIDTH // level_width

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_velocity_x = -5
    elif keys[pygame.K_RIGHT]:
        player_velocity_x = 5
    else:
        player_velocity_x = 0

    if not jumping and on_ground:
        if keys[pygame.K_SPACE]:
            jumping = True
    if jumping:
        player_velocity_y = -jump_count
        jump_count -= 1

    # Apply gravity
    player_velocity_y += GRAVITY

    # Collision detection with the ground
    if player_y + PLAYER_HEIGHT + player_velocity_y > SCREEN_HEIGHT:
        player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
        jumping = False
        on_ground = True
        jump_count = 10
    else:
        on_ground = False

    # Update player position
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Draw the level
    for row in range(level_height):
        for col in range(level_width):
            if level_data[row][col] == "X":
                pygame.draw.rect(screen, GROUND_COLOR, (col * tile_size, row * tile_size, tile_size, tile_size))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()
sys.exit()
