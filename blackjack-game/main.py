
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(cards):
    score=sum(cards)
    if score==21 and len(cards)==2: 
        return 0
    elif 11 in cards and score>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)    
    else:
        return score
def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return "its a draw"
    elif dealer_score==0:
        return "you lose"
    elif user_score==0:
        return "you won"
    elif user_score>21:
        return "you lose"
    elif dealer_score>21:
        return "you won"
    else:
        if user_score>dealer_score:
            return "you won"
        else:
            return "you lose"
case1=True
while case1:
    user=[]
    dealer=[]
    for i in range(2):
        user.append(deal_card())
        dealer.append(deal_card())
    #print(user)
    
    case=True
    while case:
        user_score=calculate_score(user)
        dealer_score=calculate_score(dealer)
        print(f" your score is {user_score}, your cards: {user}")
        print(f" computer first card: {dealer[0]}")
        if user_score==0 or dealer_score==0:
            case=False
        elif user_score>21:
            case=False
        elif user_score<21:
            ans=input("do you want to add another card...yes or no?")
            if ans=="yes":
                user.append(deal_card())
            elif ans=="no":
                case=False
        user_score=calculate_score(user) 
    if user_score!=0 and user_score<=21:     
        while dealer_score<17:        
            dealer.append(deal_card())
            dealer_score=calculate_score(dealer)
    
    result=compare(user_score,dealer_score) 
    print(result)
    ans1=input("do you want to play again or not...yes or no?")
    if ans1=="yes":
        case1=True
    else:
        case1=False
        print("game ended")