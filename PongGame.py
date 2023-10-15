'''Creating Pong Game Using Turtle Module'''

import turtle
import time
`
'''Scres for Both Players Initially 0'''

score_a=0
score_b=0
`
'''It Creates a Screen and appears for liitle seconds'''
window_screen=turtle.Screen()
'''To set the width and height of the above created window_screen'''
window_screen.setup(800,600)#800-->Width of screen,600 refers to height of screen(in pixels)
# '''To Set the Background Image of Screen'''Not working-->Need to refer
# window_screen.bgpic("Dhoni3.jpg")
'''To Set the Background Color of Screen'''
window_screen.bgcolor("green")
'''To Set the Title of the Window'''
window_screen.title("Pong Game")
'''(Here,Paddle)Things you are creating and move it to the place you want.If you not give tracer(0),then it'll
give you the tracing of that thing(Here,Paddle).Like moving from origin to the place you moved'''
window_screen.tracer(0)

'''Creating Paddles'''
#Left Paddle
'''Creating a left paddle as Turtle Object'''
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-385,0)

# right Paddle
'''Creating a right paddle as Turtle Object'''
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)

'''Creating a Ball'''
'''Creating Ball as Turtle Object'''
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.dx=0.15 #Rate of change in X direction .Ball by default need to move without any keypress.
ball.dy=0.15 #Rate of change in Y direction

'''Moving Paddles Up and Down Using listen() and onKeyPress()'''

'''Functions fo move left and right paddles up and down'''
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)#settting y coordinate to move 20 pixels up
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)#settting y coordinate to move 20 pixels down
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)#settting y coordinate to move 20 pixels up
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)#settting y coordinate to move 20 pixels down

window_screen.listen()#It will listen to the keyboard keys we are pressing
'''Syntax:Do make Action on key press:window_screen.onkeypress(function,Keys)'''
'''For left Paddles-->'W'-->Move Up and --->'S'--->Move Down '''
window_screen.onkeypress(left_paddle_up,'W') #(also if you want 'W'.lower()
window_screen.onkeypress(left_paddle_down,'S')
'''For Right Paddles-->'Up'-->Move Up and --->'Down'--->Move Down '''
window_screen.onkeypress(right_paddle_up,'Up')
window_screen.onkeypress(right_paddle_down,'Down')


'''Writing Scores On TOP of Screen By Creating new Thing (Pen) as Turtle Object'''
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("PLAYER A:0   PLAYER B:0",align="center",font=("Arial",24,"normal"))


'''To keep the screen appear continuously You need to update it infinitely.So Giving While as True:'''
while True:
    window_screen.update()
    '''As balls are going to move by default without any keypress.So,give it in While Loop'''
    '''Ball Movement'''
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    '''Ball-Wall Collision-->When Collides the border it should return back.'''
    #Top Wall
    if ball.ycor()>290:
        ball.sety(290)#Even,it's not given,it will work.When your system is slow,it checks if condition and
        ball.dy*=-1   # and then make the ball movement return take time,so inside again set value is 290.
    #Bottom Wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    #Right Wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("PLAYER A:{}   PLAYER B:{}".format(score_a,score_b),align="center",font=("Arial",24,"normal"))
        if score_a == 5:
            pen.goto(0,0)
            pen.penup()
            pen.speed(0)
            pen.write("GAME OVER\n PLAYER A is WINNER",align="center",font=("Arial",24,"normal"))
            time.sleep(5)
            break

    #Left Wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        pen.write("PLAYER A:{}   PLAYER B:{}".format(score_a, score_b),align="center",font=("Arial",24,"normal"))
        if score_b == 5:
            pen.goto(0,0)
            pen.penup()
            pen.speed(0)
            pen.write("GAME OVER\n PLAYER B is WINNER", align="center", font=("Arial", 24, "normal"))
            time.sleep(5)
            break
    '''Ball Collides with the paddle'''
    if ball.xcor()>370 and right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50:
        ball.setx(370)
        ball.dx*=-1
    if ball.xcor()<-370 and left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50:
        ball.setx(-370)
        ball.dx*=-1

