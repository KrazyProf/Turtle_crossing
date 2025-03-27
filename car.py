from turtle import Turtle
import random

class Car(Turtle):
    COLORS = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']  # Class variable
    
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the main turtle
        self.cars = []  # To store all car turtles
        self.make_cars()

    def make_cars(self):
        for _ in range(10):
            car = Turtle()
            car.shape('square')
            car.color(random.choice(self.COLORS))
            car.shapesize(stretch_len=4, stretch_wid=1)
            car.penup()
            car.goto(random.randint(-290, 290), random.randint(-200, 200))
            self.cars.append(car)  # Store the car
    
    def move_car(self):

        for car in self.cars:
            car.fd(-10)
    
    def spawn_cars(self):
        car = Turtle()
        car.shape('square')
        car.color(random.choice(self.COLORS))
        car.shapesize(stretch_len=4, stretch_wid=1)
        car.penup()
        car.goto(random.randint(310 , 320) , random.randint(-200 , 200))
        self.cars.append(car)

