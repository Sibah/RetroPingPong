from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.increase_score(0)

    def increase_score(self, point):
        self.score += point
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "bold"))
