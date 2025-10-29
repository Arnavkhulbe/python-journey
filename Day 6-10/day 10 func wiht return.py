def hello(first,second):
    new=first.title()
    new1=second.title()
    return f"updated name is {new} {new1}"


output=hello(input("enter your first name"),input("enter your second name "))    
print(output)    
