weight=int(input("enter your weight in kg"))
height=float(input("enter you height in m"))
bm=weight/(height*height)
bmi=round(bm,1)
print(f"your bmi is {bmi}")
if bmi<=18.5:
    print("you are underweight")
elif bmi<=25:
    print("you come under normal weight")
elif bmi<=30:
    print(" you are in overweight")
elif bmi<=35:
    print("you are obese")
else:
    print("clinicallly obese")

