# Assignment

This file contains all the assignments for this particular class. Students are required to solve each problem with Python and submit the code.

## Class Assignments

* [ ] Ask a user to input a number 10 times and calculate the sum of the 10 numbers which are inputted. Do so with both a``for`` and``while`` loop.
* [ ] Make a loop which keeps asking for input from the user. The loop terminates only if the number inputted =``-1``.

### Solutions

#### Question 1

```python
# for loop
total = 0
for i in range(10):
    num = int(input("Enter number: "))
    total += num

print("The sum of all 10 numbers is", total)

# while loop
total = 0
count = 0
while count < 10:
    num = int(input("Enter number: "))
    total += num
    count += 1 # to count iterations

print("The sum of all 10 numbers is", total)
```

#### Question 2

```python
numm = ""
while num != "-1": # runs as long as the number is not -1
    num = input("Enter a number")

# this code is executed when the program exits the while loop
print("You entered -1!")
```

## Home Assignments

* [ ] Make a loop that keeps asking for a number from the user. The loop terminates only if the number inputted is greater than 50 or less than 0 (negative).
* [ ] Imagine you work for a firm with 5 employees. Write a program which allows all 5 employees to input their name and print it.
* [ ] Write a loop which prints all multiples of 4 until 100

## Other Details
