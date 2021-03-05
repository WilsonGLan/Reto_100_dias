from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400) #Damos dimensionamiento a la ventana principal
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
colors = ["green", "blue", "red", "yellow", "orange", "purple"]
position_y = [-100, -60, -20, 20, 60, 100]

for index_turtle in range(6):
    raphael = Turtle(shape="turtle")    
    raphael.color(colors[index_turtle])
    raphael.penup()
    raphael.goto(x= -220, y=position_y[index_turtle])

screen.listen()

screen.exitonclick()