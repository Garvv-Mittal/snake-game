from turtle import Screen
from snake import snake
from Food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0) # turns off the animation of turtles one by one
screen.title("Snake Game")
  
snake = snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() # updates the screen with animation after tracer stopped it.
    # So screen.update when outside the for loop will update the screen when all the segments have moved.    
    time.sleep(0.1) #Delays the time by 0.1 second
    snake.move()
        
    # Dectect Collision
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Dectection collsion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
 
screen.exitonclick()