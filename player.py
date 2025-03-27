from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0 , -280)
        self.move_speed = 0.1

    def move(self):
        self.fd(10)
    
    def player_reset(self):
        self.move_speed *= 0.8
        self.goto(0,-280)