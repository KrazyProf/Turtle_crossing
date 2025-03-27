from turtle import Screen
from car import Car
from player import Player
from score import Score
import time

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create instance of Car class (singular)
car_manager = Car()

# Creating player 
player = Player()

#Creating score
score = Score()

# Listening to key input
screen.onkey(key='Up' , fun=player.move)
spawn_condition = 0

is_over = False
while not is_over:
    screen.update()
    time.sleep(player.move_speed)
    
    # Access the cars list from the car_manager instance
    if spawn_condition > 5 :
        car_manager.spawn_cars()
        spawn_condition = 0
    
    # Detecting collision
    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over()
            is_over = True
            break
        

    # checking if player passed the level
    if player.ycor() > 290:
        score.update_level()
        player.player_reset()


    car_manager.move_car()
    spawn_condition += 1 
screen.exitonclick()