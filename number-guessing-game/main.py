import random
print("welcome to the number guessing game")
print("i am thinking of a number between 1 and 100")
num1=random.randint(1,101)
mode=input("whats the mode you want easy or difficult?\n").lower()
def guessing(mode):
    count=10
    if mode=="easy":
        print("you have 10 steps remaining to guess the number")
        while count>0:
            choice=int(input("enter any number between 1 and 100\n"))
            if choice>num1:
                print("Too high. guess again")
            elif choice<num1:
                print("Too low. guess again")
            elif choice==num1:
                print(f"you got it the number was {num1}")
                break
            count-=1
            print(f"you are having {count} chances now")
            
    elif mode=="difficult":
        count=5
        print("you have 5 steps remaining to guess the number")
        while count>0:
            choice=int(input("enter any number between 1 and 100\n"))
            if choice>num1:
                print("Too high. guess again")
            elif choice<num1:
                print("Too low. uess again")
            elif choice==num1:
                print(f"you got it the number was {num1}")
                break
            count-=1
            print(f"you are having {count} chances now")
            
guessing(mode)  