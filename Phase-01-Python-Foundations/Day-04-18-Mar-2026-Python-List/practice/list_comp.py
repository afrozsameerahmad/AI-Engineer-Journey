# Add 1 to 10 numbers using list comprehension
l=[]
for i in range(1,11):
    l.append(i)
print(l)
# this is the traditional way to create a list of numbers from 1 to 10 and add them to a list using a for loop and append method

#using list comprehension
l=[i for i in range(1,11)]
print(l)