import pygame
import random
import sys

from pygments.styles.paraiso_light import PURPLE

# ustawienia
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 20
FPS = 8

# kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# kierunki
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def random_cell():
    x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1)
    y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1)
    return (x, y)

def draw_cell(position, color):
    rect = pygame.Rect(position[0]*CELL_SIZE, position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

# inicjalizacja gry
snake = [(10, 10)]  # pozycja startowa
direction = RIGHT
food = random_cell()
score = 0

# --- pętla gry ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # ruchy weza
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = ((head_x + dx) % (SCREEN_WIDTH // CELL_SIZE),
                (head_y + dy) % (SCREEN_HEIGHT // CELL_SIZE))

    # kolizja z samym soba
    if new_head in snake:
        print("Game Over! Wynik:", score)
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # zjedzenie owocu
    if new_head == food:
        score += 1
        food = random_cell()
    else:
        snake.pop()  # usuwa ogon

    # rysowanie
    screen.fill(BLACK)
    draw_cell(food, RED)
    for segment in snake:
        draw_cell(segment, PURPLE)
    pygame.display.flip()

    clock.tick(FPS)