from turtle import Turtle

class Players:
    def __init__(self):
        self.segments = []
        self.positions1= [(-380, -20),(-380, 0),(-380, 20)]
        
        self.player1()
        self.head_up = self.segments[0]
        self.head_down = self.segments[2]

        
    
    def player1(self):
        for position in self.positions1:
            self.new_segment(position)

    
    def new_segment(self, position):
        new_segment = Turtle()
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def up(self):
        for segment in self.segments:
            segment.sety(segment.ycor() + 20)


    def down(self):
        for segment in self.segments:
            segment.sety(segment.ycor() - 20)