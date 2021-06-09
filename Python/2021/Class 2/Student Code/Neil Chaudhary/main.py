def one():
  number = input("Enter your number: ")
  number = int(number)

  even = (number % 2) == 0

  if (even != True):
    print("The Number you entered is odd")
  else:
    print("The number you entered is even")

def two():
  number = input("Enter the number of chocolates you need: ")
  number = int(number)

  if (number > 10):
    print("Sorry the shop doesnt have that mnay chocolates")
  else:
    print(f"Your total bill is {number * 15}")

def three():
  mininimum = int(input("What's the lower limit: "))
  maximum = int(input("What's the upper limit: "))
  number = int(input("Enter your number: "))

  isBetween = (number - mininimum) * (maximum - number) >= 0

  if (isBetween == True):
    print("Your number is between the limit")
  else:
    print("Your number is not between the limit")


