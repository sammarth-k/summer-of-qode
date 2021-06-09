#Input the age of someone and tell them how many years they have before they turn 100 years old

age = int(input("Enter your age: "))

if age <= 0:
    age = 1


if age > 100:
    print("you have already turned a hundred years old")
else:
    age_before_Hundred = 100 - age
    print("You will turn a hundred in ", age_before_Hundred, " years")
