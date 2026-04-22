#- Create a program that flips a coin k times and prints the sequence of results (Heads or Tails).
import random
def coin_flip(number):
    outcome=['Head','tail']
    flip=[]
    for i in range (number):
        flip.append(random.choice(outcome))
    return flip

k=int(input("Enter how many times u want flip a coin"))
answer=coin_flip(k)
print(answer)