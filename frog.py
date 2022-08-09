from turtle import Turtle, forward, Screen

MOVE_DISTANCE = 20


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("green")

    # direction will be 0, 90, 180, 270 (r, f, l, b)
    def upwards(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def back(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
