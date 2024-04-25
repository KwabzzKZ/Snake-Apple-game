import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed = 15

# Apple variables
apple_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
apple_spawn = True

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

# Main game loop
def main():
    global snake_pos, snake_body, apple_pos, apple_spawn, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for key presses
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    change_to = "LEFT"
                elif keys[pygame.K_RIGHT]:
                    change_to = "RIGHT"
                elif keys[pygame.K_UP]:
                    change_to = "UP"
                elif keys[pygame.K_DOWN]:
                    change_to = "DOWN"

        # Change snake direction
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
        else:
            snake_body.pop()

        # Apple spawn
        if not apple_spawn:
            apple_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
            apple_spawn = True

        # Draw elements
        WIN.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(WIN, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(WIN, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))
        
        # Collision detection
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
            game_over()
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        # Refresh screen
        pygame.display.flip()
        pygame.time.Clock().tick(snake_speed)

if __name__ == "__main__":
    main()
