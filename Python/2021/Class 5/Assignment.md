# Assignment

This file contains all the assignments for this particular class. Students are required to solve each problem with Python and submit the code.

## Class Assignments

* [ ] Define a function which takes in 2*different* integers and returns the greatest out of the two.
* [ ] Define a function which changes the value of a global variable.
* [ ] Define a function to replace a value in a list (do not use any methods)

### Solutions

#### Question 1

```python
def greatest(a,b):
    if a > b:
	return a
    return b
```

#### Question 2

```python
var = "value" # can be any value

def change():
    global var
  
    # checking initial value
    print(var)
  
    # changing the value
    var = "new value"
 
# calling the function
change()

# checking if the variable was changed
print(var)
```

#### Question 3

```python
def replace_value(list1, original, final):
  
    # finds index of element and replaces element at that index
    for i in range(len(list1)):
    	if list1[i] == original:
    	    list1[i] = final
  
    # no return statement is needed since the original list is changed

# taking sample data
sample_data = [1,2,3,4,5]

# calling the function
replace_value(sample_data, 4, 100)

# to verify change
print(sample_data)
```

## Home Assignments

Write a function which takes in a list of negative numbers and returns the number with the largest absolute value. You will have to research about the built-in abs() function.

* [ ] Write a function which takes a list as a parameter and returns the number of elements in it.
* [ ] Write a function which takes 2 parameters- a list and an element. The function should iterate over the list to check if the second parameter, the element, is in the list. If it is, then return true otherwise return false. Example- if [2,3,4] and 3 are passed then true should be returned, but if [2,3,4] and 6 are passed then false should be returned.

## Other Details
