menu = {
    "espresso": {
        "ingredients": {
            "milk":0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
left={
    "water":300,
    "milk":200,
    "coffee":100}

change=0
case=True
money=0

while case:
    

   
    ans=input("what would you like? (espresso/latte/cappuccino):  or turn off the machine \n")
    
    
    
    
    def choice(ans,change,money):
        
        if ans=="latte" or ans=="espresso" or ans=="cappuccino":
            def resources(ans):   
                ing=menu[ans]["ingredients"]
                for i in ing:
                    if ing[i]>left[i]:
                        print(f"not enough {i}")
                        return False
                return True        
                    
              
            ans1=resources(ans)
            if ans1==False:
                return True,money
            
            
                        
            print("please enter coins")
            q=int(input("how many quarters? \n"))
            d=int(input("how many dimes? \n"))
            n=int(input("how many nickels? \n"))
            p=int(input("how many pennies? \n"))
            amnt=(q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
            if amnt>=menu[ans]["cost"]:
                change=amnt-menu[ans]["cost"]
                print(f"here is your {change} in change")
                print(f"here is your {ans} , enjoy!")
                left["water"]-=menu[ans]["ingredients"]["water"]
                left["milk"]-=menu[ans]["ingredients"]["milk"]
                left["coffee"]-=menu[ans]["ingredients"]["coffee"]
                return True,menu[ans]["cost"]
            elif amnt<menu[ans]["cost"]:
                print("not enough money")
                return False,money
        elif ans=="report":
            
            print("water: " + str(left["water"])+"ml")
            print("milk: " + str(left["milk"])+"ml")
            print("coffee: " + str(left["coffee"]) +"gm")
            print("money: "+ str(money))
            return True,money
        elif ans=="off":
            return False,money
           
    ans2,money1=choice(ans,change,money)
        
    money+=money1
    
    
    case=ans2 