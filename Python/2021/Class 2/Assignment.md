# Assignment

This file contains all the assignments for this particular class. Students are required to solve each problem with Python and submit the code.

## Class Assignments

* [ ] Input a number and check whether it is greater than or less than 10.
* [ ] Input the users age and check whether they are elgible to drive or not.
* [ ] Create a grading system from A - E where A represents 90%+, B represents 80%+, C 70%+ and so on till E (50%+) after which a student must take the class again. Test your system with input.

### Solutions

#### Question 1

```python
# inputting the number
number = int(input("Enter a number: "))

# creating the condition
if number > 10:
    print(x, "is greater than 10")
else:
    print(x, "is less than 10")
```

#### Question 2

```python
# inputting age
age = int(input("Enter age: "))

# eligible if age is greater than or equal to 18
if age >= 18:
   print("Eligible to drive")
else:
   print("Not eligible to drive")
```

#### Question 3

```python
# getting marks
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 50:
    print("E")
else:
    print("Please take this class again!")
```

Why do we use only one condition instead of 2 (because there is a range)? Well, if you think about it, the interpreter evaluates the ``if`` condition first, then the first ``elif`` then the second ``elif`` and so on.

That means, if the marks are greater than or equal to 90, it will output A, but if they are not, then it will move to the next condition and this means the marks are less than 90. Now it will check whether the marks are greater than or equal to 80, and if they are, it means they are in the 80-90 range, thereby eliminating the need to use more than one condition!

Similarly, if the first ``elif`` is ``False``, the program knows the marks are less than 80, so it will then check if they are greater than 70, and if they are, it means the marks are in the 70-80 range.

This is an example of how we can use logic to reduce code length and reduce time it takes for the program to run. At this stage, runtime will not be much of a problem since the code is very small, but when you create programs which involve lots of processes, you will need to optimise your code for efficiency - that's what being a good programmer is about!

## Home Assignments

* [ ] Input number and check if it's odd or even
* [ ] A certain shop has 10 chocolates. Input the number of chocolates required by the user and return true if those many chocolates are available (false otherwise). If available, tell the total price (each chocolate costs 15 rupees).
* [ ] We need to write a program to tell if a certain number falls within a given range. Input 2 numbers indicating the upper and lower limit of the range, and then input a third number and tell the user if it is in the range or not. Upper and lower limits are included.

## Other Details
