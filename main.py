from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import random
import time
from scoreboard import Score

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


middle_line=Turtle()
middle_line.color("white")
middle_line.shape("classic")
middle_line.hideturtle()


middle_line.setx(0)
middle_line.penup()
middle_line.sety(-300)
middle_line.setheading(90)


for dash_middle_line in range(30):
    middle_line.pendown()
    middle_line.forward(10)
    middle_line.penup()
    middle_line.forward(10)




r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
blue_score=Score("blue",(-100,200))
blue_score.title("Blue Team",(-150,180))
red_score=Score("red",(100,200))
red_score.title("Red Team",(60,180))




game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    screen.listen()
    screen.onkeypress(fun=r_paddle.go_up, key='Up')
    screen.onkeypress(fun=r_paddle.go_down, key='Down')
    screen.onkeypress(fun=l_paddle.go_up,key='w')
    screen.onkeypress(fun=l_paddle.go_down,key='s')


    # Detect collision with wall
    if ball.ycor()> 279 or ball.ycor()<-279:
        ball.bounce_y()

    #Detect collision with right paddle (r_paddle):
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor()>380:
        print("blue player scored")
        blue_score.add_score()
        ball.reset_ball()

    # Detect left paddle misses
    if ball.xcor()<-380:
        print("right player scored")
        red_score.add_score()
        ball.reset_ball()

    if red_score.score== 5:
        ball.game_over()
        red_score.game_over("Red Team")
        game_is_on= False

    elif blue_score.score==5:
        ball.game_over()
        blue_score.game_over("Blue Team")
        game_is_on= False







screen.exitonclick()