import turtle

screen = turtle.Screen()
screen.title('Pong game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

class Base:
    def __init__(self, position_x, position_y, shape):
        self.position_x = position_x
        self.position_y = position_y
        self.shape = shape
        self.vector = turtle.Turtle()
    
    def model(self):
        self.vector.speed(0)
        self.vector.shape(self.shape)
        self.vector.color('white')
        self.vector.penup()
        self.vector.goto(self.position_x, self.position_y)

    


class Paddle(Base):
    def __init__(self, position_x, position_y, shape):
        super().__init__(position_x, position_y, shape)
        self.position_x = position_x
        self.position_y = position_y
        self.shape = shape
        self.paddle = turtle.Turtle()

    def model(self):
        super().model()
        self.vector.shapesize(stretch_wid=5, stretch_len=1)


paddle_a = Paddle(-350,0,'square')
def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)
paddle_a.model()
screen.listen()
screen.onkeypress(paddle_a_up,'w')


#paddle b
paddle_b = Paddle(350, 0,'square')
paddle_b.model()


#ball
ball = Base(0,0,'circle')
ball.model()
print(paddle_a.position_x)

#main loop
while True:
    screen.update()
    
   