from turtle import Turtle

STARTING_POSITION=[(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
#                                        make snake body 

    def create_snake(self):
        for position in STARTING_POSITION:
            self.Add_segment(position)



#      when score increase sname increase

    def Add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.Add_segment(self.segment[-1].position())

    
#                                           move the snake 
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            x=self.segment[seg_num-1].xcor()
            y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(x,y)
        self.segment[0].forward(MOVE_DISTANCE)

    def Up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)


        