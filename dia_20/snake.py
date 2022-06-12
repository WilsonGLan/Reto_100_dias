from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup() # evita que deje la marca de linea al mover
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # en el range se simula el start, stop y step
        for seg_nums in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_nums - 1].xcor()
            new_y = self.segments[seg_nums - 1].ycor()
            self.segments[seg_nums].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)