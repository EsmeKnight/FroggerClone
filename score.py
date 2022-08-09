from turtle import Turtle

FONT = "courier"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.pencolor("black")
        self.score = 0
        self.write_score()

    def add(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def gameover(self):
        self.goto(0, 100)
        self.write(f"You lose", align="center", font=FONT)
