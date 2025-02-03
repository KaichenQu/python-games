import sys

import pygame
from Snake.snake import Snake
from Snake.food import Food
from Snake.scoreboard import Scoreboard

pygame.init()


width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Snake Game")

# welcome page
fancy_font = pygame.font.Font('./Snake/fancy_font.ttf', 40)
original_start_image = pygame.image.load('./Snake/background1.jpg')
start_image = pygame.transform.scale(original_start_image, (width, height))


def welcome_screen():
    welcome_background = pygame.image.load('./Snake/background1.jpg')
    welcome_background = pygame.transform.scale(welcome_background, (width, height))

    text_color = (255, 0, 255)
    welcome_text = fancy_font.render("Welcome to Snake Game!", True, text_color)
    welcome_text_rect = welcome_text.get_rect(center=(width / 2, height / 2 - 70))

    smaller_font = pygame.font.Font('./Snake/fancy_font.ttf', 24)
    team_text = smaller_font.render("Team YSKZ", True, (0, 0, 0))
    team_text_rect = team_text.get_rect(center=(width / 2, height / 2 + 170))

    click_to_start_image = pygame.image.load('./Snake/click_to_start.png')
    image_size = (170, 90)
    click_to_start_image = pygame.transform.scale(click_to_start_image, image_size)
    click_to_start_rect = click_to_start_image.get_rect(center=(width / 2, height / 2 + 70))

    while True:
        screen.blit(welcome_background, (0, 0))
        screen.blit(click_to_start_image, click_to_start_rect)
        screen.blit(welcome_text, welcome_text_rect)
        screen.blit(team_text, team_text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

def game():
    pygame.init()

    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    welcome_screen()

    # actual game
    original_background_image = pygame.image.load('./Snake/background.jpg')
    background_image = pygame.transform.scale(original_background_image, (width, height))
    font = pygame.font.Font('./Snake/fancy_font.ttf', 24)

    snake = Snake(screen)
    food = Food(screen, width, height)
    scoreboard = Scoreboard(screen, font)

    # main game
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        snake.move()
        snake.draw()
        food.draw()
        scoreboard.show_score()

        if snake.eat(food):
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        if snake.is_collision(width, height):
            running = False
            scoreboard.game_over()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)

        pygame.display.update()
        pygame.time.delay(100)



if __name__ == '__main__':
    game()
    pygame.quit()