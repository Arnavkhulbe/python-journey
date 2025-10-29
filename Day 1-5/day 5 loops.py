fruits=["apple","orange","kiwi"]
for fruit in fruits:
    print(fruit)
    print(fruit+ " pie")


height=input("enter a list of student hieght")
height1=height.split()
print(height1)
length=len(height1)
#print(length)
add=0
for i in height1:
    add=add+int(i)
#print(add)
avg=add/length
print(round(avg))
print(f" avg height of students is {avg}")




