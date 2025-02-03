import pygame


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.segments = [[300, 300], [285, 300], [270, 300]]
        self.direction = pygame.K_RIGHT
        original_snake_image = pygame.image.load('./Snake/snake_texture.png')
        self.snake_image = pygame.transform.scale(original_snake_image, (20, 20))

    def draw(self):
        for pos in self.segments:
            self.screen.blit(self.snake_image, pos)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i] = self.segments[i - 1].copy()

        if self.direction == pygame.K_UP:
            self.segments[0][1] -= 20
        elif self.direction == pygame.K_DOWN:
            self.segments[0][1] += 20
        elif self.direction == pygame.K_LEFT:
            self.segments[0][0] -= 20
        elif self.direction == pygame.K_RIGHT:
            self.segments[0][0] += 20

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = key
        elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = key
        elif key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = key
        elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = key

    def eat(self, food):
        if self.segments[0] == food.position:
            return True
        return False

    def extend(self):
        tail = self.segments[-1].copy()
        self.segments.append(tail)

    def is_collision(self, width, height):

        if (self.segments[0][0] >= width or self.segments[0][0] < 0 or
                self.segments[0][1] >= height or self.segments[0][1] < 0):
            return True

        for segment in self.segments[1:]:
            if segment == self.segments[0]:
                return True
        return False
