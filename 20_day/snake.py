from turtle import Turtle

starting_pos = [(0, 0), (-10, 0), (-30, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_snake_block(pos)

    def add_snake_block(self, pos):
        self.snake_block = Turtle('circle')
        self.snake_block.color('red')
        self.snake_block.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake_block.penup()
        self.snake_block.goto(pos)
        self.snake_blocks.append(self.snake_block)

    def extend_snake(self):
        self.add_snake_block(self.snake_blocks[-1].position())


    def move_snake(self):
        for block_index in range(len(self.snake_blocks) - 1, 0, -1):
            x_cor = self.snake_blocks[block_index - 1].xcor()
            y_cor = self.snake_blocks[block_index - 1].ycor()
            self.snake_blocks[block_index].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)