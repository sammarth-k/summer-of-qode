
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
```
fruits = ['apple','banana','orange','mango','lychee']
fruits[2]='kiwi' #we are changing the value at index 2(orange) to 'kiwi'
print(fruits)
```
<b>Output</b>
```
['apple','banana','kiwi','mango','lychee']
```

### Deleting items from a list
There are 2 ways to delete items from a list:
<ul>
  <li>The remove() method
      <br>This will remove a specified element from the list. You have to pass the name of the element as a parameter
      <br>For example
      ```python
      fruits = ['apple','banana','orange','mango','lychee']
      fruits.remove('mango') #finds an element 'mango' and removes it from the list
      print(fruits)
      ```
      <b>Output:</b>
      ```python
       ['apple','banana','orange','lychee']
      ```
