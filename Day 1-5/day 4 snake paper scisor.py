import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images=[rock,paper,scissors] 

choice=int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))
print(images[choice])

rand=random.randint(0,2)
print(" computer choose: ")
print(images[rand])
if choice>=3 or choice<0:
    print("invalid, lost ")
elif rand==0 and choice==2:
    print("you lose ")
elif rand==2 and choice==0:
    print("you win")
elif rand<choice:
    print("you win")
elif rand>choice:
    print("you lost")
elif rand==choice:
    print("its a draw")
else:
    print("invalid choice")

