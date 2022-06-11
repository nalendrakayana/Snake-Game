from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def get_point(self):
        self.score += 1
        self.update_score()