import random

num = random.randint(1, 10)

guess = int(input("Guess number (1-10): "))

if guess == num:
    print("Correct!")
else:
    print("Wrong, answer was", num)
