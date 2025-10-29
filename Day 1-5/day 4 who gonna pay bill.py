import random

names = input("Enter names separated by comma and space: ")
names_list = names.split(", ")

person_who_pays = random.choice(names_list)
print(f"{person_who_pays} is going to pay!")

