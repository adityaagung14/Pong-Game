from turtle import Turtle


class Ball_Alt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def straight_left(self):
        new_x = self.xcor() - 3
        self.goto(new_x, self.ycor())

    def straight_right(self):
        new_x = self.xcor() + 3
        self.goto(new_x, self.ycor())

    def up_right(self):
        new_x = self.xcor() + 3
        new_y = self.ycor() + 3
        self.goto(new_x, new_y)

    def up_left(self):
        new_x = self.xcor() - 3
        new_y = self.ycor() + 3
        self.goto(new_x, new_y)

    def down_right(self):
        new_x = self.xcor() + 3
        new_y = self.ycor() - 3
        self.goto(new_x, new_y)

    def down_left(self):
        new_x = self.xcor() - 3
        new_y = self.ycor() - 3
        self.goto(new_x, new_y)
