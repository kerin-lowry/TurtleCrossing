import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create player, car manager and scoreboard object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#listen for keypress, move the player up
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    #update the screen
    time.sleep(0.1)
    screen.update()
    
    #create cars
    car_manager.create_car()
    #move the car across the screen
    car_manager.move()
    
    #detect collison with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #detect if turtle has reached the finish line
    if player.ycor() == 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()