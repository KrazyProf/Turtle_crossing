from turtle import Screen
from car import Car
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create instance of Car class (singular)
car_manager = Car()

# Creating player 
player = Player()

# Listening to key input
screen.onkey(key='Up' , fun=player.move)

spawn_condition = 0
while True:
    screen.update()
    time.sleep(0.1)
    
    # Access the cars list from the car_manager instance
    if spawn_condition > 5 :
        car_manager.spawn_cars()
        spawn_condition = 0
    
    # checking if player passed the level


    car_manager.move_car()
    spawn_condition += 1 
screen.exitonclick()