import pygame as pg
import random

class Snake:
    def __init__(self, game):
        self.game = game
        self.x = game.dis_width / 2
        self.y = game.dis_height / 2
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length = 1

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def draw(self):
        for segment in self.snake_list:
            pg.draw.rect(self.game.screen, (self.game.purple),[segment[0], segment[1], self.game.tile_size, self.game.tile_size])

    def update(self):
        self.move()
        self.snake_list.append([self.x, self.y])
        if len(self.snake_list) > self.length:
            del self.snake_list[0]

class Food:
    def __init__(self, game):
        self.game = game
        self.respawn()

    def respawn(self):
        self.x = round(random.randrange(0, self.game.dis_width - self.game.tile_size) / self.game.tile_size) * self.game.tile_size
        self.y = round(random.randrange(0, self.game.dis_height - self.game.tile_size) / self.game.tile_size) * self.game.tile_size
    def draw(self):
        pg.draw.rect(self.game.screen, (self.game.red), [self.x, self.y, self.game.tile_size, self.game.tile_size])
