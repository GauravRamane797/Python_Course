from snake import Snake
from turtle import Screen
import time


snake = Snake()
sc = Screen()
sc.setup(width=400, height=400)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  sc.update()
  snake.move()
  time.sleep(1)




sc.exitonclick()

