import pygame

class Apple:
    def __init__(self, screen, background_color, x, y, width, height, color):
        self.screen = screen
        self.background_color = background_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def delete(self):
        pygame.draw.rect(self.screen, self.background_color, (self.x, self.y, self.width, self.height))