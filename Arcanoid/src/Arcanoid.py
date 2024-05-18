import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((800, 600))

# Color settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
paddle = pygame.Rect(0, 0, 100, 20)
paddle.centerx = screen.get_width() // 2
paddle.bottom = screen.get_height() - 20

# Ball settings
ball = pygame.Rect(0, 0, 20, 20)
ball.centerx = screen.get_width() // 2
ball.centery = screen.get_height() // 2

# Ball movement settings
ball_speed_x = 3
ball_speed_y = -3

# Brick settings
brick_rows = 4
brick_cols = 10
brick_width = 60
brick_height = 20
brick_margin = 10
bricks = []

for i in range(brick_rows):
    for j in range(brick_cols):
        brick = pygame.Rect(
            j * (brick_width + brick_margin) + brick_margin,
            i * (brick_height + brick_margin) + brick_margin,
            brick_width,
            brick_height,
        )
        bricks.append(brick)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < screen.get_width():
        paddle.move_ip(5, 0)

    # Ball movement
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Ball bounce off the walls
    if ball.left <= 0 or ball.right >= screen.get_width():
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Ball bounce off the paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # Loss - ball drops below the bottom edge of the screen
    if ball.bottom > screen.get_height():
        print("You lose!")
        break

    # Win - all bricks have been destroyed
    if not bricks:
        print("You win!")
        break

    # Clearing the screen
    screen.fill(BLACK)

    # Drawing the paddle
    pygame.draw.rect(screen, WHITE, paddle)

    # Drawing the ball
    pygame.draw.circle(screen, WHITE, ball.center, ball.width // 2)

    # Drawing bricks
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Screen update
    pygame.display.flip()

    # Game speed control
    pygame.time.delay(10)
