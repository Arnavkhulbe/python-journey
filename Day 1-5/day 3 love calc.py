name1=input("enter your name")
name2=input("enter your crush name")
name=name1+name2

name_=name.lower()
t=name_.count("t")
r=name_.count("r")
u=name_.count("u")
e=name_.count("e")
true=t+r+u+e
l=name_.count("l")
o=name_.count("o")
v=name_.count("v")
e=name_.count("e")
love=l+o+v+e
true_love=str(true)+str(love)#we had to change it to str because we are concanating it not adding 
print(true_love)
ttrue_love=int(true_love)#converted to int because for comparing you need int not string
if (ttrue_love<10) or (ttrue_love>90):
    print("crazy")
elif (ttrue_love>10) and (ttrue_love<90):
    print(" good ")
else:
    print("ok ok ")

