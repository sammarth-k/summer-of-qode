# Class 1

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

<hr>

## Variables and basic data types:

int
```python
a = 5
```
str
```python
b = 'hello world'
```
float
```python
c = 2.0
```

printing variables:
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

Overriding variable values
```python
x = 'Hello World'
x = 25
print(x)
```

Output:
```python
25
```

Adding variables:
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
Arithmetic operators
|Operator|Operation|
|--------|---------|
|+	| Addition |
|-	|Subtraction|
|*	|Multiplication|
|/	|Division|
|%	|Remainder|
|//	|Floor Division: rounds down to nearest integer|
|**	|Exponent|
Examples
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
Output:
```python
7
-3
10
0.4
2
2
32
```
Assignment operators
```python
Operator	==> Operation
x+= (y) ==> 	x = x + y
x-= (y) ==>	x = x - y
x*= (y) ==> x = x * y
x/= (y) ==>	x = x / y
x//= (y) ==>	x= x // y
x**= (y)	==> x = x ** y
x%= (y)	==> x = x % y
```
Examples
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

Output:
```python

20
8
12
3.75
3
64
2
```
