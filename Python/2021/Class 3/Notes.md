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

```python
0
Hi
1
Hi
2
Hi
```

Let's look at that line by line. The first line we make a variable x and give it the value 0. This is called intialising a variable, and is important because when the loop begins, it will check the value of x, and the program will return an error if x doesn't have a value. Next we have the loop statement itself with the condition, and it runs because the conditions is true. Each time the loop runs, the value of x increases by one, and when it becomes 2, the loop stops as the condition becomes false. In this situation, x is called the counter variable, and we are incrementing it by 1.

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

```python
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

```python
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

We see that ``x`` starts at ``0`` and immedietly becomes ``1``, but ``x`` and ``'Hi'`` aren't printed, that is because the code reaches the ``continue`` statement and that resets the loop, taking it to the top, where ``x`` is incremented again. Now if the increment statement was below the ``continue``, it would keep resetting the loop when the value of ``x`` became ``1`` and the loop would never end. 

### Infinite Loop
