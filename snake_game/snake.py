from turtle import Turtle

STARTING_COORDINATES = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for coordinates in STARTING_COORDINATES:
            self.create_block(coordinates)

    def create_block(self, coordinates):
        block = Turtle(shape="square")
        block.color("white")
        block.penup()
        self.snake_blocks.append(block)
        block.goto(coordinates)

    def add_block(self):
        self.create_block(self.snake_blocks[-1].position())

    def move_snake(self):
        for block in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[block - 1].xcor()
            new_y = self.snake_blocks[block - 1].ycor()
            self.snake_blocks[block].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

