def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def calculator():
    n1=int(input("enter first number"))

    dict={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
        }
    condition=True
    while condition:

        n2=int(input("enter next number"))
        for key in dict:
            print(key)
        choice=input("enter your choice")
        func=dict[choice]
        ans=func(n1,n2)
        print(f"{n1}{choice}{n2}={ans}")
        choice1=input(f"type 'y' to continue calculating with {ans} or 'n' to start with new calc")
        if choice1=="y":
            n1=ans
        else:
            condition=False
            calculator()
calculator()            

        
