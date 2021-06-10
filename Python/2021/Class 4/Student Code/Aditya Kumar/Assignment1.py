import random
guesses = 0
num = random.randint(1, 10)
while guesses < 3:
    guess = int(input("Enter a number: "))
    if guess == num:
        print("You guessed it! ")
        break
    elif guess != num:
        print("That was incorrect. ")
        guesses += 1
