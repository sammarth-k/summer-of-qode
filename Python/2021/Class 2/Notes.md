```

```

# Class 2 - Conditionals

##### What You Will Learn

1. if, else, elif
2. boolean data
3. logical operators
4. single line conditionals

## Boolean data type

A variable of data type boolean can either be True or False (remember to capitalise the T/F).

```python
x = True
y = False
```

## Logical operators

Logical operators are used the way logic gates are used (if you do not know what they are, do not worry). In Python, we have three logical operators: not,or,and

### not

not returns the opposite Boolean value of a statement. For example, not True would return False.

### or

or returns True when one or more conditions are True. Therefore, the statement 3 > 2 or 2 < 4 returns True because 3 > 2 is True.

### and

and returns True when both conditions are True. Therefore 3 < 4 and 1==1 returns True while 3 < 4 and 1 !=1 returns False

#### Examples

```python
print (not True)
print (not False)
print ((3>2) or (2<4)) #one condition true
print ((3<2) or (2>4)) #neither condition true
print ((3>2) or (2<4)) #both conditions true
print ((3<4) and (1 == 1)) #both conditions true
print ((3<4) and 1 != 1) #one condition true
```

##### Output

```python
False
True
True
False
True
True
False
```

## Conditional statements

### Syntax

Conditional constructs are formatted as follows:

```python
if (condition):
    (code to follow if condition(s) is/are met)
elif (another condition):
    (alternative code - there can be one or more elifs)
else:
    (code to execute if none of the conditions are satisfied)
```

#### Indentation

The code within the ``if`` is indented i.e. you will notice when coding yourself that after a conditional statement, the next line will be written slightly ahead instead of the margin. The indented code is the one which will be followed by the program if the condition is true (in the case of ``if``). Python uses indentation, unlike other languages where you would use curly braces ``{}``.

#### Creating conditions

Conditions are dependent on boolean values i.e. ``True`` and ``False``. Your condition can use any operators which return a boolean value. Other conditions will *not* be executed by the interpreter. The main operators you can use in conditions are **comparison operators, membership operators, logical operators and identity operators** since these return boolean values. You can also use boolean values themselves to create a condition.

### ``if``

`if` is used before a condition to check create the first condition within a conditional construct. If the condition evaluates to ``True``, then the code within the if statement (i.e. the indented code) will be executed.

#### Example 1

```python
x = 18
if x > 10:
  print ('value greater than 10') # will print if x is greater than 10
```

##### Output

```Python
value greater than 10   
```

#### Example 2

#Using booleans

```python
y = True
if y == True:
    print('success') # this will always work since y is equal to True
```

##### Output

```Python
success
```

### ``elif``

You can use another conditional statement called ``elif`` (short for else if) which basically gives a an alternative condition. If the input doesn't meet the previous requirements, you can use as many ``elif`` statements as you want to create alternative conditions.

#### Example 1

```python
x = 15
if x > 15:
  print('x is greater than 15')
elif x <= 15: #second condition- if the first condition isnt true then it checks whether this condition has been met.
  print('x is less than or equal to 15')
```

##### Output

```
x is less than or equal to 15
```

You can also use the logical operators and and or to create more than one condition since these operators return boolean values.

#### Example 2

```python
x = 39
if x < 10 and x >= 0: #ignore negative values for now
    print('the number has a single digit')
elif (x >= 10 and x < 100): #you can break this line down to 'else, if x is greater than or equal to 10 and less than 100':
    print ('the number has two digits')
```

##### Output

```Python
the number has two digits
```

### ``else``

The else statement is used to give the program a case in which none of the conditions have been met.

It must succeed if and elif statements because the input has to fail the required conditions (i.e. the previous conditions return False) before following the code in the 'else' subsection.

#### Example 1

```python
z = 20

if z == 19:
  print('z is equal to 19')
else:
  print('z is not equal to 19')
```

##### Output

```
z does not equal to 19
```

#### Example 2

```Python
x = 10
if x > 10:
  print('x is greater than 10')
elif x < 10:
  print('x is less than 10')
else:
  print('x is equal to 10') #if the input isn;t greater than or less than 10, it has to be 10
```

##### Output

```
x is equal to 10
```

### Single line conditional:

We can write conditional statements in one line instead of going to the next line to write the code. Though this is usually used if there is one instruction after a condition. Few examples are given below:

#### Example

```python
x= 30
if x>29: print ('x is greater than 29')
else: print ('x is less than or equal to 29')
```

##### Output

```
x is greater than 29
```

### Dos and Don'ts

1. Avoid extremely long chains of ifs and elifs - they are very hard to maintain and also confusing
2. Do not use``else`` unless you need to execute code in case the condition has not been satisfied
