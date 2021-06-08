marks = float(input("Enter your marks percentage: "))

if marks >= 90 and marks < 100:
    print("\nYour grade is A")
elif marks >= 80 and marks < 90:
    print("\nYour grade is B")
elif marks >= 70 and marks < 80:
    print("\nYour grade is C")
elif marks >= 60 and marks < 70:
    print("\nYour grade is D")
elif marks >= 50 and marks < 60:
    print("\nYour grade is E")
elif marks == 100:
    print("\nYou have got a perfect score! Your grade is A")
elif marks < 50 and marks > 0:
    print("\nPlease take this class again!")
elif marks > 100:
    print("\nYou marks cannot be more than 100!")
elif marks <= 0:
    print("\nYour marks cannot be less than 0!")
