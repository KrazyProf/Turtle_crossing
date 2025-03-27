from turtle import Turtle, Screen
screen = Screen()


class Score(Turtle):

    LEVEL = 0
    def __init__(self):
        super().__init__()
        self.display()

    def display(self):
        self.hideturtle()
        self.penup()
        self.goto(-250 , 250)
        self.write(arg=f"Level: {self.LEVEL}" , align='left' , font=("Courier" , 12 , 'normal'))
    
    def update_level(self):
        self.LEVEL += 1
        self.clear()
        self.display()
