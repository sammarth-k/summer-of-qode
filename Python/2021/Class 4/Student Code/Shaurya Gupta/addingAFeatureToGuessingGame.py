import random

num = random.randint(1,10)

count = 0
while count < 3:
    user_num = int(input("Enter a guess for a number between 1 and 10 (both included): "))
    count+=1
    won = False
    if user_num == num:
        print("Congrats! You got it right!")
        won = True
        break
if won == False:
    print("Tough luck! The correct answer was", num)
