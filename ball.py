from turtle import Turtle
import random




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.goto(0,0)
        random_plus_min_x=[+4,-4]
        random_plus_min_y=[-3,-1,+1,+3]

        random_horizontal=random.choice(random_plus_min_x)
        random_vertical= random.choice(random_plus_min_y)

        self.x_move=random_horizontal
        self.y_move=random_vertical
        self.move_speed=0.02


    def move(self):
        new_x=self.xcor()+ self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *= -1



    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.95
        print(self.move_speed)


    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.02
        self.bounce_x()

    def game_over(self):
        self.goto(0,0)











