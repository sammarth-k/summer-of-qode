num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))
print("Your range has been set")

num3 = int(input("Enter the third number that will decide whether its in range or not"))

if(num3>=num1 and num3<=num2):
  print(num3, "is in range")
else:
  print(num3, "is not in range")
