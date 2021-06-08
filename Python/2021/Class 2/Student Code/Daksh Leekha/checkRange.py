import sys

upp_range = float(input("Please enter your upper class limit: "))
low_range = float(input("Please enter your lower class limit: "))
num = float(input("Please enter any number: "))

if upp_range == low_range:
    print("\nThe upper and lower class limits cannot be the same!\n")
    sys.exit()

if num > low_range and num < upp_range:
    print("\nYour number is in the range specified!\n")
elif num == low_range:
    print("\nYour number is the same as the lower class limit\n")
elif num == upp_range:
    print("\nYour number is the same as the upper class limit\n")
else:
    print("\nYour nunmber is NOT in the specified range\n")
