import pygame
import sys

import Snake.main
import Yahtzee.Run
from Sokoban import game
import Gomoku.main

pygame.init()

screen_width, screen_height = 960, 720
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (255, 240, 245)
screen.fill(background_color)

pygame.display.set_caption("All Games")

WHITE = (255, 255, 255)
BLUE = (0, 0, 128)

box_width, box_height = 100, 50
box_game_pairs = [
    (pygame.Rect(100, 100, box_width, box_height), game),
    (pygame.Rect(300, 100, box_width, box_height), game),
    (pygame.Rect(100, 300, box_width, box_height), game),
    (pygame.Rect(300, 300, box_width, box_height), game)
]

images = {
    'game1': pygame.image.load('img/box_cover.png'),
    'game2': pygame.image.load('img/snake.png'),
    'game3': pygame.image.load('img/dice.png'),
    'game4': pygame.image.load('img/gomoku.png')
}

positions = {
    'game1': (45, 230),
    'game2': (270, 230),
    'game3': (495, 230),
    'game4': (720, 230)
}

image_rects = {key: images[key].get_rect(topleft=pos) for key, pos in positions.items()}


# draw a rounded corner rectangle
def draw_rounded_rect(surface, color, rect, corner_radius):
    """ Draws a rectangle with rounded corners on the given surface. """
    x, y, width, height = rect
    pygame.draw.rect(surface, color, (x, y + corner_radius, width, height - corner_radius * 2))
    pygame.draw.rect(surface, color, (x + corner_radius, y, width - corner_radius * 2, corner_radius))
    pygame.draw.rect(surface, color,
                     (x + corner_radius, y + height - corner_radius, width - corner_radius * 2, corner_radius))

    pygame.draw.circle(surface, color, (x + corner_radius, y + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (x + width - corner_radius, y + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (x + corner_radius, y + height - corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (x + width - corner_radius, y + height - corner_radius), corner_radius)


# draw a rounded corner rectangle with shadow
def draw_rounded_rect_with_shadow(surface, color, rect, corner_radius, shadow_offset=(5, 5), shadow_color=(0, 0, 0)):
    shadow_rect = (rect[0] + shadow_offset[0], rect[1] + shadow_offset[1], rect[2], rect[3])
    draw_rounded_rect(surface, shadow_color, shadow_rect, corner_radius)  # Shadow
    draw_rounded_rect(surface, color, rect, corner_radius)  # Main rectangle


# draw a text in the screen
def draw_text(font, text, text_color, text_center):
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=text_center)
    screen.blit(text_surface, text_rect)


font_large = pygame.font.Font(None, 32)
font_small = pygame.font.Font(None, 24)

# This is the integrated gaming platform.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            rect_game1 = image_rects.get('game1')
            rect_game2 = image_rects.get('game2')
            rect_game3 = image_rects.get('game3')
            rect_game4 = image_rects.get('game4')
            if rect_game1.collidepoint(mouse_pos):
                game.sokoban()
            if rect_game2.collidepoint(mouse_pos):
                Snake.main.game()
            if rect_game3.collidepoint(mouse_pos):
                Yahtzee.Run.run()
            if rect_game4.collidepoint(mouse_pos):
                Gomoku.main.run()
            pygame.display.set_caption("Games")

    screen.fill((255, 192, 203))
    draw_rounded_rect_with_shadow(screen, (255, 255, 255), (40, 225, 210, 270), 5, shadow_offset=(5, 5),
                                  shadow_color=(235, 172, 183))
    draw_rounded_rect_with_shadow(screen, (255, 255, 255), (265, 225, 210, 270), 5, shadow_offset=(5, 5),
                                  shadow_color=(235, 172, 183))
    draw_rounded_rect_with_shadow(screen, (255, 255, 255), (490, 225, 210, 270), 5, shadow_offset=(5, 5),
                                  shadow_color=(235, 172, 183))
    draw_rounded_rect_with_shadow(screen, (255, 255, 255), (715, 225, 210, 270), 5, shadow_offset=(5, 5),
                                  shadow_color=(235, 172, 183))

    draw_text(font_large, "CLICK ONE GAME TO START...", (255, 255, 255), (200, 540))

    draw_text(font_small, "SOKOBAN", (235, 172, 183), (145, 460))
    draw_text(font_small, "SNAKE", (235, 172, 183), (370, 460))
    draw_text(font_small, "YAHTZEE", (235, 172, 183), (595, 460))
    draw_text(font_small, "GOMOKU", (235, 172, 183), (820, 460))

    if pygame.display.get_window_size()[0] != screen_width or pygame.display.get_window_size()[1] != screen_height:
        pygame.display.set_mode((screen_width, screen_height))
    for image, rect in zip(images.values(), image_rects.values()):
        screen.blit(image, rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
