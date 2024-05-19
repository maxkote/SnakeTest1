from game import Game
import pygame as pg

# configuration
DIS_WIDTH = 600
DIS_HEIGHT = 400
TILE_SIZE = 20
SNAKE_SPEED = 10
# colors
GREEN = (9, 232, 68)
PURPLE = (131, 41, 227)
RED = (214, 2, 2)
DARK_GREEN =(78, 168, 13)

pg.init()
game = Game(DIS_WIDTH, DIS_HEIGHT, TILE_SIZE, SNAKE_SPEED, GREEN, PURPLE, RED, DARK_GREEN)
game.run()
