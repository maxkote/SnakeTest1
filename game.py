import pygame as pg
from game_objects import Snake, Food

class Game:
    def __init__(self, dis_width, dis_height, tile_size, snake_speed, green, purple, red, dark_green):
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.screen = pg.display.set_mode((dis_width, dis_height))
        self.tile_size = tile_size
        self.snake_speed = snake_speed
        self.running = True
        self.clock = pg.time.Clock()

        self.snake = Snake(self)
        self.food = Food(self)

        self.green = green
        self.purple = purple
        self.red = red
        self.dark_green = dark_green

        self.font = pg.font.SysFont("arial", 45)

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(self.snake_speed)

    def draw(self):
        self.screen.fill((self.green))
        self.snake.draw()
        self.food.draw()
        self.draw_score()
        self.draw_grid()
        pg.display.flip()

    def draw_score(self):
        score_text = self.font.render(f"{self.snake.length - 1}", True, (255, 255, 255))
        self.screen.blit(score_text, [20, 15])

    def draw_grid(self):
        grid_color = (dark_green)  # Dark green color
        for x in range(0, self.dis_width, self.tile_size):
            pg.draw.line(self.screen, grid_color, (x, 0), (x, self.dis_height))
        for y in range(0, self.dis_height, self.tile_size):
            pg.draw.line(self.screen, grid_color, (0, y), (self.dis_width, y))
    def check_collision(self):
        if self.snake.x >= self.dis_width or self.snake.x < 0 or self.snake.y >= self.dis_height or self.snake.y < 0:
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
                if event.key == pg.K_LEFT and self.snake.x_change == 0:
                    self.snake.x_change = -self.tile_size
                    self.snake.y_change = 0
                elif event.key == pg.K_RIGHT and self.snake.x_change == 0:
                    self.snake.x_change = self.tile_size
                    self.snake.y_change = 0
                elif event.key == pg.K_UP and self.snake.y_change == 0:
                    self.snake.y_change = -self.tile_size
                    self.snake.x_change = 0
                elif event.key == pg.K_DOWN and self.snake.y_change == 0:
                    self.snake.y_change = self.tile_size
                    self.snake.x_change = 0

    def run(self):

        pg.display.set_caption('Snake')
        while self.running:

            self.check_input_events()
            self.check_collision()
            self.check_food_collision()

            self.update()
            self.draw()

        pg.quit()
        quit()

