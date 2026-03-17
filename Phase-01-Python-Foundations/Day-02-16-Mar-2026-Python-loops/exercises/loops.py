'''
LOOPS IN PYTHON
In Python, loops are used to execute a block of code repeatedly until a certain condition is met.
There are two main types of loops in Python: 
1- for loops 
2- while loops.


Why we need loops?

exmaple :- Loop are used in different different software example in flipkart 
when you search something like you search samsung mobile  
and you will see all samsung mobile represented in same way like description ,images and price it repeat in same way again and again 
lets say 1000 time repeated  

if i ask you what difference in it and what simmilarities 
you could say different images dercription and price and same is  every mobile have same structure

if you are web developer of this page can you write 1000 time same code for every mobile
no you will write code once and use loop to repeat it 1000 time 
thats real example of loop in real life

'''


'''
1- While Loop
A while loop in Python repeatedly executes a block of code as long as a specified condition is true 
syntax of while loop
while condition:
    # code to be executed   
Example of while loop
i = 1
while i <= 5:
    print(i)
    i += 1
Output: 1 2 3 4 5


'''


'''
Print table of a number entered by the user using while loop
'''

num = int(input("Enter a number: "))
i = 1
while i<=10:
    print(num,"x",i,"=",num*i)
    i += 1
    

'''
While loop with else
'''
i = 1
while i <= 5:
    print(i)
    i += 1  
else:
    print("Loop has ended")
    
    
'''
FOR LOOP
A for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) 
and execute a block of code for each item in the sequence.
syntax of for loop
for variable in sequence:
    # code to be executed
Example of for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
Output: apple banana cherry

'''

for i in range(1, 6):# 1 is starting point and 6 is ending point but it will not include 6 it always run n-1 times
    print(i)
    
for i in range(1, 11,2):
    print(i)
    
    
'''
NESTED LOOPS
A nested loop is a loop that is contained within another loop.

'''
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
        
        

'''
Pattern Printing
*
**
***
****

'''
row = int(input("Enter the number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*", end="")
    print() # for new line
    
for i in range(row, 0, -1): # reverse order
    for j in range(1, i+1):
        print("*", end="")
    print()  
    
    
    
'''
1
121
12321
1234321
123454321


'''
row = int(input("Enter the number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j, end="")
    for k in range(i-1,0,-1):
        print(k, end="")
    print() 