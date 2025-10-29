print("welcome to the tip calculator")
bill=float(input("enter the bil "))
per=int(input("what perc tip would you like to give? 10, 12 or 15? "))
billwithtip=(per/100)*bill+bill
print(f"total bill is {billwithtip}")
people=int(input("how many people to split the bill? "))
total_tip=billwithtip/people
finalamount=round(total_tip,2)#rounded upto two decimal place
print(f" each person should pay {finalamount}")


