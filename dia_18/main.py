from  turtle import Turtle, Screen

def turtle_right():
    tim.forward(100)
    tim.right(90)

def turtle_square():
    for _ in range(4):
        turtle_right()

def dashed_line(up, down):
    tim.forward(up)
    tim.penup() # alza el boligrafo para no dibujar
    tim.forward(down)
    tim.pendown() # baja el boligrafo para dibujar


tim = Turtle()

tim.shape("turtle")
tim.color("green")

""" Dibuja un cuadrado """
#turtle_square()

""" Dibuja una linea segmentada """
for _ in range(30):
    dashed_line(10,10)

































screen = Screen()
screen.exitonclick()