from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():    
    tim.forward(50)

def move_backwards():
    tim.backward(50)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()    
    tim.home()
    tim.pendown()    

screen.listen()
screen.onkey(move_forwards, key = "w")
screen.onkey(move_backwards, key = "s")
screen.onkey(turn_left, key = "a")
screen.onkey(turn_right, key = "d")
screen.onkey(clear, key = "c")
screen.exitonclick()