import random
seed1=int(input("enter random number \n"))
random.seed(seed1)
random_num=random.randint(0,1)
if random_num==1:
    print("heads")
else:
    print("tails")
