'''
----All Content of this file is written by me based on my understanding of the topic
at some places u find good real world examples  for better understanding
---


Today Topics....

1-What are Lists 
2-List vs Arrays
3-Characteristics of Lists
4-How to create a List
5-Access item from a List
6-Adding items to a list 
7-Deleting items from a list
8-Operations on lists 
9-Functions on Lists
10-List Comprehension



'''


'''
1-----------------What are Lists--------------


Lists are datatype where you can store multiple items in a single variable.
More technically list act like dynamic arrays which mean you can add more items  on the fly .
Lists are ordered, mutable and allow duplicate values.
example: movies reviews --- if u can store every review in a single variable it will take lot of space 
but if you store all the reviews in a single variable as a list it will be more efficient and easy to manage.

we store list in square brackets [] and each item is separated by a comma.example:
a = [1, 2, 3, "hello", True]
'''


'''
2-----------------List vs Arrays-------------


In array the size of array is fixed  length and all the items must be homogenous means similar datatype

but in list the size is dynamic and can store items of different datatypes.

lets understand this with example 

---Advantage of list over array---
in array we define int arr[50] which means we can store 50 integers supoose if we use 10 integers only
then 40 spaces will be wasted 
but in list we can store 10 integers and we can add more 
means list are flexible and memory efficient than arrays.


--Disadvantage of list over array-----
list are slower than arrays because of their dynamic nature 

important ---
in list when we create list then the list items randomly stored in memory 
    and we access them using index
list is referential array where each element is a reference to another object in memory  


to know address of list items we can use id() function which return the memory address of the object
example:
my_list = [1, 2, 3]
print(id(my_list[0]))  # memory address of first item
'''

l=[1, 2, 3, "hello", True]
print(id(l[0]))  # memory address of first item
print(id(l[1]))  # memory address of second item




'''
3-Characteristics of Lists

1-Ordered: the items in a list have a defined order and that order will not change unless we explicitly change it.
example :
l=[1,2,3]
l1=[3,2,1]
print(l)  # output: [1, 2, 3]
print(l1) # output: [3, 2, 1]
l==l1  # output: False because the order of items is different in both lists
as you can see the order of items in l and l1 is different



2-Mutable: we can change the items in the list after it is created
3-Allow duplicate values: we can have multiple items with the same value in a list
4-Heterogeneous: we can store items of different datatypes in a list
5-Dynamic: we can add or remove items from a list on the fly
6-Indexing and slicing: we can access items in a list using their index and we can also slice the list to get a subset of items
7-Methods: lists have built-in methods that allow us to perform various operations on them such as adding, removing, sorting, etc.
8-can contain any kind of object: lists can contain any kind of object including other lists, dictionaries, etc.

'''


'''
4-How to create a List---

we can create a list by enclosing a comma-separated sequence of items in square brackets []
'''
# EMPTY LIST
l=[]

# 1D LIST
l1=[1,2,3,4,5]

# 2D LIST
l2=[[1,2,3],[4,5,6],[7,8,9]]

# Quick question it is homogeneous or heterogeneous list ?
# answer is heterogeneous list because it contains items of different datatypes


