print(2**3)
#note that in python it is PEMDAS
#which means that parenthesis>  exponent>  mul/div>  add/sub
print(3*3+  3/3-7)


#BMI program
weight=int(input("enter your weight in kg"))
height=float(input("enter your height in m"))#becasue in bmi formula you need height in m 
bmi=weight/(height*height)
bmi1=int(bmi)#converted to int so that we get bmi without decimal
print(bmi1)
