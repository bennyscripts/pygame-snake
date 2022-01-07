import pygame

class Snake:
    def __init__(self, screen, background_color, x, y, width, height, color):
        self.screen = screen
        self.background_color = background_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.body = [[self.x, self.y]]
        self.direction = "right"
        self.score = 0
        self.game_over = False

    def draw(self):
        for i in range(len(self.body)):
            pygame.draw.rect(self.screen, self.color, (self.body[i][0], self.body[i][1], self.width, self.height))

    def move(self):
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "up":
            self.y -= 10
        elif self.direction == "down":
            self.y += 10

        self.body.insert(0, [self.x, self.y])
        self.body.remove(self.body[len(self.body) - 1])

    def change_direction(self, direction):
        self.direction = direction

    def check_collision(self):
        if self.x < 0 or self.x > self.screen.get_width() - self.width:
            self.game_over = True
        if self.y < 0 or self.y > self.screen.get_height() - self.height:
            self.game_over = True

    def check_collision_with_food(self, food):
        if self.x == food.x and self.y == food.y:
            self.score += 1
            self.body.append([self.x, self.y])
            return True
        return False

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.body = [[self.x, self.y]]
        self.direction = "right"
        self.score = 0
        self.game_over = False