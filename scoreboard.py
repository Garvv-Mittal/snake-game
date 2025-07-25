from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",22,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\\Coding\\Python\\Projects\\Snake Game\\data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}      high score: {self.highscore}", align= ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("D:\\Coding\\Python\\Projects\\Snake Game\\data.txt",mode="w") as data:
               int(data.write(f"{self.highscore}"))
        self.score = 0
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()