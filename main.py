from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect Collision With Turtle(Food)
    if snake.snake_head.distance(food) < 15:
        food.coordinate()
        scoreboard.get_point()
        scoreboard.update_score()
        snake.extend()
    
    #Detect Collision With Wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.snake_reset()
    
    #Detect Collision With Other Body
    for body in snake.snakes[1:]:
        if snake.snake_head.distance(body) < 10:
            scoreboard.reset()
















screen.exitonclick()