# class assignment
input1 = int(input("your number is? "))
if input1 > 10:
    print("your number is greater than 10")
else:
    print("your number is less than 10")

age = int(input("what is your age "))
if age > 18:
    print("you are eligible to drive")
else:
    print("you are not eligible to drive")

marks = int(input("what was your exam result "))
total = int(input("what was your exam's total marks "))
grade = (marks/total)*100
print(grade, "%")
if grade >= 90:
    print("you got an A")
elif grade >= 80:
    print("you got a B")
elif grade >= 70:
    print("you got a C")
elif grade >= 60:
    print("you got a D")
elif grade >= 50:
    print("you got an E")
else:
    print("you need to redo class")

# assignment2------------------------------------------------------------
x = int(input("enter your number "))
if x % 2 == 0:
    print("your number is even")
elif x % 2 == 1:
    print("your number is odd")
else:
    print("idk")

cookies = int(input("how many cookies would you like "))
if cookies > 10:
    print("cookies not available")
else:
    price = cookies*15
    print("your total price is ", price)

r1 = int(input("what is the lower range "))
r2 = int(input("what is the higher range "))
num = int(input("write ur number "))
if (num > r1 and num < r2):
    print("the number is within range")
elif r1 > r2:
    print("range invalid")
else:
    print("number is not within range")
