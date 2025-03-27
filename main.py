from turtle import Screen
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = Car()

screen.update()






screen.exitonclick()