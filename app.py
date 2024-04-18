import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
win_width = 800
win_height = 300
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Ball Game")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

# Set up game variables
ball_radius = 20
ball_x = 50
ball_y = 200
ball_vel = 5

cactus_x = win_width
cactus_y = 200
cactus_width = 32
cactus_height = 64
cactus_vel = 5

score = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(30)  # FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and ball_y == 200:  # Jump only if ball is on the ground
        ball_vel = -10

    ball_y += ball_vel
    if ball_y >= 200:
        ball_y = 200
        ball_vel = 0
    else:
        ball_vel += 0.5

    cactus_x -= cactus_vel
    if cactus_x + cactus_width < 0:
        cactus_x = win_width
        score += 1

    # Collision detection
    if ball_x + ball_radius > cactus_x and ball_x - ball_radius < cactus_x + cactus_width \
            and ball_y + ball_radius > cactus_y:
        running = False

    # Draw everything
    win.fill(WHITE)
    pygame.draw.circle(win, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(win, GREEN, (cactus_x, cactus_y, cactus_width, cactus_height))
    
    # Display score
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))
    
    pygame.display.update()

pygame.quit()
print("Game over! Your score:", score)
