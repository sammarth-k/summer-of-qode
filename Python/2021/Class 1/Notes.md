# Class 1
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

## Operators
Arithmetic operators
```python

+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Remainder
//	Floor Division: rounds down to nearest integer
**	Exponent
```
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
