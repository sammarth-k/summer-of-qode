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
Output:
```
banana
orange 
```
Refer to index chart above to see how which elements got printed
