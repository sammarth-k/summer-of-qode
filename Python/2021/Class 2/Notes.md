```

```

# Class 2

##Boolean data type

A variable of data type boolean can either be True or False (remember to capitalise the T/F).

```python
x = True
y = False
```

##Logical operators
Logical operators are used the way logic gates are used. In Pyton, we have tree logical operators: not,or,and

###not
not returns the opposite Boolean value of a statement. For example, not True would return False.

###or
or returns True when one or more conditions are True. Therefore, the statement 3 > 2 or 2 < 4 returns True because 3 > 2 is True.

###and
and returns True when both conditions are True. Therefore 3 < 4 and 1==1 returns True while 3 < 4 and 1 !=1 returns False

####Examples
```python
print (not True)
print (not False)
print ((3>2) or (2<4)) #one condition true
print ((3<2) or (2>4)) #neither condition true
print ((3>2) or (2<4)) #both conditions true
print ((3<4) and (1 == 1)) #both conditions true
print ((3<4) and 1 != 1) #one condition true
```

#####Output
```python
False
True
True
False
True
True
False
```
##Conditional statements

###Syntax

Conditional constructs are formatted as follows:
if (condition):
    (code to follow if condition(s) is/are met)
elif:
    (alternative code)
else:
    (code to execute if none of the conditions are satisfied)

####Indentation
The codes within the if subsection is indented i.e. you will notice when coding yourself that after a conditional statement, the next line will be written slightly ahead instead of directly below the if statement. The indented code is the one which will be followed by the program if the condition is true.

####Creating conditions

Conditions are dependent on boolean values i.e. True and False. Your condition can use any operators which return a boolean value. Other conditions will not be executed by the interpreter. The major operators you can use in conditions are comparison operators, membership operators, logical operators and identity operators since these return boolean values. You can also use boolean values themselves to create a condition.


###if
if is used before a condition to check create the first condition within a conditional construct. If it is satisfied/true, then the code within the if statement will be executed.

####Example 1
```python
x = 18
if x > 10:
  print ('value greater than 10')
```
#####Output
```Python
value greater than 10   
```
####Example 2
#Using booleans
```python
y = True
if y == True:
    print('success')
```
#####Output
```Python
success
```

You can also use the logical operators and and or to create more than one condition since these operators return boolean values.

####Example
```python
x = 39
if x < 10 and x >= 0: #ignore negative values for now
    print('number has a single digit')
elif (x >= 10 and x < 100):    #you can break this line down to 'else, if x is greater than or equal to 10 and less than 100':
    print ('number has two digits')
```

#####Output
```Python
number has two digits
 ```
###elif
You can use another conditional statement called elif which basically gives a an alternative set of conditions. If the input doesn't meet the previous requirements, you can use as many elif statements as you want to create alternative conditions.

####Example
```python
x = 15
if x > 15:
  print('x is greater than 15')
elif x <= 15: #second condition- if the first condition isnt true then it checks whether this condition has been met.
  print('x is less than or equal to 15')
```

#####Output
x is less than or equal to 15

###else
The else statement is used to give the program a case in which none of the conditions have been met.

It must succeed if and elif statements because the input has to fail the required conditions (i.e. the previous conditions return False) before following the code in the 'else' subsection.

####Example 1
```python
z = 20

if z == 19:
  print('z is equal to 19')
else:
  print('z is not equal to 19')
```
#####Output
```Python
z does not equal to 19
```

####Example 2
```Python
x = 10
if x > 10:
  print('x is greater than 10')
elif x < 10:
  print('x is less than 10')
else:
  print('x is equal to 10') #if the input isn;t greater than or less than 10, it has to be 10
```
#####Output
```python
x is equal to 10
```

###Single line conditional:

We can write conditional statements in one line instead of going to the next line to write the code. Though this is usually used if there is one instruction after a condition. Few examples are given below:

####Example
```python
x= 30
if x>29: print ('x is greater than 29')
else: print ('x is less than or equal to 29')
```
#####Output
```Python
x is greater than 29
```
