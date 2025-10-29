import random
word=["hello","bye","guy"]
chosen_word=random.choice(word)
print(chosen_word)
display=[]
for words in chosen_word:
    display.append("_")
print(display)
while display!=list(chosen_word):
    guess=input("guess a letter").lower()
    for index in range(len(chosen_word)):
        letter=chosen_word[index]
        if guess==letter:
            display[index]=guess
    print(display)
print("you win")        

    
