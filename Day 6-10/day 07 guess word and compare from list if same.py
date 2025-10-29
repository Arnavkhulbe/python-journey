import random
word=["hello","bye","guy"]
guessed=random.choice(word)
print(guessed)
guess=input("enter letter to be guesseed").lower()
for chosen in guessed:
    if guess==chosen:
        print("right")
    else:
        print("wrong")

