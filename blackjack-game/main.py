import random
user=[]
dealer=[]
def deal_card():
    num=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    choice=random.choice(num)
    return choice

for i in range(2):
    user.append(deal_card())
    dealer.append(deal_card())
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
game_over=False
#Hint 11: The score will need to be rechecked with every new card drawn and the
#checks in Hint 9 need to be repeated until the game ends.
while not game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack
    #(0) or if the user's score is over 21, then the game ends.
    out1=calculate_score(user)
    out2=calculate_score(dealer)
    print(f"your cards are{user} and score is {out1}")
    print(f"dealer first card is {dealer[0]}")
    if out1==0 or out2==0 or out1>21:
        game_over=True
    #Hint 10: If the game has not ended, ask the user if they want to draw another
    #card. If yes, then use the deal_card() function to add another card to the
    #user_cards List. If no, then the game has ended.
    if game_over==False:
        choice1=input("do you want to add more('yes' or 'no')").lower()
        if choice1=="yes":
            user.append(deal_card())  
            print(f"your score is now {calculate_score(user)}")
        elif choice1=="no":
            game_over=True
#Hint 12: Once the user is done, it's time to let the computer play. The computer
#should keep drawing cards as long as it has a score less than 17.
while out2!=21 and out2<17:
    dealer.append(deal_card())
    out2=calculate_score(dealer)
    print(f"your final cards are{user} and xcore being {out1}")
    print(f"comp cards are{dealer} and xcore being {out2}")
def compare(out1,out2):
    if out1==out2:
        print("draw")
    elif out1==0:
        print("user wins")
    elif out2==0:
        print("you lost ")
    elif out1>21:
        print("you lost ")
    elif out2>21:
        print("you won")
    elif out1>out2:
        print("you won")
    else:
        print("you lost ")
compare(out1,out2) 