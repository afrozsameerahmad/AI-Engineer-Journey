'''
Strings are sequence of characters.
in pyhton specifically ,strings are a sequence of unicode characters.
in this above line unicode means that we can use characters from any language in the world in our strings.
In python, we can create a string by enclosing characters in single quotes('') or double quotes("").


Today Topics
1-Creating Strings
2-Accessing string
3-Adding characters to a string
4-Editing a string
5-Deleting a string
6-Operations on strings
7-String functions

'''


'''
1-Creating Strings
To create a string in python, we can use single quotes('') or double quotes("").


'''
a= 'hello'
a="hello"
a= '''hello'''
print(a)
'''
example where we use single  quotes and double quotes in the same string
"it's raining outside"


a= 'it's raining outside'
if you use like this python interpreter will get confused
because it will think that the string ends at the first single quote and then it will not understand what is after that.
To avoid this confusion we can use double quotes to create the string and then we can use single
quotes inside the string without any problem.

'''




'''
2- Accessing  Substrings from a string
To access a substring from a string, we can use slicing and indexing.
Indexing starts from 0 in python, so the first character of the string is at index 0, 
the second character is at index 1 and so on and in last index-1 is the last character of the string.
'''
# POSITIVE INDEXING
#right to left indexing stratts from 0
s="hello world"
print(s[0]) #h
print(s[1]) #e
print(s[2]) #l

# NEGATIVE INDEXING
#left to right indexing starts from -1
s="hello world"
print(s[-1]) #d
print(s[-2]) #l 
print(s[-7]) #o

'''
Slicing is used to access a range of characters from a string.
The syntax for slicing is string[start:end:step]

 start from 0 and end at n-1 is the last index of the string
'''
s="hello world"
print(s[0:5]) #hello
print(s[6:11]) #world


"""
Step in slicing
"""
#Positive step
s='12345678'
print(s[0:6:2])
# output: '135'

#negative step
s='12345678'
print(s[7:0:-2]) 
# always remember that when you use negative step, the start index should be greater than the end index
# output: '8642'


'''
simple trick to reverse a string using slicing
s='hello world'
print(s[::-1])
'''

s='hello world'
print(s[-5:]) 
# output: 'world'



'''
----Editing and deleting a string----


Strings are immutable in python, 
which means that we cannot changeor edit the characters of a string once it is created

'''

#  Deleting a string
s='hello world'
del s
print(s)  
# This will raise a NameError because the variable 's' has been deleted 
# actually we are not deleting the string but we are deleting the variable that is pointing to the string, 
#  so we cannot access the string anymore through that variable



'''
-----Operations on strings---
1-Arithmetic operations
2-Comparison operations
3-Logical operations
4-loops on strings
5- membership operations
'''

# In Arithmetic operations we can use + and * operators on strings
print('delhi'+'mumbai') # concatenation
print('delhi'*3) # repetition

# In comparison operations we can use ==, !=, >, <, >=, <= operators on strings
print('delhi'=='delhi') # True
print('delhi'!='mumbai') # True
print('delhi'>'mumbai') # False
# in comparison operations, the strings are compared lexicographically,
# which means that the characters are compared one by one from left to right until a difference is found.
print('delhi'<'mumbai') # True
print('delhi'>='delhi') # True
print('delhi'<='delhi') # True



#Logical operations on strings
s1='delhi'
s2='mumbai'
print(s1 and s2) 
'''output: mumbai beacause  python me internally koe bhi string jisme kuchh bhi agr 
characters hai to pyhton usko true smajhta hai
# and agr string empty hai to python usko false samajhta hai'''

print(s1 or s2) # delhi

not 'hello' # False
not '' # True



'''
Loops on strings
We can use for loop to iterate over the characters of a string.

'''
for i in 'hello':
    print(i)
    
# Membership operations on strings\ ensure it is case sensitive
s='hello world'
print('h' in s) # True
print('z' in s) # False
print('hello' in s) # True 




''''
-----------COMMON STRING FUNCTIONS----

1- len() function
2- max() function
3- min() function
4- sorted() function


'''

s ='Sameer'
print(len(s)) # 6
print(max(s)) # s
print(min(s)) # a
print(sorted(s)) # ['S', 'a', 'e', 'm', 'r']

