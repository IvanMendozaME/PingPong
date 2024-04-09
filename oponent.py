from turtle import Turtle
import random
class Oponent(Turtle):
    def __init__(self,location) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.create_oponent(location)
    def create_oponent(self,location):
        self.goto(location)
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)