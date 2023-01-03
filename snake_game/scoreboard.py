from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-20, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(-20, 0)
        self.pendown()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)