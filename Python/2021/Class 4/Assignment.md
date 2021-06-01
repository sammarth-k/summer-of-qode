# Assignment

This file contains all the assignments for this particular class. Students are required to solve each problem with Python and submit the code.

## Class Assignments

* [ ] 🎲 Using the``random`` module, create a program to generate a list of 5 random numbers between 1-100 (both included) without repeats. Print the maximum and minimum value in this list using``max()`` and``min()``.
* [ ] 🔢 **Number Guessing Game:** Generate a random integer in the range 1 - 10 (both included). Store this value in a variable``value``. Input a number from the user and check whether it is the same.

### Solutions

#### Question 1

```python
import random

nums = []

for i in range(5):
    num = random.randint(1, 100)

    # to generate a new random number not in the list
    while num in nums:
        num = random.randint(1, 100)

    # .append() method adds an element to the end of the list
    nums.append(num)

print("Minimum:", min(nums), "Maximum:", max(nums))
```

#### Question 2

```python
import random

# generating random number
num = random.randint(1,10)

# get a guess from the user
user_num = int(input("Enter a guess for a number between 1 and 10 (both included): "))

if user_num == num:
    print("Congrats! You got it right!")
else:
    print("Tough luck! The correct answer was", num)
```

Do you think you can change the guessing range 🤔? Give it a try for 1-100!

## Home Assignments

* [ ] Add a feature to the number guessing game, where a person gets 3 tries to guess the number.
* [ ] rock**Rock Paper Scissors:** Create a Python version of the classic game, rock paper scissors. Hint: you can use``random.choice`` (Google it to see what it does!)
* [ ] Randomly select 5 elements of a list using their index (do*not* use``random.choice()``). Then, check for duplicate values.*Hint:* ****use the``.count()`` method.

## Other Details
