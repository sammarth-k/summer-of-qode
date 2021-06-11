import random
list = ['r', 'p', 's']
choice = random.choice(list)
userChoice = input("Choose r, p or s: ")
if choice == 'r' and userChoice == 'p':
    print("You win!!")
    print(f"My choice was {choice}.")
elif choice == 'p' and userChoice == 's':
    print("You win!!")
    print(f"My choice was {choice}.")
elif choice == 's' and userChoice == 'r':
    print("You win!!")
elif choice == userChoice:
    print("We tied!!")
else:
    print("I win!!")
    print(f"My choice was {choice}.")
