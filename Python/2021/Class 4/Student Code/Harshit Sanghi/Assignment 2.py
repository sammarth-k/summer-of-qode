import random
list = ["q", "v", "r"]
choice = random.choice(list)
userChoice = input("Choose q, v or r: ")
if choice == "q" and userChoice == "v":
    print("You win!!")
    print(f"My choice was {choice}.")
elif choice == "v" and userChoice == "r":
    print("You win!!")
    print(f"My choice was {choice}.")
elif choice == "r" and userChoice == "q":
    print("You win!!")
elif choice == userChoice:
    print("We tied!!")
else:
    print("I win!!")
    print(f"My choice was {choice}.")
