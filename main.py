from turtle import Screen
from oponent import Oponent
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

player2 = Oponent((350,0))
player1 = Oponent((-350,0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(player2.go_up,"Up")
screen.onkey(player2.go_down,"Down")

screen.onkey(player1.go_up,"W")
screen.onkey(player1.go_down,"S")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.xcor() > 380:
        ball.refresh()  
        score.r_update()
    if ball.xcor()<-390:
        ball.refresh()
        score.l_update()
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.bounce_x()     
        print("Hit")
    
screen.exitonclick()
