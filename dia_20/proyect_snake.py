from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup() # evita que deje la marca de linea al mover
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # en el range se simula el start, stop y step
    for seg_nums in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_nums - 1].xcor()
        new_y = segments[seg_nums - 1].ycor()
        segments[seg_nums].goto(new_x, new_y)
    segments[0].forward(20)




screen.exitonclick()