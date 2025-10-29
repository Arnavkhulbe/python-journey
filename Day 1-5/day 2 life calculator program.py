#note if you use / it give result in float but if use // gives result in int
print(round(8/3,2))#rounds off upto 2 digit



result=4/2
result /=2
print(result)


score=0
print("your score is " + str(score))

#or you can do this by f-string
score=1
print(f"your score is {score}")


#excercise to calculate weeks ,days and months until you turn 90
#remember that there are 365 days 52 weeks and 12 months in a year
age=int(input("enter your age"))
weeksspend=52*age
daysspend=365*age
monthsspend=12*age
weeksleft=(90*52)-weeksspend
daysleft=(90*365)-daysspend
monthsleft=(90*12)-monthsspend
print(f"you have {weeksleft} weeks left, {daysleft} days left and {monthsleft} months left")
#note in this you are getting answer in int because only while dividing two int you get flaot 
