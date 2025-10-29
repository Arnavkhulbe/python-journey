import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

new={}
def bid():
    name=input("enter name")
    price=int(input("enter bidding amount"))
    new[name]=price
    choice=input("yes or no ").lower()
    if choice=="yes":
        clear()
        bid()

    else:
        max=0
        winner=""
        for letter in new:
            if new[letter]>max:
                max=new[letter]
                winner=letter


        print(f"winner is {winner} with the hghest bid of {max}")            
bid()      
            
        
    
