import time
from turtle import Screen
from Models.player import Player
from Models.car_manager import CarManager
from Models.scoreboard import Scoreboard
# from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreBoard = Scoreboard()

screen.listen()

screen.onkey(player.up, "Up")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.game_over()

        if player.finished():
            player.start()
            car_manager.level_up()
            scoreBoard.increase_level()

screen.exitonclick()
