import random
import sys


choices = ["rock", "paper", "scissor"]
sign = random.choice(choices)


print(choices)
user_choice = int(input("Enter a number from 1-3. '1' is equal to rock, '2' equals paper so on. Good Luck: "))


if user_choice < 1 or user_choice > 3:
    print("the number is invalid")
    sys.exit(0)


user_sign = choices[user_choice - 1]
print("the opponent chose", sign, "and you chose",  user_sign)


if sign == choices[0] and user_sign == choices[1] or sign == [1] and user_sign == choices[2] or sign == choices[2] and user_sign == choices[0]:
    print("you won")
elif sign == user_sign:
    print("it was a tie")
else:
    print("you lost")
