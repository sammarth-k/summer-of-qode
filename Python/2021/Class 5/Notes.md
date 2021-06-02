# Class 5: Functions

## What are functions
They are blocks of code which runs only when called. They are used to make code more efficient, instead of writing the same twice, you can write the function one time and use it as many times as needed.


## Types of functions

### 1. Built-in functions
These are functions already present in python and are available for use for programmers.

#### Examples
You have used these functions before.
```python
int() #built-in function which returns an integer number
input() #built-in function which allows input
str() #built-in function which returns a string object
```
### 2. User defined functions
These are functions which are created by programmer itself.

### Creating user-defined functions:
In Python a function is created using the def keyword:
```python
def func1(): #user-defined function
  print ('Hello!')
```
### Calling functions
To call a function, use the function name followed by parenthesis:
```python
func1()
```
#### Output
```python
Hello!
```

# Arguments
Functions can have certain requirements to be passed before being called. These requirements are called arguments. If they are called without these arguments then it would cause an error. In func1 above, there were no arguments required. Remember, there is no limit to how many arguments can be passed.

#### Examples
```python
def increment(var): #the argument in this case is var. An integer or floating point value must be passed when calling the function increment
  print (var + 1)
```
A call to
```python
increment()
```
would case an error. However:
```python
increment(3)
increment(5.5)
```
would output:
```python
4
6.5
```

## Global and local variables

### Local variables
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

```python
def f1():
  x = 300
  print(x)
f1() #will work and print 300
print (x) #will not work since there is no variable called x outside the function
```
x is a local variable in the code above.

### Global variables
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
```python
x = 300

def f2():
  print(x)
f2() #will work and print 300
print (x) #will work and print 300 since x is defined outside variable
```
x is a global variable in the code above.



### Scope of global vs local variables

```python
x = 300

def f3():
  x = 200
  print(x)

f3() #prints 200
print(x) #prints 300
```
x is treated as a separate variable in the global scope (x = 300) and in the local scope (x=200 and so calling a function will print the local variable x but simply printing x would output the global variable x.

### Changing values of local and global variables

#### Changing a local variable to a global variable
Use the 'global' keyword to change a local variable into a global variable
```python
def f4():
  global x
  x = 300

f4() #turns x into a global variable
print(x) #also prints 300 since x has been made a global variable
```
#### Changing the value of a global variable
```python
x = 300

def f6():
  global x
  x = 200

f6()
print(x) #prints 200 since x is made a global variable and equals to 200 in the function f6. 
```
