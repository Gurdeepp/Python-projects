import random
num = int(input("Guess a number between 0 to 20"))
print("computer's output")
r = random.randint(0,20)
print(r)
if r == num:
    print("your guess is perfect")
elif r > num:
    print("your guess is too low")
else:
    print("your guess is too high")