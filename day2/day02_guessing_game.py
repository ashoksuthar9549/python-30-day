import random

secret_number = random.randint(1, 100)

num = int(input("Guess the number between 1 and 100"))

if(num > secret_number):
    print("Too high! Try again.")
elif(num < secret_number):
    print("Too low! Try again.")
elif(num == secret_number):
    print("Congratulations! You guessed it!")
