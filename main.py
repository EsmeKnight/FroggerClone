from turtle import Screen
from score import Score
from frog import Frog
from cars import Cars
import time
import schedule

STARTING_POSTION = (0, -275)

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtler")
screen.tracer(0)
screen.listen()

# create frog instance
frog = Frog()
frog.goto(STARTING_POSTION)

# create score instance
score = Score()

# establish controls
screen.onkey(frog.upwards, "Up")
screen.onkey(frog.back, "Down")
screen.onkey(frog.left, "Left")
screen.onkey(frog.right, "Right")


# update screen so player doesnt see turtle move to beginning position
screen.update()
time.sleep(0.1)

# create cars instance
cars = Cars()


# function for managable car generation with schedule
def car_gen():
    for i in range(1, 4):
        cars.create_cars(i)


schedule.every(0.5).seconds.do(car_gen)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    schedule.run_pending()

    cars.move_cars()

    # establish screen boundaries and point conditions
    if frog.ycor() >= 275:
        frog.goto(STARTING_POSTION)
        score.add()

    # establsih game over
    for car in cars.cars_top_bottom:
        if car.distance(frog) < 10:
            score.gameover()
            game_is_on = False
    for car in cars.cars_middle:
        if car.distance(frog) < 10:
            score.gameover()
            game_is_on = False


screen.exitonclick()
