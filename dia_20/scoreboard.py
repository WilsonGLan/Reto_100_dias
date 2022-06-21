from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup() #Para que no marque una linea de desplazamiento.
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align= "Center", font=("Arial", 24, "normal"))
        self.hideturtle()
        