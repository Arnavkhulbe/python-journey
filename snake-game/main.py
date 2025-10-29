import time
import turtle
import random
s=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
t1.goto(0,0)


t5.penup()
t6.penup()
t5.goto(-90,280)
t4.shape("circle")
t4.color("red")
t5.hideturtle()
t6.hideturtle()

t4.penup()
x=random.randint(-280,280)
y=random.randint(-280,280)
t4.goto(x,y)
t=[]
def setup():
    t1.goto(0, 0)
    t2.goto(-20, 0)
    t3.goto(-40, 0)
    t = [t1, t2, t3]
    for seg in t:
        seg.showturtle()
        seg.shape("square")
        seg.color("grey")
        seg.penup()
        seg.speed(0)
    return t

tt = setup()


tt=setup()


score=0
case=True
def up():
    t1.setheading(90)
def left():
    t1.setheading(180)
def right():
    t1.setheading(0)
def down():
    t1.setheading(270)
s.listen()
s.onkey(up, "Up")
s.onkey(down, "Down")
s.onkey(left, "Left")
s.onkey(right, "Right")
s.tracer(0)
while case:
    t6.clear()
    with open("data.txt","r") as f:
        high=int(f.read())
    t5.clear()
    t5.goto(95, 280)
    t5.write(f"High Score: {high}", align="center", font=("Courier", 14, "bold"))
    t6.goto(x=-90,y=280)
    t6.write(f"Score: {score}", align="center", font=("Courier", 16, "bold"))

    def move():


        for i in range(len(tt)-1,0,-1):
            tt[i].goto(tt[i-1].position())
        tt[0].forward(10)
    move()
    for segment in tt[1:]:
        if t1.distance(segment) < 10:
            if score > high:
                high = score
                with open("data.txt","w") as f:
                    f.write(f"{high}")
            # Hide all segments
            for seg in tt:
                seg.goto(1000,1000)
            score = 0
            time.sleep(0.5)
            tt = setup()
            break
    s.update()
    time.sleep(0.10)
    if t1.distance(t4) <= 20:
        new_segment = turtle.Turtle()  # naya segment
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        tt.append(new_segment)
        t4.goto(x=random.randint(-280,280),y=random.randint(-280,280))
        score+=10
        t6.clear()
        t6.goto(x=-90,y=280)
        t6.write(f"Score: {score}", align="center", font=("Courier", 15, "bold"))
    if t1.xcor() > 290 or t1.xcor() < -290 or t1.ycor() > 290 or t1.ycor() < -290:
        if score  > high:
            high = score
            with open("data.txt","w") as f:
                f.write(f"{high}")
            t6.clear()
        t5.clear()
        score=0
        time.sleep(0.1)

        tt=setup()
s.exitonclick()