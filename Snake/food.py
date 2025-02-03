import pygame
import random


class Food:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        original_food_image = pygame.image.load('./Snake/food.png')
        self.food_image = pygame.transform.scale(original_food_image, (20, 20))
        self.refresh()

    def draw(self):
        self.screen.blit(self.food_image, self.position)

    def refresh(self):
        self.position = [random.randrange(1, (self.width // 20)) * 20,
                         random.randrange(1, (self.height // 20)) * 20]
