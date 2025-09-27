import pygame
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen_width = 800
screen_height = 400
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Thunder_Snake Game")

snake_size = 15
snake_x = 45
snake_y = 55
speed_x = 0
speed_y = 0

food_size = 10
food_x = random.randint(20, int(screen_width/2))
food_y = random.randint(20, int(screen_height/2))

score = 0

fps = 40
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -5
                speed_y = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 5
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 5
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = -5
                speed_x = 0


    snake_x += speed_x
    snake_y += speed_y

    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score += 10
        print("Score:", score)
        food_x = random.randint(20, int(screen_width/2))
        food_y = random.randint(20, int(screen_height/2))


    if snake_x < 0 or snake_x > screen_width-snake_size or snake_y < 0 or snake_y > screen_height-snake_size:
        print("Game Over! Final Score:", score)
        running = False

        blue = 2
        green = 3
        red = 4
        black = 1
        random.randint(1,4)


 
    game_window.fill(white)
    pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(game_window, green, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(game_window, blue, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()


