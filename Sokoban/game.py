import pygame
import copy

block_img = pygame.image.load('./Sokoban/img/block.png')
wall_img = pygame.image.load('./Sokoban/img/wall.png')
ball_img = pygame.image.load('./Sokoban/img/ball.png')
box_img = pygame.image.load('./Sokoban/img/box.png')
up_img = pygame.image.load('./Sokoban/img/up.png')
down_img = pygame.image.load('./Sokoban/img/down.png')
left_img = pygame.image.load('./Sokoban/img/left.png')
right_img = pygame.image.load('./Sokoban/img/right.png')

man = [0, 0, 4]


def draw_text(screen, text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)


# Draw the map.
def draw_array(screen, array):
    image_size = 35

    for y, row in enumerate(array):
        for x, value in enumerate(row):

            screen.blit(block_img, (x * image_size, y * image_size))
            if value == 1:
                screen.blit(wall_img, (x * image_size, y * image_size))
            elif value == 2:
                screen.blit(ball_img, (x * image_size, y * image_size))
            elif value == 3 or value == 5:
                screen.blit(box_img, (x * image_size, y * image_size))
            elif value == 4 or value == 6:
                man[0] = x
                man[1] = y
                if man[2] == 4:
                    screen.blit(up_img, (x * image_size, y * image_size))
                elif man[2] == 5:
                    screen.blit(down_img, (x * image_size, y * image_size))
                elif man[2] == 6:
                    screen.blit(left_img, (x * image_size, y * image_size))
                elif man[2] == 7:
                    screen.blit(right_img, (x * image_size, y * image_size))


# Find and move the character.
def move(array, direction):
    x, y = man[0], man[1]

    if x is None or y is None:
        return

    dx, dy = 0, 0
    if direction == 'up':
        dy = -1
    elif direction == 'down':
        dy = 1
    elif direction == 'left':
        dx = -1
    elif direction == 'right':
        dx = 1

    new_x, new_y = x + dx, y + dy

    if 0 <= new_x < len(array[0]) and 0 <= new_y < len(array):
        next_cell = array[new_y][new_x]
        next_next_cell = array[new_y + dy][new_x + dx]

        if next_cell == 3 or next_cell == 5:
            if next_next_cell == 0 or next_next_cell == 2:
                array[new_y + dy][new_x + dx] += 3
                array[new_y][new_x] -= 3
                array[new_y][new_x] += 4
                array[y][x] -= 4
                man[0] = new_x
                man[1] = new_y
        elif next_cell == 0 or next_cell == 2:
            array[new_y][new_x] += 4
            array[y][x] -= 4
            man[0] = new_x
            man[1] = new_y


# Determine whether the game is over.
def is_game_over(array):
    for row in array:
        if 2 in row or 6 in row:
            return False

    return True


# When the gamee is over, give the prompt and go to next level.
def over_and_next(screen):
    message = "You Win! Press Space Key To Next Level!"

    font = pygame.font.Font(None, 36)

    text = font.render(message, True, (255, 255, 255))

    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    screen.blit(text, text_rect)

    pygame.display.flip()


# Game's main function.
def sokoban():
    levels = [
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 3, 3, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 3, 3, 3, 1, 1, 1, 1, 3, 0, 1, 0, 0],
         [0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
         [1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 3, 3, 0, 1],
         [1, 0, 2, 1, 1, 0, 1, 0, 0, 0, 1, 0, 3, 0, 0, 1],
         [1, 0, 2, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
         [1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
         [1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 3, 3, 3, 0, 1],
         [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 3, 0, 3, 0, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 3, 0, 3, 0, 1],
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 3, 0, 1],
         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    ]

    index = 0

    array = copy.deepcopy(levels[index])

    win = False

    pygame.init()

    screen_width = 560
    screen_height = 560
    font = pygame.font.Font(None, 24)
    current_text = "Current Level: " + str(index + 1)
    text_surface = font.render(current_text, True, (255, 255, 255))
    text_width, text_height = text_surface.get_size()
    screen = pygame.display.set_mode((screen_width, screen_height))

    draw_array(screen, array)
    draw_text(screen, "Press R - Retry", (10, 10), font)
    draw_text(screen, current_text, (screen_width - text_width - 10, 10), font)
    draw_text(screen, "Press Esc - Quit", (10, 530), font)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    man[2] = 4
                    move(array, 'up')
                elif event.key == pygame.K_DOWN:
                    man[2] = 5
                    move(array, 'down')
                elif event.key == pygame.K_LEFT:
                    man[2] = 6
                    move(array, 'left')
                elif event.key == pygame.K_RIGHT:
                    man[2] = 7
                    move(array, 'right')
                elif event.key == pygame.K_SPACE:
                    if win:
                        index += 1
                        array = copy.deepcopy(levels[index])
                        current_text = "Current Level: " + str(index + 1)
                        win = False
                elif event.key == pygame.K_r:
                    array = copy.deepcopy(levels[index])

                draw_array(screen, array)
                draw_text(screen, current_text, (screen_width - text_width - 10, 10), font)
                draw_text(screen, "Press R - Retry", (10, 10), font)
                pygame.display.flip()

                if is_game_over(array):
                    win = True
                    over_and_next(screen)


if __name__ == '__main__':
    sokoban()
    pygame.quit()
