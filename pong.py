import turtle

screen = turtle.Screen()
screen.title('Pong game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

class Paddle:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    
    def model(self):
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape('square')
        paddle.color('white')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(self.position_x, self.position_y)

class Ball:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    def model(self):   
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape('circle')
        ball.color('white')
        ball.penup()
        ball.goto(self.position_x, self.position_y)

#paddle a

paddle_a = Paddle(-350,0)
paddle_a.model()

#paddle b
paddle_b = Paddle(350, 0)
paddle_b.model()

#ball
ball = Ball(0,0)
ball.model()

#main loop
while True:
    screen.update()