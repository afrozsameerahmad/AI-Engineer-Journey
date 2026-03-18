'''
Print the Cartesian product of two sets using list comprehension.

'''

set1 = [1, 2, 3]
set2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in set1 for y in set2]
print(cartesian_product)
