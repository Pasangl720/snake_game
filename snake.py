import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
snake_size = 10
snake_speed = 15
direction = "right"


def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, black, [x, y, snake_size, snake_size])


# Set up the food
food_size = 10
food_x = round(random.randrange(0, width - food_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - food_size) / 10.0) * 10.0

# Set up the score
font = pygame.font.SysFont(None, 25)


def display_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, [0, 0])


# Start the game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    while not game_over:

        while game_close == True:
            window.fill(white)
            display_score(Length_of_snake - 1)
            game_over_text = font.render("Game Over! Press Q-Quit or C-Play Again", True, black)
            window.blit(game_over_text, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    direction = "right"
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    x1_change = 0
                    y1_change = -snake_size  # The code block after this elif statement was missing.
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    x1_change = 0
                    y1_change = snake_size

                if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                    game_close = True

                x1 += x1_change
                y1 += y1_change
                window.fill(white)
                pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])

                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)


