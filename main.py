import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen = pygame.display.set_mode((800, 600))

# Ustawienia kolorów
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ustawienia racketki
racket = pygame.Rect(0, 0, 100, 20)
racket.centerx = screen.get_width() // 2
racket.bottom = screen.get_height() - 20

# Ustawienia piłki
ball = pygame.Rect(0, 0, 20, 20)
ball.centerx = screen.get_width() // 2
ball.centery = screen.get_height() // 2

# Ustawienia ruchu piłki
ball_speed_x = 3
ball_speed_y = -3

# Ustawienia cegieł
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

    if keys[pygame.K_LEFT] and racket.left > 0:
        racket.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and racket.right < screen.get_width():
        racket.move_ip(5, 0)

    # Ruch piłki
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Odbijanie piłki od ścian
    if ball.left <= 0 or ball.right >= screen.get_width():
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Odbijanie piłki od racketki
    if ball.colliderect(racket):
        ball_speed_y = -ball_speed_y

    # Kolizja piłki z cegłami
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # Przegrana - piłka opada poniżej dolnej krawędzi ekranu
    if ball.bottom > screen.get_height():
        print("Przegrana!")
        break

    # Wygrana - wszystkie cegły zostały zniszczone
    if not bricks:
        print("Wygrana!")
        break

    # Czyszczenie ekranu
    screen.fill(BLACK)

    # Rysowanie racketki
    pygame.draw.rect(screen, WHITE, racket)

    # Rysowanie piłki
    pygame.draw.circle(screen, WHITE, ball.center, ball.width // 2)

    # Rysowanie cegieł
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Aktualizacja ekranu
    pygame.display.flip()

    # Kontrola szybkości gry
    pygame.time.delay(10)
