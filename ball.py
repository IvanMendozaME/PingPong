from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("slowest")
        self.goto(0,0)
        self.x_move=8
        self.y_move = 8
        self.move_speed = 0.04
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed *=0.9
    def refresh(self):
        self.move_speed = 0.04
        self.goto(0,0)
        self.x_move*=-1


