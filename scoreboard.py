from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier",60,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier",60,"normal"))

    def r_update(self):
        self.r_score+=1
        self.clear()
        self.update_scoreboard()
    def l_update(self):
        self.l_score+=1
        self.clear()
        self.update_scoreboard()