# Not Complete yet...

import pygame
import random

pygame.init()

# Window dimensions
WIDTH = 500
HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird dimensions
BIRD_WIDTH = 64
BIRD_HEIGHT = 48

# Pipe dimensions
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(200, 400)
GAP = 150

# Bird position and velocity
bird_x = int(WIDTH / 3) 
bird_y = int(HEIGHT / 2)
bird_y_velocity = 0

# Score
score = 0

# Game over flag
game_over = False

# Set up the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

# Load pipe images
pipe_bottom_img = pygame.image.load("pipe.png")
pipe_top_img = pygame.transform.flip(pipe_bottom_img, False, True)

# Resize pipe images
pipe_bottom_img = pygame.transform.scale(pipe_bottom_img, (PIPE_WIDTH, PIPE_HEIGHT))
pipe_top_img = pygame.transform.scale(pipe_top_img, (PIPE_WIDTH, HEIGHT - PIPE_HEIGHT - GAP))

def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    window.blit(text, (10, 10))

def display_bird():
    window.blit(bird_img, (bird_x, bird_y))

def display_pipes(pipes):
    for pipe in pipes:
        window.blit(pipe_bottom_img, (pipe["x"], pipe["bottom_height"]))
        window.blit(pipe_top_img, (pipe["x"], pipe["top_height"]))

def move_bird():
    global bird_y, bird_y_velocity, game_over

    bird_y += bird_y_velocity
    bird_y_velocity += 1

    # Check for collision with the ground
    if bird_y + BIRD_HEIGHT > HEIGHT - 100:
        game_over = True

def move_pipes(pipes):
    for pipe in pipes:
        pipe["x"] -= 2

        # Check for collision with the bird
        if bird_x + BIRD_WIDTH > pipe["x"] and bird_x < pipe["x"] + PIPE_WIDTH:
            if bird_y < pipe["top_height"] or bird_y + BIRD_HEIGHT > pipe["bottom_height"]:
                return True

        # Increase score if bird passes the pipe
        if bird_x > pipe["x"] + PIPE_WIDTH and not pipe["scored"]:
            pipe["scored"] = True
            global score
            score += 1

        # Remove pipes that are off the screen
        if pipe["x"] + PIPE_WIDTH < 0:
            pipes.remove(pipe)

def generate_pipe(pipes):
    new_pipe = {
        "x": WIDTH,
        "top_height": random.randint(50, HEIGHT - PIPE_HEIGHT - GAP),
        "bottom_height": random.randint(PIPE_HEIGHT + GAP, HEIGHT - 100),
        "scored": False
    }
    pipes.append(new_pipe)

def game_loop():
    global game_over, score

    clock = pygame.time.Clock()

    pipes = []
    generate_pipe(pipes)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_velocity = -10

        window.fill(WHITE)

        move_bird()
        display_bird()

        if move_pipes(pipes):
            game_over = True

        display_pipes(pipes)

        if pipes[-1]["x"] < WIDTH - 200:
            generate_pipe(pipes)

        display_score()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()





