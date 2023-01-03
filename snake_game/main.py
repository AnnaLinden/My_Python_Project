import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
from snake import Snake

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Food colisions
    if snake.head.distance(food)<17:
        food.locate_food()
        snake.add_block()
        score.increase_score()

    if snake.head.xcor()<-290 or snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score.game_over()
        game_on = False

    for block in snake.snake_blocks[1:]:
        if snake.head.distance(block)<10:
            score.game_over()
            game_on = False




screen.exitonclick()