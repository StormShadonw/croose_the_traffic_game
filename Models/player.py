from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def start(self):
        self.goto(STARTING_POSITION)
