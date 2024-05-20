import pygame as pg
import random
import config


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.x = config.DIS_WIDTH / 2
        self.y = config.DIS_HEIGHT / 2
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length = 1

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def draw(self):
        for segment in self.snake_list:
            pg.draw.rect(self.screen, (config.PURPLE),[segment[0], segment[1], config.TILE_SIZE, config.TILE_SIZE])

    def update(self):
        self.move()
        self.snake_list.append([self.x, self.y])
        if len(self.snake_list) > self.length:
            del self.snake_list[0]


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, config.DIS_WIDTH - config.TILE_SIZE) / config.TILE_SIZE) * config.TILE_SIZE
        self.y = round(random.randrange(0, config.DIS_HEIGHT - config.TILE_SIZE) / config.TILE_SIZE) * config.TILE_SIZE

    def draw(self):
        pg.draw.rect(self.screen, (config.RED), [self.x, self.y, config.TILE_SIZE, config.TILE_SIZE])
