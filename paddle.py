from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor, up_key, down_key):
        super() .__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.up_key = up_key
        self.down_key = down_key
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.goto(self.x_cor, self.y_cor)
        
    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.x_cor, new_y)
        
    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.x_cor, new_y)