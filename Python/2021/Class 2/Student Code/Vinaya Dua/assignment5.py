# We need to write a program to tell if a certain number falls within a given range. 
# Input 2 numbers indicating the upper and lower limit of the range,
# and then input a third number and tell the user if it is in the range or not. 
# Upper and lower limits are included.

num1= int(input("enter your first number:"))
num2= int(input("enter your second number:"))
num3= int(input("please enter another number to check if it is in range:"))

if num3>= num1 and num3<= num2:

    print("the number is in range")

else:
    print("number is not in range")
