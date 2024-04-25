import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed = 15

# Apple variables
apple_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
apple_spawn = True

# Pineapple variables
pineapple_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
pineapple_spawn = False
pineapple_timer = 0
bonus_points = 0

# Score variable
score = 0

# Game over function
def game_over():
    font = pygame.font.SysFont('Arial', 30)
    game_over_text = font.render(f'Game Over! Score: {score}', True, RED)
    WIN.blit(game_over_text, [WIDTH / 3, HEIGHT / 3])
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

# Keyboard bindings
def go_up():
    global change_to
    if snake_direction != "DOWN":
        change_to = "UP"

def go_down():
    global change_to
    if snake_direction != "UP":
        change_to = "DOWN"

def go_left():
    global change_to
    if snake_direction != "RIGHT":
        change_to = "LEFT"

def go_right():
    global change_to
    if snake_direction != "LEFT":
        change_to = "RIGHT"

# Main game loop
def main():
    global snake_pos, snake_body, apple_pos, apple_spawn, pineapple_pos, pineapple_spawn, pineapple_timer, bonus_points, score, change_to

    running = True  # Add a variable to control the main loop

    while running:  # Use the variable to control the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the loop when the window is closed

        # Keyboard bindings
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            go_up()
        elif keys[pygame.K_s]:
            go_down()
        elif keys[pygame.K_a]:
            go_left()
        elif keys[pygame.K_d]:
            go_right()

        # Change snake direction
        global snake_direction  # Declare snake_direction as global
        if change_to == "LEFT" and not snake_direction == "RIGHT":
            snake_direction = "LEFT"
        elif change_to == "RIGHT" and not snake_direction == "LEFT":
            snake_direction = "RIGHT"
        elif change_to == "UP" and not snake_direction == "DOWN":
            snake_direction = "UP"
        elif change_to == "DOWN" and not snake_direction == "UP":
            snake_direction = "DOWN"

        # Move snake
        if snake_direction == "LEFT":
            snake_pos[0] -= 10
        elif snake_direction == "RIGHT":
            snake_pos[0] += 10
        elif snake_direction == "UP":
            snake_pos[1] -= 10
        elif snake_direction == "DOWN":
            snake_pos[1] += 10

        # Snake body growth
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            score += 1
            apple_spawn = False
            bonus_points += 1
            if bonus_points % 5 == 0:
                score += 5
        elif snake_pos[0] == pineapple_pos[0] and snake_pos[1] == pineapple_pos[1]:
            score += 10
            pineapple_spawn = False
        else:
            snake_body.pop()

        # Apple spawn
        if not apple_spawn:
            apple_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
            apple_spawn = True

        # Pineapple spawn
        pineapple_timer += 1
        if pineapple_timer == 300:  # 5 seconds (60 frames per second * 5)
            pineapple_spawn = True
            pineapple_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
            pineapple_timer = 0

        # Draw elements
        WIN.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(WIN, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(WIN, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))
        if pineapple_spawn:
            pygame.draw.rect(WIN, YELLOW, pygame.Rect(pineapple_pos[0], pineapple_pos[1], 10, 10))

        # Collision detection
        # Detect collision with window edges
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
            game_over()

        # Detect collision with snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        # Refresh screen
        pygame.display.flip()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()  # Call pygame.quit() outside the loop to properly close the game window

if __name__ == "__main__":
    main()
