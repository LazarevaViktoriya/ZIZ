import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размера экрана и размера блоков
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 10

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Определение функций
def draw_block(color, row, column):
    """Отрисовка блока на экране"""
    pygame.draw.rect(screen, color, [column * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])

def generate_food():
    """Генерация случайной еды для змейки"""
    food_row = random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1)
    food_column = random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1)
    return food_row, food_column

# Инициализация переменных
game_over = False

# Создание змейки
snake = [(SCREEN_HEIGHT // BLOCK_SIZE) // 2, (SCREEN_WIDTH // BLOCK_SIZE) // 2]
snake_direction = "right"

# Создание еды
food_row, food_column = generate_food()

# Главный игровой цикл
while not game_over:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT:
                snake_direction = "right"
            elif event.key == pygame.K_UP:
                snake_direction = "up"
            elif event.key == pygame.K_DOWN:
                snake_direction = "down"
    
    # Перемещение змейки
    if snake_direction == "left":
        snake[1] -= 1
    elif snake_direction == "right":
        snake[1] += 1
    elif snake_direction == "up":
        snake[0] -= 1
    elif snake_direction == "down":
        snake[0] += 1
    
    # Проверка на столкновение со стенками
    if snake[0] < 0 or snake[0] >= SCREEN_HEIGHT // BLOCK_SIZE or snake[1] < 0 or snake[1] >= SCREEN_WIDTH // BLOCK_SIZE:
        game_over = True
    
    # Проверка на столкновение с телом змейки
    for block in snake[1:]:
        if snake[0] == block[0] and snake[1] == block[1]:
            game_over = True
    
    # Проверка на съедание еды
    if snake[0] == food_row and snake[1] == food_column:
        food_row, food_column = generate_food()
        snake.append(snake[-1])
    
    # Отрисовка фона
    screen.fill(BLACK)
    
    # Отрисовка еды
    draw_block(RED, food_row)
