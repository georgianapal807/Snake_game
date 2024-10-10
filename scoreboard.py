from turtle import Turtle
from snake import Snake
from food import Food

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)