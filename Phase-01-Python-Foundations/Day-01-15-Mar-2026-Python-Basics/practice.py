# DATA TYPES PRACTICE PROBLEMS


#  1

# take input from the user and store them  in a variable
# add the 2 variables
# print the result

# take input from the user and store them  in a variable
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")   
# add the 2 variables
result = num1 + num2
# print the result
print(result)

#the output will be the concatenation of the two strings because the input() function returns a string value.
#example: if the user enters 5 and 10, the output will be 510 instead of 15 because the input() function returns a string value.

# for adding the two numbers, we need to convert the input values to integers using the int() function.
num1 = int(input("Enter the first number: "))   
num2 = int(input("Enter the second number: "))
result = num1 + num2
print(result)



# 2 

#Write a program that prints your name, age, and city on the screen.
name = "Sameer Ahmad"
age = 21
city = "Lucknow"
print("Name:", name)
print("Age:", age)
print("City:", city)

# 3 - Take a user's name as input and print a welcome message.
name = input("Enter your name :")
print(f"Welcome,{name}")


#4 - Print the data type of the following values:10  ,3.14 ,"Python" ,True
print(type(10)) # int
print(type(3.14)) # float
print(type("Python")) # str
print(type(True)) # bool

# 5 - Create variables of the following data types:
# int, float, str, bool, list, tuple, set, dictionary, none print the data type of each variable.
int_var = 10
float_var = 3.14
str_var = "Python"
bool_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {7, 8, 9}
dict_var = {"a": 1, "b": 2}
none_var = None

print(type(int_var)) # int
print(type(float_var)) # float
print(type(str_var)) # str
print(type(bool_var)) # bool
print(type(list_var)) # list
print(type(tuple_var)) # tuple
print(type(set_var)) # set
print(type(dict_var)) # dict
print(type(none_var)) # NoneType

#6 -Create a complex number and print its: real part, imaginary part, and data type.
num = 2 + 3j
print("Real part:", num.real) # real part
print("Imaginary part:", num.imag) # imaginary part
print("Data type:", type(num)) # data type






# Variables & Identifiers Practice Problems

# 1 - Create variables for: student's name, age, and grade. Print the variables.
studen_name="Sameer Ahmad"
student_age=21
student_grade="A"
print("Student Name:", studen_name) 
print("Student Age:", student_age)
print("Student Grade:", student_grade)


# 2 - Assign multiple variables in one line and print them.
name,age,city= "Sameer",21,"Lucknow"
print("Name:", name)    
print("Age:", age)
print("City:", city)

# 3-   Assign same value to multiple variables and print them.
x=y=z=10
print("x:", x)
print("y:", y)  
print("z:", z)

# 4- Change the value of a variable from integer to string and print it.
num = 10 
print("Before changing the value:", num) # Before changing the value
num = "Ten"
print("After changing the value:", num) # After changing the value

# 5 - Create three valid identifiers and three invalid identifiers.
# Valid identifiers
name = "Sameer"
age = 21
city = "Lucknow"
# Invalid identifiers
# 1. 2name = "Sameer" # starts with a number
# 2. my-name = "Sameer" # contains a hyphen
# 3. my name = "Sameer" # contains a space


# Input / Output Practice Problems

#1 - Take user's name and age as input and print: My name is ____ and I am ____ years old.
name = input("Enter your name : ")
age = input("Enter your  age :")
print(f"My name is {name} and i am {age} years of old" )

# 2 - Take two numbers from the user and print: addition, subtraction, multiplication, and division of the two numbers.
num1= float(input("Enter the first number:"))
num2= float(input("Enter the second number:"))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# 3- Take a number as input and print its square.
num = float(input("Enter a number: "))
print("Square:", num ** 2)

# 4- Take input as a string "50" and convert it into integer.
num_str = "50"
num_int = int(num_str)
print("String:", num_str)
print("Integer:", num_int)



# Type Conversion Practice Problems

# 1 -Add an integer and float and print the result.
int_num = 10
float_num = 3.14
result = int_num + float_num
print("Result:", result)
print("Data type of result:", type(result)) 
# the result will be a float because when we add an integer and a float, the result is promoted to a float.

# 2- Convert the following values: integer to float, float to integer, string to integer, and integer to string.
# Integer to float
int_num = 10
float_num = float(int_num)
print("Integer:", int_num)
print("Float:", float_num)
# Float to integer
float_num = 3.14
int_num = int(float_num)
print("Float:", float_num)
print("Integer:", int_num)
# String to integer
str_num = "50"
int_num = int(str_num)
print("String:", str_num)
print("Integer:", int_num)
# Integer to string
int_num = 10
str_num = str(int_num)
print("Integer:", int_num)
print("String:", str_num)


# Logical Operators Practice Problems

# 1- Print binary, octal, and hexadecimal form of a number.
a= 0b1010 # 10 in binary
b= 0o12 # 10 in octal
c= 0x1A # 26 in hexadecimal

print(a,b,c)


#2 - Create a variable storing your favorite programming language and print its type.
fav_lang = "Python"
print("Favorite Programming Language:", fav_lang)
print("Data type:", type(fav_lang))


# 3-Print a message using multiple print arguments.
name = "Sameer"
age = 21
print(f"My name is {name} and I am {age} years old.")

# 4 Take user input and print it in uppercase.
name=input("Enter your name ")
print(name.upper())

# 5- Reverse a string given by the user.
name=input("Enter your name ")
print(name[::-1]) 
# the [::-1] slicing technique is used to reverse the string. 
# It starts from the end of the string and moves towards the beginning



# Mini Logic

 # 1- Take three numbers as input and print their average.
num1=(int(input("Enter your fisrt number :")))
num2=(int(input("Enter your second number :")))
num3=(int(input("Enter your third number :")))

result = num1 + num2 + num3
result = result / 3
print("The average is :", result)


# 2- Take a number and print: square, cube, and square root of the number.
num=(int(input("Enter your number :"))) 
print("Square:", num ** 2)
print("Cube:", num ** 3)    
print("Square Root:", num ** 0.5)


# 3- Swap two numbers using a third variable.
a=(int(input("Enter the first number :")))
b=(int(input("Enter the second number :")))
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)

