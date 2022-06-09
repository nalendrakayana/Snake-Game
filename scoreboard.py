from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
    
    def player_lose(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over!", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)