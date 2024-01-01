import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 400
FPS = 60
WHITE = (255, 255, 255)
PIPE_WIDTH = 50
GAP_HEIGHT = 100

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird properties
bird_size = 50
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_speed = 5

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - GAP_HEIGHT - 50)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height + GAP_HEIGHT, PIPE_WIDTH, HEIGHT))

    def move(self):
        self.x -= bird_speed

# Main game loop
clock = pygame.time.Clock()
is_game_over = False
pipes = [Pipe(WIDTH + i * 300) for i in range(2)]  # Initial pipes

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

    # Game logic here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_y -= bird_speed
    else:
        bird_y += 1  # Add gravity

    # Move pipes
    for pipe in pipes:
        pipe.move()

    # Generate new pipes
    if pipes[-1].x < WIDTH - 300:
        pipes.append(Pipe(WIDTH))

    # Remove off-screen pipes
    if pipes[0].x + PIPE_WIDTH < 0:
        pipes.pop(0)

    # Check for collisions with pipes
    for pipe in pipes:
        if (
            bird_x < pipe.x + PIPE_WIDTH
            and bird_x + bird_size > pipe.x
            and (bird_y < pipe.height or bird_y + bird_size > pipe.height + GAP_HEIGHT)
        ):
            is_game_over = True

    # Draw background
    screen.fill(WHITE)

    # Draw pipes
    for pipe in pipes:
        pipe.draw()

    # Draw bird
    pygame.draw.rect(screen, (255, 0, 0), (bird_x, int(bird_y), bird_size, bird_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
