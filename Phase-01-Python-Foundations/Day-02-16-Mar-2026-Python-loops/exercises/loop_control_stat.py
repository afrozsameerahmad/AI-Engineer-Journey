'''
Loop Control Statements
Loop control statements are used to control the flow of a loop.
There are three types of loop control statements in Python:
1- break
2- continue
3- pass


1- break statement
The break statement is used to exit a loop prematurely when a certain condition is met. 
When the break statement is executed, the loop is terminated immediately, and the program continues with the next statement after the loop.

2- continue statement
The continue statement is used to skip the current iteration of a loop and move to the next iteration
When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped,
and the loop proceeds to the next iteration.

3- pass statement
The pass statement is a null statement in Python. It is used as a placeholder when a statement
is syntactically required but you do not want to execute any code. 
When the pass statement is executed, it does nothing and the program continues with the next statement.

'''



'''
Example of break statement

'''
for i in range(1, 11):
    if i == 4:
        break
    print(i)
#Output: 1 2 3


'''
Example of continue statement
'''
for i in range(1, 11):
    if i == 4:
        continue
    print(i)
#Output: 1 2 3 5 6 7 8 9 10

'''

Example of pass statement

'''
for i in range(1, 11):
    if i == 4:
        pass
    print(i)
#Output: 1 2 3 4 5 6 7 8 9 10


lower = int(input("Enter a lower number: "))
upper = int(input("Enter an upper number: "))
for i in range(lower, upper + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)