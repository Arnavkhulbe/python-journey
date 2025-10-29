score=input("enter list of scores")
score1=score.split()
print(score1)
score1=[int(i) for i in score1]
first=score1[0]
print(first)
for i in score1:
    if first<i:
        first=i
        
print(f" highest score is {first}")

