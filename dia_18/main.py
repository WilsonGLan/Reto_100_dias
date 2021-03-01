from  turtle import Turtle, Screen

def turtle_right():
    tim.forward(100)
    tim.right(90)

def turtle_square():
    for _ in range(4):
        turtle_right()


tim = Turtle()

tim.shape("turtle")
tim.color("green")

turtle_square()



































screen = Screen()
screen.exitonclick()