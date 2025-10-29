print(" welcome to pizza land ")
print("price for small pizza: 100 \nprice for medium pizza: 200 \nprice for large pizza: 300")
pizza=input(" which pizza u want to order- S_M_L")
price=0
if pizza=="s":
    print(" pay 100 ")
    price=100
elif pizza=="m":
    print(" pay 200 ")
    price=200
else:
    print("pay 300")
    price=300
chillies=input("do you want chillies for 5 rup? yes or no")
if chillies=="yes":
    price=price+5
    print(f" your price is {price}")
else :
    price=price
souce=input("do you want sauce for 10 rup? yes or no ")
if souce=="yes":
    price+=10
    print(f"your total price is {price}")
else:
    price=price
    print(f"your total price is {price}")
    
    
