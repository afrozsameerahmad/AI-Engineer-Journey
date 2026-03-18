'''
print a (3x3) matrix using list comprehension.
'''
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
for row in matrix:
    print(row)