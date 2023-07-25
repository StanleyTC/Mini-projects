from turtle import Turtle

class Snack:
    def __init__(self):    
    # Snack definitions
        self.starting_positions = [(0, 0),(-20, 0),(-40, 0)]
        self.segments = []
        for position in self.starting_positions:
            new_segment= Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)




    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)
