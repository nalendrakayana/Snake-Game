from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.snake_head = self.snakes[0]
        
    def create_snake(self):    
        for coordinate in COORDINATES:
            self.add_body(coordinate)
            
    def add_body(self, coordinate):
        body = Turtle("square")
        body.penup()
        body.color("white")
        body.goto(coordinate)
        self.snakes.append(body)

    def extend(self):
        self.add_body(self.snakes[-1].position())
    
    def move(self):
        for snake in range (len(self.snakes) - 1, 0, -1):
            new_xcor = self.snakes[snake - 1].xcor()
            new_ycor = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_xcor, new_ycor)
        self.snake_head.forward(DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)