print(" WELCOME TO THE TREASURE ISLAND")
print(" your mission is to find the treasure ")
choice=input(' where do you want to go? "left" or  "right".').lower()
if choice=="left":
    choice_1=input(" you came to lake, do you wanna swim or wait?").lower()
    if choice_1=="wait":
        choice_2=input("which door colour, red , yellow or blue?").lower()
        if choice_2== "yellow":
            print("lost")
        elif choice_2== "blue":
            print("lost")
        elif choice_2=="red":
            print("won")
        else:
            print("wrong choice")
    else:
        print("game over")
else:
    print("you fell into the hole game over for you")
    
     
