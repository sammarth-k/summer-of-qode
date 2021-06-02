
<h1>Class 4 - Lists & Random Module</h1>

What You Will Learn
<ol>
  <li>Lists
  <li>The random module
</ol>

## 1.Lists
In python, a list is a type of data structure that can store multiple values in it
<br>We represent lists using square brackets in python [ ]
<br>Note here that the elements can be any datatype
<br>To define lists, we use this syntax
```python
numbers = [5,3,2,1,4] #This stores int values
names = ['Sammarth','Avi'] #This stores str values
```
### List indexing
Lists are ordered, ie. each position has a fixed value, called its <b>index</b>
<br>The indexing works in the following manner and <b>positive indexing begins from 0</b>
```python
            0        1       2        3         4      #positive indexing
fruits = ['apple','banana','orange','mango','lychee']
            -5      -4       -3       -2       -1      #negative indexing
``` 
To extract an item from the list using its index, we will do it in the following manner:
```python
print(fruits[1])  #index position 1  
print(fruits[-3]) #index position -3
```
<b>Output</b>
```
banana
orange 
```
Refer to index chart above to see how which elements got printed

### Changing items in the list
Lists are mutable ie. you can change its contents at any time in the program
<br>To do so, we have to use the following syntax:
```python
fruits = ['apple','banana','orange','mango','lychee']
fruits[2]='kiwi' #we are changing the value at index 2(orange) to 'kiwi'
print(fruits)
```
<b>Output</b>
```python
['apple','banana','kiwi','mango','lychee']
```

### Useful List methods and function
<b>NOTE:</b>For all examples below, my_list=['apple','banana','orange','mango','lychee']
<table>
  <tr>
    <th>Function/method
    <th>Explanation and example
    <th>Ouptut
  </tr>
  <tr>
    <td>my_list.append(<i>item</i>)
    <td>Adds item at the end of list<br><u>For eg:</u><br>my_list.append('kiwi')<br>print(my_list)
    <td>['apple','banana','orange','mango','lychee','kiwi']
  </tr>
  <tr>
    <td>my_list.remove(<i>item_name</i>)
    <td>Removes item from the list by name<br><u>For eg:</u><br>my_list.remove('mango')<br>print(my_list)
    <td>['apple','banana','orange','lychee']
  </tr>
  <tr>
    <td>my_list.pop(<i>item_index</i>)
    <td>Removes item from the list by index<br><u>For eg:</u><br>my_list.pop(2)<br>print(my_list)
    <td>['apple','banana','mango','lychee']
  </tr>
  <tr>
    <td>len(my_list)
    <td>Returns the length of the list<br><u>For eg:</u><br>print(len(my_list))
    <td>5
  </tr>
  <tr>
    <td>my_list.reverse()
    <td>Reverses the list<br><u>For eg:</u><br>my_list.reverse()<br>print(my_list)
    <td>['lychee','mango','orange','banana','apple']
  </tr>
</table>

## The ```random``` Module
What is the random modulle? It's basically a set of functions that allow you to generate random numbers and collections of random numbers. In this course we will be looking at the basic functions inside the random module which are useful for creating randomized games.

### Importing ```random```

We can add the random module to our program by typing:
```python
import random
```

### Calling Functions
To call functions from the random module we use the syntax ```random.function_name()```

For example:
```python
import random

random_num = random.random()
```
```random.random()``` generates a random number between 0 and 1, decimal numbers included.

For example, it could generate ```0.7972140627899765```.

### ```random.randint()```
This generates a random integer between a range of 2 numbers (both included)

#### Example
```python
import random
number = random.randint(1,100) # random integer between 1 and 100 (both included)
print(nnumber
```

##### Output
```
35
```

### ```random.randrange()```
This generates a random integer between a range of 2 numbers, but unlike ```random.randint()``` it will never include the final value in the output. It also allows a step value (similar to the ```range()``` function).

#### Example
```python
import random

number = random.randrange(1,100, 2) # see how we added a step value here, now it will only generate an integer excluding 2,4,6,8,... i.e. only odd numbers

print(number)
```

##### Output
```
49
```

### ```random.choice()```
This function selects a random value from a sequence (eg: a list)

#### Example
```python
import random

# creating a sample list of values
sample_list = [1,2,3,4,5]

# selecting a random element
number = random.choice(sample_list)

print(number)
```

##### Ouput
```
3
```

### ```random.sample()```
This function allows you to choice 'n' number of items randomly from a sequence (eg:list).

#### Example
```python
import random

# creating a sample list
sample_list = [1,2,3,4,5,6,7,8,9,10]

# getting a sample of values
sample = random.sample(sample_list, 3) # the 3 means a sample of 3 elements

print(sample)
```

##### Output
```python
[3,2,5]
```
