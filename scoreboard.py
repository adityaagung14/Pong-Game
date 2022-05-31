from turtle import Turtle, Screen

LEFT_ALIGNMENT = "left"
RIGHT_ALIGNMENT = "right"
CENTER_ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, color, score_position):
        super().__init__()
        self.score = 0
        self.color(color)
        self.penup()
        self.pos=score_position
        self.goto(self.pos)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(self.pos)
        self.write(f"{self.score}", align=CENTER_ALIGNMENT, font=("Courier", 40, "normal"))

    def title(self, team_name,position):
        self.name=team_name
        self.position=position
        self.goto(self.position)
        self.write(f"{self.name}", align=LEFT_ALIGNMENT, font=("Arial", 15, "normal"))


    def game_over(self,winner_team):
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.write(f"   GAME OVER \n {winner_team} Wins", align=CENTER_ALIGNMENT,font=("Arial", 30, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.title(self.name,self.position)
