def assignmentOne():
  age = input("Enter Your Age: ")
  age = int(age)

  yearsLeft = 100 - age

  return print(f"You Have {yearsLeft} years until you turn 100!")

def assignmentTwo():
  first = input("Enter the number of tea cups you want to buy from shop 1: ")
  second = input("Enter the number of tea cups you want to buy from shop 2: ")

  total = int(first) * 15 + int(second) * 30

  return print(f"Your total bill is {total}") 


which = input("Which home assignment would you like view the solution to, (1) or (2): ")

if (which == "1"):
  assignmentOne()
elif (which == "2"):
  assignmentTwo()
else:
  print("Invalid Assignment")
