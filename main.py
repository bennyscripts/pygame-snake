import pygame
import random

from utils import Snake
from utils import Apple

pygame.font.init()

font = pygame.font.SysFont('Arial', 18)
size = (300, 300)
background_color = (0, 0, 0)
rendered_game_over = False

screen = pygame.display.set_mode(size)
screen.fill(background_color)
pygame.display.set_caption("Snake")

snake = Snake(screen, background_color, size[0] / 2, size[1] / 2, 10, 10, (255, 255, 255))
apples = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if snake.game_over == False:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("right")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("left")
                elif event.key == pygame.K_UP:
                    snake.change_direction("up")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("down")
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.key == pygame.K_RETURN:
                snake.reset(size[0] / 2, size[1] / 2)
                apples = []
                rendered_game_over = False
                screen.fill(background_color)
            elif event.key == pygame.K_SPACE:
                snake.game_over = False
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
 
    if snake.game_over == False:
        if len(apples) < 1:
            x = random.randint(0, size[0] - 10)
            y = random.randint(0, size[1] - 10)

            x = x - x % 10
            y = y - y % 10

            apples.append(Apple(screen, background_color, x, y, 10, 10, (255, 0, 0)))
    
        screen.fill(background_color)
    
        for apple in apples:
            apple.draw()
    
        snake.draw()
        snake.move()
        snake.check_collision()
    
        for apple in apples:
            if snake.check_collision_with_food(apple):
                apples.remove(apple)

        text = font.render("Score: " + str(snake.score), True, (255, 255, 255))
        screen.blit(text, (10, 10))
    
    else:
        if rendered_game_over == False:
            rendered_game_over = True

            text = font.render("Game Over", True, (255, 255, 255))
            text2 = font.render("Press Enter to restart", True, (255, 255, 255))
            
            screen.blit(text, (size[0] / 2 - text.get_width() / 2, size[1] / 2 - text.get_height() / 2 - 20))
            screen.blit(text2, (size[0] / 2 - text2.get_width() / 2, size[1] / 2 - text2.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(85)