import pygame
import time
import random
pygame.init()
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
snake_block = 10
snake_speed = 15
font = pygame.font.SysFont(None, 25)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])
def game_loop():
    game_over = False
    game_close = False
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            game_display.fill(white)
            game_over_text = font.render("Game Over! Press C-Play Again or Q-Quit", True, red)
            game_display.blit(game_over_text, [width / 6, height / 3])
            our_snake(snake_block, snake_list)
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
                    lead_x_change = -snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_block
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = snake_block
                    lead_x_change = 0
        if (
            lead_x >= width
            or lead_x < 0
            or lead_y >= height
            or lead_y < 0
        ):
            game_close = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)
        pygame.display.update()
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        pygame.time.Clock().tick(snake_speed)
    pygame.quit()
    quit()
game_loop()
