from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.title("Paddle Game")
screen.bgcolor("black")
screen.setup(width = 800, height= 600)
screen.tracer(0)

score = ScoreBoard()

l_paddle = Paddle(-350, 0, "w", "s")
r_paddle = Paddle(350, 0, "Up", "Down")
ball = Ball()
   
    
screen.listen()
screen.onkeypress(l_paddle.go_up, l_paddle.up_key)
screen.onkeypress(l_paddle.go_down, l_paddle.down_key)
screen.onkeypress(r_paddle.go_up, r_paddle.up_key)
screen.onkeypress(r_paddle.go_down, r_paddle.down_key)





is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Wall collision
    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.ball_bounce_y()

    # Right paddle collision
    if ball.distance(r_paddle) < 45 and ball.x_cor > 0:
        ball.ball_bounce_x()

    # Left paddle collision
    if ball.distance(l_paddle) < 45 and ball.x_cor < 0:
        ball.ball_bounce_x()

    # Right player misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.left_point()

    # Left player misses
    if ball.xcor() < -380:
        ball.reset_ball()
        score.right_point()
        





















screen.exitonclick()