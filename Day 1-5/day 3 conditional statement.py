height=int(input("enter your height in cm"))
age=int(input("enter age "))
bill=0
if height>=120:
    if age<=18:
        print("your ticket is  70 rup")
        bill=70
    elif age<=35:
        print("your ticket is 90 rup")
        bill=90
    else :
        print("your ticeket is 110 rup")
        bill=110
    ans=input(" do you want your pictures clicked? yes or no ")
    if ans== "yes":# gave indentation here becuse it should be with if block cuz agar if block ke andar aaya to ye claega
        bill=bill+15
        print(f" your ticket with pic is {bill}")
    else:

        print(f" your ticket is {bill}")
else:
   print("sorry, not eligible")

#to check odd or even
#num=int(input("enter number"))
#if num%2==0:
#    print("even")
#else:
#    print("odd")
    
