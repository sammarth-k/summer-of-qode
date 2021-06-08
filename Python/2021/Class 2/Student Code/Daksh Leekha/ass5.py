age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to drive")
elif age <= 0:
    print("You are not born yet!")
else:
    print("Not eligible to drive")
