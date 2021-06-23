from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh()
    
    
    def refresh(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)
    
    
    def increase_score(self):
        self.score += 1
        self.refresh()
    
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)