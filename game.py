import pygame as pg
from game_objects import Snake, Food
import config


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(config.SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.init = pg.init()
        self.caption = pg.display.set_caption('Snake')
        self.font = pg.font.SysFont("arial", 45)
        self.running = True

        self.snake = Snake(self.screen)
        self.food = Food(self.screen)

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(config.SNAKE_SPEED)

    def draw(self):
        self.screen.fill((config.GREEN))
        self.snake.draw()
        self.food.draw()
        self.draw_score()
        self.draw_grid()
        pg.display.flip()

    def check_events(self):
        self.check_input_events()
        self.check_collision()
        self.check_food_collision()

    def draw_score(self):
        score_text = self.font.render(f"{self.snake.length - 1}", True, (255, 255, 255))
        self.screen.blit(score_text, [20.5, 14.5])

    def draw_grid(self):
        for x in range(0, config.DIS_WIDTH, config.TILE_SIZE):
            pg.draw.line(self.screen, config.DARK_GREEN, (x, 0), (x, config.DIS_HEIGHT))
        for y in range(0, config.DIS_HEIGHT, config.TILE_SIZE):
            pg.draw.line(self.screen, config.DARK_GREEN, (0, y), (config.DIS_WIDTH, y))

    def check_collision(self):
        if self.snake.x >= config.DIS_WIDTH or self.snake.x < 0 or self.snake.y >= config.DIS_HEIGHT or self.snake.y < 0:
            self.running = False

        for segment in self.snake.snake_list[:-1]:
            if segment == [self.snake.x, self.snake.y]:
                self.running = False

    def check_food_collision(self):
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.food.respawn()
            self.snake.length += 1

    def check_input_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.running = False
                if (event.key == pg.K_LEFT or event.key == pg.K_a) and self.snake.x_change == 0:
                    self.snake.x_change = -config.TILE_SIZE
                    self.snake.y_change = 0
                elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and self.snake.x_change == 0:
                    self.snake.x_change = config.TILE_SIZE
                    self.snake.y_change = 0
                elif (event.key == pg.K_UP or event.key == pg.K_w)and self.snake.y_change == 0:
                    self.snake.y_change = -config.TILE_SIZE
                    self.snake.x_change = 0
                elif (event.key == pg.K_DOWN or event.key == pg.K_s) and self.snake.y_change == 0:
                    self.snake.y_change = config.TILE_SIZE
                    self.snake.x_change = 0

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()

        pg.quit()
        quit()