# 3D LIST
l3=[[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
# is this homogeneous or heterogeneous list ?
# answer is homogeneous list because it contains items of same datatypes which are lists


# using type conversion
l4=list((1,2,3,4,5))
print(list(l4))  # output: [1, 2, 3, 4, 5]   string to list




'''
5-Access item from a List---

1-INDEXING
we can access items in a list using their index starting from 0 for the first item, 1 for the second item, and so on. 
we can also use negative indexing to access items from the end of the list.

2-SLICING


'''

# POSITIVE INDEXING
l=[1,2,3,4,5]
print(l[0])  # output: 1
print(l[2])  # output: 3

# NEGATIVE INDEXING
print(l[-1])  # output: 5
print(l[-3])  # output: 3

# SLICING
l=[1,2,3,4,5]
print(l[1:4])  # output: [2, 3, 4] it start from  and fetch items n-1 last index is not included
print(l[:3])   # output: [1, 2, 3]
print(l[2:5])  # output: [3, 4, 5]
print(l[0:5:2])  # output: [1, 3, 5] it fetches every second item from the list

# in slicing we have three parameters start, stop and step
# start is the index from which we want to start slicing, stop is the index at which
# we want to stop slicing and step is the number of items we want to skip while slicing



'''
6-Adding items to a list------

1-append() method: it adds an item to the end of the list
2-insert() method: it adds an item at a specific index in the list
3-extend() method: it adds all the items from another list to the end of the list
4-using + operator: we can concatenate two lists using the + operator
5-using * operator: we can repeat a list multiple times using the * operator
6-using list comprehension: we can create a new list by applying an expression to each item
    in an existing list using list comprehension

'''

l=[1,2,3,4]
# using append() method
l.append(5)
print(l)  # output: [1, 2, 3, 4, 5]

# using insert() method
l.insert(2, 10)  # it will insert 10 at index 2
print(l)  # output: [1, 2, 10, 3, 4, 5]

# using extend() method
l.extend([6, 7, 8])  # it will add all the items from the list [6, 7, 8] to the end of the list
print(l)  # output: [1, 2, 10, 3, 4, 5, 6, 7, 8]

# using + operator
l1=[9,10]
l2=l+l1  # it will concatenate l and l1 and store the result in l2
print(l2)  # output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 10]    

# using * operator
l3=l*2  # it will repeat the list l twice and store the result in l3
print(l3)  # output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 10]

# using list comprehension
l4=[x*2 for x in l]  # it will create a new list by applying the expression x*2 to each item in the list l
print(l4)  # output: [2, 4, 20, 6, 8, 10, 12, 14, 16, 18, 20] it will create a new list by multiplying each item in the list l by 2


# EDITING ITEMS IN A LIST
l=[1,2,3,4,5]
l[2]=10  # it will change the value of the item at index 2 to 10
print(l)  # output: [1, 2, 10, 4, 5]



'''
7-Deleting items from a list------
1-del statement: it can be used to delete an item at a specific index or to delete the entire list
2-remove() method: it removes the first occurrence of a specific value from the list
3-pop() method: it removes and returns the item at a specific index (default is the last item)
4-clear() method: it removes all items from the list

'''

l=[1,2,3,4,5]
# using del statement
del l[2]  # it will delete the item at index 2
print(l)  # output: [1, 2, 4, 5]

# using remove() method
l.remove(4)  # it will remove the first occurrence of the value 4 from the list
print(l)  # output: [1, 2, 5]

# using pop() method
l.pop(1)  # it will remove and return the item at index 1
print(l)  # output: [1, 4, 5]

# using clear() method
l.clear()  # it will remove all items from the list
print(l)  # output: []


'''
----List functions-------
1-len() function: it returns the number of items in the list
2-sum() function: it returns the sum of all the items in the list (only for numeric lists)
3-max() function: it returns the maximum value from the list (only for numeric lists)
4-min() function: it returns the minimum value from the list (only for numeric lists)
5-sorted() function: it returns a new sorted list from the items in the list
6-reversed() function: it returns a new reversed list from the items in the list
'''
l=[1,2,3,4,5]
print(len(l))  # output: 5

print(sum(l))  # output: 15
print(max(l))  # output: 5
print(min(l))  # output: 1
print(sorted(l, reverse=True))  # output: [5, 4, 3, 2, 1] it will return a new sorted list in descending order
print(list(reversed(l)))  # output: [5, 4, 3, 2, 1] it will return a new reversed list from the items in the list 

# count
print(l.count(3))  # output: 1 it will return the number of times the value 3 appears in the list 

# index
print(l.index(4))  # output: 3 it will return the index of the first occurrence of the value 4 in the list 

# sort : it will sort the list in ascending order and it will modify the original list 
l.sort()
print(l)  # output: [1, 2, 3, 4, 5] it will sort the list in ascending order and it will modify the original list

#copy
l1=l.copy()  # it will create a copy of the list l and store it in l1
print(l1)  # output: [1, 2, 3, 4, 5] it will create a copy of the list l and store it in l1


'''
LIST COMPREHENSION


List comprehension is a concise way to create lists. 
It consists of brackets containing an expression followed by a for clause then zero or more for or if clauses. 
The expressions can be anything, meaning you can put in all kinds of objects in lists.
Example: new_list = [expression for item in iterable if condition==True]


Advantages of list comprehension 
1- it is more concise and readable than traditional for loops for creating lists
2- it can be faster than traditional for loops for creating lists because it is optimized for performance
3- it can be used to create new lists by applying an expression to each item in an existing list
4- it can be used to filter items from an existing list based on a condition
Example:
squares = [x**2 for x in range(10) if x%2==0]  # it will create a new list of squares of even numbers from 0 to 9
print(squares)  # output: [0, 4, 16, 36, 64] it will create a new list of squares of even numbers from 0 to 9

'''



'''

---IMPORTANT---

TWO WAYS TO TRAVERSE A LIST
1-ITEMWISE
2-INDEXWISE

'''

# itemwise traversal
l=[1,2,3,4,5]
for item in l:
    print(item)  # output: 1 2 3 4 5 it will print each item in the list on a new line
    
    
# indexwise traversal
l=[1,2,3,4,5]
for i in range(len(l)):
    print(l[i])  # output: 1 2 3 4 5 it will print each item in the list on a new line using indexwise traversal
    
