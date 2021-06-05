num1 = int(input("Please enter an integer: "))

num_rem = num1%2

if num_rem == 0:
    print("\nThere is no remainder on dividing", num1, "by 2.\n")
else:
    print("\nThe remainder of", num1, "divided by 2 is", num1%2, "\n")