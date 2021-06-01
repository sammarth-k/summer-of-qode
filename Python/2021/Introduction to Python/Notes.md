# Class 1 - Introduction to Python

#### What You Will Learn

1. What is Python?
2. Python Syntax
3. Data Types in Python
4. Operators in Python

## Introduction to Python

- Creator: Guido Van Rossum
- Beginner-friendly language
- Wide variety of applications: Game Development, Data Science, AI, etc.
- Unique syntax: no curly braces or semicolons (many languages have these)

## Downloading Python (Optional)

You can download Python from the official [Python](https://python.org) website and it is also available in the Windows Store

## Course Materials

### Platform

For this course, we will be using [Replit](https://replit.com) which will allow you to access all of our code and also code yourself, without having to install anything. To get started you will need to make a free account.

### Code Repository

All of the code, notes and assignments of this course will be hosted in this repository. We advise you to make a GitHub account and **fork** our repository, which essentially means create a copy of it in your own profile. This will allow you to upload your code to your own copy and have it for future reference, with all of our notes and assignments.You can also create a **pull request** if you want to merge with the original repository, and we will have to approve your request.

While GitHub is not the primary focus of this course, we advise you to become familiar with its interface since you will be using i very often if you choose to pursue Python further.

---

# Variables and basic data types:

A variable is something that stores data within it, and can be used later by simply using the name it has been given.

### Components of a Variable

1. **Identifier:** The identifier is the name of the variable. It has naming rules which we have to follow or we will get an error. On top of that, there are certain conventions we use.
2. **Literal:** The value(s) stored within a variable is the literal

For example in the expression ``x = 5``, x is the variable **identifier** while 5 is the **literal**

#### Identifier Rules

###### Don't

1. Cannot begin with a digit. Eg:``1var`` is not allowed
2. Cannot use a**keyword** as an identifier. There are 33 keywords in Python, but here are the ones relevant right now:
   * | and  | or   | not   | is  | in       | None  | True   | False  | return | if |
     | ---- | ---- | ----- | --- | -------- | ----- | ------ | ------ | ------ | -- |
     | else | elif | while | for | continue | break | global | import | class  | as |

     You will see these appear thorughout the course, and will soon have them on your fingertios
3. Special Symbols are not allowed, eg``! @ # \$ % ^ & *``

###### Do

1. Meaningful variable names - can be a combination of letters and numbers. For example if I want to store a persons age, I should name the variable``age`` rather than``a`` since it helps a person understand your code better (and for you when you come back to it!)
2. By convention, when you have more than one word in a variable name, separate each word by an underscore, eg:``my_age = 17``
3. You can have any length as desired, but try to keep variable names as short as possible.

In the examples you will see that we have used single character identifiers, but that is just for convenience and readability. Don't do this in real programs! You will see that in our proper codes, we have used descriptive names, as you should.

#### Basic Literal Types

##### int (integers)

```python
a = 5
```

##### str (strings)

```python
b = 'hello world'
```

##### float (floating point numbers)

```python
c = 2.0
```

##### Printing Variables

```python
print(a)
print(b)
print(c)
```

Output:

```python
5
hello world
2.0
```

###### Overriding variable values

```python
x = 'Hello World'
x = 25
print(x)
```

Output:

```python
25
```

###### Adding variables:

```python
x = 'Hello'
y = 'World'
z = x + y
x2 = 5
y2 = 10
z2 = x2 + y2
print(z)
print(z2)
```

Output:

```python
HelloWorld
15
```

<hr>

## Operators

### Arithmetic operators

| Operator | Operation                                      |
| -------- | ---------------------------------------------- |
| +        | Addition                                       |
| -        | Subtraction                                    |
| *        | Multiplication                                 |
| /        | Division                                       |
| %        | Remainder                                      |
| //       | Floor Division: rounds down to nearest integer |
| **       | Exponent                                       |
|          |                                                |

#### Examples

```python
x= 2
y= 5
print (x+y)
print (x-y)
print (x*y)
print (x/y)
print (x%y)
print (y//x)
print (x**y)
```

##### Output:

```python
7
-3
10
0.4
2
2
32
```

### Assignment operators

|       Operator       | Operation                                                     |
| :------------------: | ------------------------------------------------------------- |
| **``x += y``** | ``x = x + y`` - adds y to existing value of x                 |
|      ``x -= y``      | ``x = x - y`` - subtracts y from existing value of x          |
|      ``x *= y``      | ``x = x*y`` - multiplies existing value of x by y             |
|      ``x \= y``      | ``x = x / y `` - divides existing value of x by y             |
|     ``x //= y``     | ``x = x//y`` - floor divides existing value of x by y         |
|     ``x **= y``     | ``x = x ** y`` - raises existing value of x to the power y    |
|      ``x %= y``      | ``x = x % y`` - remainder of existing value of x divided by y |

#### Examples

```python
#equal to
x = 2

#equals to sum
x += 18
print(x)

#equals to difference
x= 10
x -= 4
print(x)

#equals to product
x= 3
x *= 4
print(x)

#equals to quotient
x = 15
x /= 4
print(x)

#equals to quotient (floor)
x = 20
x //= 6
print(x)

#equals to value raised to the power
x= 8
x **= 3
print(x)

#equals to remainder
x = 14
x %= 4
print(x)
```

##### Output:

```python
20
8
12
3.75
3
64
2
```
