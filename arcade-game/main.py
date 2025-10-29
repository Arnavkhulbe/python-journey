import turtle
import time
s= turtle.Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
t1=turtle.Turtle()
t1.shape("square")
t1.color("white")
t1.penup()
t1.goto(-380,0)
t1.shapesize(stretch_wid=3.5, stretch_len=1)
s.listen()
def left_up():
    y = t1.ycor()
    if y < 250:
        t1.sety(y + 20)

def left_down():
    y = t1.ycor()
    if y > -250:
        t1.sety(y - 20)
s.onkey(left_up, "w")
s.onkey(left_down, "s")

t2=turtle.Turtle()
t2.shape("square")
t2.color("white")
t2.penup()
t2.goto(380,0)
t2.shapesize(stretch_wid=3.5, stretch_len=1)



def right_up():
    y=t2.ycor()
    if y<250:
        t2.sety(y + 20)
def right_down():
    y=t2.ycor()
    if y>-250:
        t2.sety(y-20)
s.onkey(right_up, "Up")
s.onkey(right_down, "Down")
t3=turtle.Turtle()
t3.shape("circle")
t3.color("white")
t3.goto(0,0)
t3.penup()
case=True
x=15
y=15
sl = 0
sr = 0
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)  # Screen ke top center ke thoda niche
score_turtle.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Left: {sl}  Right: {sr}", align="center", font=("Courier", 24, "normal"))

s.tracer(0)
while case:
    time.sleep(0.1)


    xcor = t3.xcor()
    ycor = t3.ycor()
    if ycor > 290 or ycor < -290:
        y *= -1  # Y direction ulta karo

    t3.goto(xcor + x, ycor + y)
    #detect collision with left paddle
    if t3.distance(t1)<10  or (t3.xcor()<-360 and t3.distance(t1)<40):
        x *= -1
        sl+=1
        update_score()
    if t3.distance(t2)<10 or (t3.xcor()>360 and t3.distance(t2)<40):
        x *= -1
        sr+=1
        update_score()
    if t3.xcor()>400:
        sl+=1
        update_score()
        t3.goto(0,0)
        x*=-1

    if t3.xcor() < -400:
        sr+=1
        update_score()
        t3.goto(0, 0)
        x*=-1
    s.update()



    # Score update karne ke liye ek function banao


s.exitonclick()