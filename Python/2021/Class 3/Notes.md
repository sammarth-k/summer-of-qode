# Class 3: Loops

A loop is when a certain part of the code is repeated using specific commands. It helps when you have to run the same code multiple times, so instead of writing it again and again, you can just use a loop.

There are two types of loops in python, ``while`` loops and ``for`` loops.

## While Loops

A while loop takes a condition in the beginning of the loop and checks it. If the the condition is true, then the code inside will run, but if it isn't, the loop ends. The condition is checked each time before the loop runs. The syntax is as follows:

```python
x = 0
while x < 3:
  print(x)
  print('Hi')
  x += 1
```

##### Output

```
0
Hi
1
Hi
2
Hi
```

Let's look at that line by line. The first line we make a variable x and give it the value 0. This is called intialising a variable, and is important because when the loop begins, it will check the value of x, and the program will return an error if x doesn't have a value. Next we have the loop statement itself with the condition, and it runs because the conditions is true. Each time the loop runs, the value of x increases by one, and when it becomes 3, the loop stops as the condition becomes false. In this situation, x is called the counter variable, and we are incrementing it by 1.

### Break and Continue

There are two keywords here that help us use loops even better: ``break`` and ``continue``. ``break`` ends the loop, and ``continue`` skips only that particular iteration of the loop.

#### Examples

```python
x = 0
while x < 3:
  print(x)
  break
  print('Hi')
```

##### Output

```
0
```

```python
x = 0
while x < 3:
  print(x)
  if x == 1:
    break
  print('Hi')
  x += 1
```

##### Output

```
0
Hi
1
```

In the first example the loop only runs once, it prints the vaue of ``x`` and then stops, because of the ``break ``command, and it doesn't continue to print ``"Hi"`` as the loop ended there only. In the second example we can see the loop ran once, but once the value of ``x`` increased, the ``if`` statement caused the ``break`` statement to end the loop.

```python
x = 0
while x < 3:
  x += 1
  if x == 1:
    continue
  print(x)
  print('Hi')
```

##### Output

```python
2
Hi
3
Hi
```

In the example above you see the usage of ``continue``. You may also notice that increment statement is near the top of the loop. While this is not convention, in this case if we had put it near the bottom, it would have led to an infinite loop due to the nature of the ``continue`` statement. We will explain that in a bit. 

We see that ``x`` starts at ``0`` and immediately becomes ``1``, but ``x`` and ``'Hi'`` aren't printed, that is because the code reaches the ``continue`` statement and that resets the loop, taking it to the top, where ``x`` is incremented again. Now if the increment statement was below the ``continue``, it would keep resetting the loop when the value of ``x`` became ``1`` and the loop would never end. 

### Infinite Loop

An infinite loop is a loop that never breaks, or never stops. Remember to watch out for these, since they occur when you forget to add a mechanism to stop the loop. However, if you want to make one, there are several ways you can do that. 

```python
x = 0
while x < 1:
  print('Hi')
 ```
 
 #### Output
 
 
 When you run it, the program will indefinitely print 'Hi' untill it is forcefully stopped through keyboard interrupt (ctrl + c) or using some other method.
 
 ```python
 while True:
  print('Hi')
 ```
 
 ```python 
 while 1:
  print('Hi')
 ```
 
 All of these programs output the same thing, since the condition in the while system always stays True and never changes. 
 
You can use the break statement in conjunction with an infinite loop to create a unique type of loop that checks a condition at the end of the loop, compared to at the beginning like in a while loop
 
 ```python
 while 1:
  num = input("Enter the number 2")
  if num == '2':
    print('Very good')
    break 
  else:
    print('Try again')
 ```
 
 #### Output
 
 ``` 
 Enter the number 2
 INPUT - 3
 Try again
 INPUT - 2
 Very good
 ```
 
The loop keeps running until you satisfy the condition at the end of loop by entering the correct number.
 
### For Loop
 
A for loop in python is one that loops through certain values. Unlike the while loop which runs as long as the condition is True, the for loop only runs a given number of times.
A for loop as a variable known as the counter variable, which can be used in the loop and doesn't require incrementing. The syntax is as follows

```python

for i in 'hello':
  print(i)
 ```
 
#### Output

```
h
e
l
l
o
```

As the loop goes through the string, the value of i will be each element of the string, which we can use like a variable in the loop. 

We can use numbers in the loop as well, using the range() function.

```python
for i in range(4):
  print(i)
```

#### Output

```
0
1
2
3
```

The values of i in this case will be the numbers starting from 0 and till 3. The number put in the range function isn't included. The loop will however run 4 times only, which is the number in the range function. 

You can enter a number to begin with instead of 0 as well. 
```python 
for i in range(2,4):
  print(i)
```

#### Output
 
```
2
3
```

The first number is included. 

You can also enter a third parameter to change the increment value, known as step in this case

```python
for i in range(0,10,2):
  print(i)
```

#### Output

```
0
2
4
6
8
10
```

The step value is the increment here, and the value of i increase by that value every time. Negative values make the loop go reverse. 



 
 
