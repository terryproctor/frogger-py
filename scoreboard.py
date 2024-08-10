from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        message = f"Level: {self.level}"
        self.write(message, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        self.update_high_score()
        self.level = 1

    def high_score(self):
        with open("high_score.txt") as file:
            
            try:
                h_score = int(file.read())
                if self.level > h_score:
                    with open("high_score.txt", mode="w") as file:
                        file.write(str(self.level))
            except:
                with open("high_score.txt", mode="w") as file:
                    file.write(str(self.level))
                    h_score = self.level
        return h_score
    
    def update_high_score(self):
        self.goto(0, 200)
        message = f"High Score: {self.high_score()}"
        self.write(message, align="center", font=FONT)
