#using .split()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = num1 / num2

res = str(res).split('.')[0]

print("\nThe value of", num1, "divided by", num2, "without a decimal point is", res)