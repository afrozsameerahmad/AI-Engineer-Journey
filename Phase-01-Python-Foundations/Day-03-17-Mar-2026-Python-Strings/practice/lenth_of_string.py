'''
Find the length of a string without using the built-in len() function.
'''


s = input("Enter a string: ")

count=0
for i in s:
    count+=1
print("Length of the string is:", count)
