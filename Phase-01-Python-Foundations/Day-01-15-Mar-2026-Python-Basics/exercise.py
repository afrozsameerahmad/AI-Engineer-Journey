# 1-Python output

# python is case-sensitive language
print("Hello, World!")
print("hello",1,1.5,True)

#end parameter in print function "/n" is default end parameter in print function

print("Hello", end=" ")
print("World")



# 2-Python data types

# int, float, str, bool
a = 10 # int
b = 3.14 # float/decimal
c = "Hello" # str
d = True # bool

#type function is used to check the data type of a variable
print(type(a))
print(type(b))      
print(type(c))
print(type(d))

#complex data type
e = 2 + 3j # complex number has real part and imaginary part
print(type(e))
print(e.real) # print the real part of the complex number   
print(e.imag) # print the imaginary part of the complex number


#list, tuple, set, dictionary
my_list = [1, 2, 3, 4, 5] # list is ordered and mutable
my_tuple = (1, 2, 3, 4, 5) # tuple is ordered and immutable
my_set = {1, 2, 3, 4, 5} # set is unordered and mutable not allow duplicate values
my_dict = {"name": "Sameer", "age": 20, "city": "Lucknow"} # dict is unordered and mutable
print(type(my_list))
print(type(my_tuple))               
print(type(my_set))
print(type(my_dict))

#none data type
f = None # none is a special data type that represents the absence of a value
print(type(f))
print(f)




# 3-Python variables


#variables in python are used to store data values. A variable is created when you assign a value to it. 
# The variable name must start with a letter or an underscore and can contain letters, numbers, and underscores.
# Variable names are case-sensitive. example: name and Name are two different variables. 
# 2ab is not a valid variable name because it starts with a number.
# _name is a valid variable name because it starts with an underscore.
name= "Sameer"
age = 20
print(name)
print(age)

#dynamic typing in python means that you can change the data type of a variable at runtime.
 

#static typing in python means that you cannot change the data type of a variable at runtime.
# In static typing, you need to declare the data type of a variable before using it.

#dynamic binding in python means that the variable is bound to the value at runtime.
# In dynamic binding, the variable can be bound to different values at different times during the execution
# means no fix data type for a variable in python. you can assign any data type to a variable and change it later.
x = 10 # x is an integer
print(x)
x = "Sameer" # x is now a string
print(x)


#declaration of multiple variables in a single line
a, b, c = 1, 2.5, "Hello"
print(a,b,c)

# we can also assign the same value to multiple variables in a single line
x = y = z = 10
print(x,y,z)


# COMMENTS IN PYTHON

# comments are used to explain the code and make it more readable.

# This is a single line comment 
#multi-line comments in python are created using triple quotes (""" """) or (''' ''')
"""This is a multi-line comment in python"""




# 4-Python keywords and identifiers

# keywords 
#there are 35 keywords in python that are reserved words and cannot be used as variable names, function names, or any other identifiers.
# keywords are reserved words in python that have a special meaning and cannot be used as variable names, function names, or any other identifiers.
# example of keywords in python: if, else, elif, for etc..


#identifiers 


# identifiers are names used to identify variables, functions, classes, modules, and other objects in python.

# rules for naming identifiers in python:  

# 1. An identifier must start with a letter (a-z, A-Z) or an underscore (_).
# 2. An identifier can only contain letters, digits (0-9), and underscores.
# 3. An identifier cannot be a keyword. 
# 4. An identifier cannot start with a digit.
# 5. An identifier cannot contain spaces.
# example of valid identifiers in python: name, age, _name, name1 etc..
# example of invalid identifiers in python: 1name, name!, name@ etc....


# User input in python
# input() function is used to take input from the user in python.
# input() function always returns a string value, so we need to convert it to the desired
# data type using type casting functions like int(), float(), str() etc..
input("apna naam bta bhai: ") # this will take input from the user and print it on the console
name = input("Enter your name: ")  
print(name)


# satic and dynamic typing in python

# static typing in python means that you cannot change the data type of a variable at runtime.
# In static typing, you need to declare the data type of a variable before using it.    
# dynamic typing in python means that you can change the data type of a variable at runtime.
# In dynamic typing, the variable can be bound to different values at different times during the execution




# implicit and explicit type conversion in python
# implicit type conversion in python is done automatically by the interpreter when it encounters an expression with different data types.
# example of implicit type conversion in python:
x = 10 # x is an integer
y = 20.5 # y is a float
z = x + y # z is a float (implicit type conversion)
print(z)


# explicit type conversion in python is done manually by the programmer using type casting functions like int(), float(), str() etc..
# example of explicit type conversion in python:
y = "20" # y is a string
z = int(y) # z is now an integer
print(z)


#some places implicit type conversion is not possible
# example of implicit type conversion not possible in python:
x = "10" # x is a string    
y = 20 # y is an integer
z = x + y # this will raise a TypeError because implicit type conversion is not possible between string and integer
print(z)

# type conversion make temporary change in the data type of a variable for a specific operation
# while type casting permanently changes the data type of a variable.


# type conversion in python is done using type casting functions like int(), float(), str() etc..
#example of type conversion in python:
x = 10 # x is an integer
y = float(x) # y is now a float
print(y)


#type casting in python is done using type casting functions like int(), float(), str() etc.. to convert a variable from one data type to another data type.
#example of type casting in python:
x = 10 # x is an integer
y = float(x) # y is now a float
print(y)

# how differ from type conversion and type casting in python?
# Type conversion and type casting are often used interchangeably, but technically:
# - Type conversion is a broader term that includes both implicit and explicit conversion.
# - Type casting is a more specific term that refers to explicit type conversion performed by the programmer.   



# literals in python are the values that are assigned to variables.
# example of literals in python: 10, 3.14, "Hello", True, None etc..

a= 0b1010 # binary literal (base 2)
b = 0o12 # octal literal (base 8)   
c = 0x1A # hexadecimal literal (base 16)
print(a) # 10 in decimal
print(b) # 10 in decimal
print(c) # 26 in decimal


# all types of literals in python

# 1. String literals: "Hello", 'World', """This is a string literal
# 2. Numeric literals: 10, 3.14, 2 + 3j
# 3. Boolean literals: True, False
# 4. None literal: None
