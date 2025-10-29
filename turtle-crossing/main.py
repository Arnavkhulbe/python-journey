import turtle
import random
import time
t1=turtle.Turtle()
t1.hideturtle()
t1.penup()
t1.shape('turtle')
t1.goto(0,-290)
t1.setheading(90)
t1.showturtle()
s=turtle.Screen()
s.listen()
def up():
    t1.forward(20)
def down():
    t1.forward(-20)
s.onkey(up,'Up')
s.onkey(down,'Down')
cars=[]
color = ["yellow", "red", "blue", "black", "brown", "orange",
         "green", "pink", "purple", "cyan", "magenta", "gold",
         "silver", "violet", "indigo", "lime", "turquoise", "navy"]


lanes = [-250,-230, -200,-170, -150,-130, -100,-80, -50,-30, 0,30, 50,80, 100,130, 150,170, 200,230, 250]
score = 1
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-310, 280)  # top-left corner
score_turtle.write(f" Level: {score}", align="left",font=("Arial", 16, "bold"))
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Level: {score}", align="left", font=("Arial", 16, "bold"))
def createcar():
    t2 = turtle.Turtle()
    t2.hideturtle()
    t2.shape('square')
    t2.shapesize(stretch_len=3, stretch_wid=1)
    t2.penup()
    t2.goto(330, random.choice(lanes))
    t2.setheading(180)
    t2.color(random.choice(color))
    t2.showturtle()
    return t2
x1 = 10
def movecar():

    for car in cars:
        x = car.xcor()
        y = car.ycor()
        car.goto(x - x1, y)


case1=True
s.tracer(0)
while case1:
    time.sleep(0.1)


    if random.randint(1,4)==1:
        cars.append(createcar())
    movecar()
    for car in cars:
        distance=t1.distance(car)
        if distance<20:
            score_turtle.goto(0,0)
            score_turtle.write(f"You Lose", align="center", font=("Arial", 20, "bold"))

            case1=False
        if t1.ycor()>315:
            print("you win")
            t1.hideturtle()
            t1.goto(0,-290)
            t1.showturtle()
            x1+=5
            time.sleep(0.5)
            score+=1
            update_score()
        for car in cars[:]:  # iterate over a copy
            if car.xcor() < -350:
                car.hideturtle()
                cars.remove(car)
        s.update()

s.exitonclick()
