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
        with open("Frogger\DataFolder\data.txt", "r") as file:
            self.highscore = int(file.read())
        self.write_score()

    def add(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(
            f"Score: {self.score} Highscore: {self.highscore}", align="left", font=FONT
        )

    def gameover(self):
        self.goto(0, 100)
        self.write(f"You lose", align="center", font=FONT)
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Frogger\DataFolder\data.txt", "w") as file:
                file.write(f"{self.highscore}")