'''
in sorted duplicate characters are print only once 
but in max and min duplicate characters are considered

'''
print(sorted('sameer', reverse=True)) # ['s', 'r', 'm', 'e', 'a']



'''
Functions which only work on strings
1- upper() function
2- lower() function
3- title() function
4- capitalize() function
5- swapcase() function

'''
s='sameer'
s.capitalize() # Sameer
# IT CAPTALIZES THE FIRST CHARACTER OF THE STRING AND MAKES ALL OTHER CHARACTERS LOWERCASE
s='hello world'


s.title() # Hello World
# IT CAPTALIZES THE FIRST CHARACTER OF EACH WORD IN THE STRING AND MAKES ALL

s.upper() # HELLO WORLD
# IT CONVERTS ALL THE CHARACTERS OF THE STRING TO UPPERCASE

s.lower() # hello world
# IT CONVERTS ALL THE CHARACTERS OF THE STRING TO LOWERCASE



'''
----COUNT ,FIND , INDEX FUNCTIONS---
'''
'Sameer Ahmad'.count('a') # 3
# it counts the number of occurrences of the specified substring in the string

'Sameer Ahmad'.find('a') # 1
# it returns the index of the first occurrence of the specified substring in the string
# if u find something which is nor present in the string then it will return -1
'Sameer Ahmad'.find('z') # -1   
'Sameer Ahmad'.index('a') # 1
# it returns the index of the first occurrence of the specified substring in the string


'''
the difference between find() and index() functions is that if the specified substring is not found in the string,
then find() function will return -1 but index() function will raise a ValueError.
'''



'''
endswith() and startswith() functions
'''
'hello world'.startswith('hello') # True
'hello world'.endswith('world') # True  
'hello world'.startswith('world') # False



'''
FORMAT() FUNCTION
The format() function is used to format the string by replacing the placeholders with the specified values.

'''


name = 'Sameer'
age = 25
print('My name is {} and I am {} years old.'.format(name, age))
# output: My name is Sameer and I am 25 years old.
# it automatically replaces the placeholders {} with the values of the variables name and age in the order they are passed to the format() function.


'''
isalpha(),isdigit(), isidentifier() and isalnum() functions 

isalpha() function returns True if all the characters in the string are alphabets and there is at least one character, otherwise it returns False.

isdigit() function returns True if all the characters in the string are digits and there is at least one character, otherwise it returns False.

isidentifier() function returns True if the string is a valid identifier, which means that it can be used as a variable name in python, otherwise it returns False.

isalnum() function returns True if all the characters in the string are alphanumeric, which means that they are either alphabets or digits and there is at least one character, otherwise it returns False.

'''
'sameer'.isalpha() # True
'sameer123'.isalpha() # False

'sameer123'.isdigit() # False
'12345'.isdigit() # True

'sameer'.isidentifier() # True
'123sameer'.isidentifier() # False

'sameer123'.isalnum() # True
'sameer 123'.isalnum() # False





'''
Split() and join() functions
Split function is used to split a string into a word by word basis and it returns a list of words in the string.
Key point to remember is that the split() function does not modify the original string, it returns a new list of words.

JOIN() function is used to join a list of strings into a single string with a specified separator between the strings.


'''

'hi my name is Sameer'.split() # ['hi', 'my', 'name', 'is', 'Sameer']
'hi,my,name,is,Sameer'.split('is,') # ['hi,my,name,', 'Sameer']

# by default it splits the string by space but we can also specify the separator to split the
# string by using the separator as an argument in the split() function.


" ".join(['hi', 'my', 'name', 'is', 'Sameer']) # 'hi my name is Sameer'
'-'.join(['hi', 'my', 'name', 'is', 'Sameer']) # 'hi-my-name-is-Sameer'



# REPLACE() FUNCTION
# The replace() function is used to replace a specified substring with another substring in the string.
'hi my name is Sameer'.replace('Sameer', 'Ahmad') # 'hi my name is Ahmad'


'''
STRIP() FUNCTION
The strip() function is used to remove the leading and trailing whitespace characters from the string.
'   hi my name is Sameer   '.strip() # 'hi my name is Sameer'

'''
'hi my name is sameer                   '.strip() 
# it remove trailing and leading whitespace but it does not remove the extra spaces between the words in the string'
# output:  'hi my name is sameer'
