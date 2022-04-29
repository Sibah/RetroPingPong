from turtle import Turtle
import time

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.currentScore = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)


    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER 🙄\nRestart with r", move=False, align="center", font=("Arial", 24, "bold"))

    def startCountdown(self, timer):
        self.clear()
        self.goto(0, 0)
        while timer >= 0:
            time.sleep(1)
            self.write(f"STARTING IN {timer}\nKeys: w   s   ↥   ↧", move=False, align="center", font=("Arial", 24, "bold"))
            timer -= 1
            self.clear()

    def clearscreen(self):
        self.clear()
