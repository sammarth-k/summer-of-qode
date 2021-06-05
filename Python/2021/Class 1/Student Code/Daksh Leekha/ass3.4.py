#this is NOT correct. i still wanted to put it. Because it is the correct mathematical way of representing without a decimal point.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = num1 / num2

if num1%num2 == 0:
    res = int(res)
    print("\nThe value of", num1, "divided by", num2, "without a decimal point is", res)
else:
    print(f"\nThe value of {num1} divided by {num2} without a decimal point is {num1}/{num2}")
