user = input("rock, paper or scissors: ")
actions = ["rock", "paper", "scissors"]
print ("You chose", (user))


if user == "rock":
  print ("The computer chose paper")
  print ("tough luck, paper covers rock ")
elif user == "scissors":
  print ("The computer chose rock")
  print ("GG, you lost")
elif user == "paper":
  print ("The computer chose scissors")
  print ("brush up your skills, come play with me next 31 february")