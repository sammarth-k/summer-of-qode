import random
num = random.randint(1,8)
count = 0
while count < 3:
  user_num = int(input("Enter a guess for a number between 1 and 8 (both included): "))
  if user_num == num:
    print("Congrats! You got it right!")
    break
  else:
    print("Wrong pls try again")
    count += 1

user = input("rock, paper or scissors: ")
actions = ["rock", "paper", "scissors"]
computer = random.choice(actions)
print ("You chose", (user))
print ("The computer chose", (computer))
if user==computer:
  print (f"Both players have chosen {user}. Tie! Try again or play later")
elif user == "rock":
  if computer == "scissors":
    print ("rock smashes scissors, winner winner chicken dinner")
  else:
    print ("tough luck, paper covers rock ")
elif user == "scissors":
  if computer == "paper":
    print ("scissors shreds paper. you win")
  else:
    print ("GG, you lost")
elif user == "paper":
  if computer == "rock":
    print ("lucky, ill beat you next time")
  else:
    print ("brush up your skills, come play with me next 31 february")

list = [1,2,3,4,5,2,5,4,7,3,2,3,4,5,10,10001]
x = list.count(2) 
print(x)
