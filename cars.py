import threading
from turtle import Turtle
from random import randint, choice, randrange

MOVE_DISTANCE = 20


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

x_generator = randint(0, 1)


class Cars:
    def __init__(self):
        self.cars_top_bottom = []
        self.cars_middle = []

    def create_cars(self, row):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.speed(3)

        # right to left bottom
        if row == 1:
            random_y_coord = randrange(-225, -75, 75)
            new_car.goto(300, random_y_coord)
            self.cars_top_bottom.append(new_car)

        # left to right middle
        if row == 2:
            random_y_coord = randrange(-50, 100, 75)
            new_car.goto(-300, random_y_coord)
            self.cars_middle.append(new_car)

        # right to left top
        if row == 3:
            random_y_coord = randrange(100, 275, 75)
            new_car.goto(300, random_y_coord)
            self.cars_top_bottom.append(new_car)

        # randomise car starting location
        # random_x_coord = 0

        # if x_generator == 0:
        #     random_x_coord = -300
        # else:
        #     random_x_coord = 300

    def move_cars(self):
        for car in self.cars_top_bottom:
            car.backward(MOVE_DISTANCE)
            if car.xcor() >= 300:
                self.cars_top_bottom.remove(car)
        for car in self.cars_middle:
            car.forward(MOVE_DISTANCE)
            if car.xcor() <= -300:
                self.cars_middle.remove(car)

            # if car.xcor() == -300:
            #     # car.setheading(0)
            #     car.forward(MOVE_DISTANCE)
            # if car.xcor() == 300:
            #     # car.setheading(180)
            #     car.backward(MOVE_DISTANCE)
