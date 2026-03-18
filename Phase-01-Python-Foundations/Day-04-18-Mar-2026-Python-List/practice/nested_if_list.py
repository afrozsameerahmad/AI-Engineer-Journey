'''
Print all fruits that are in the basket and start with the letter 'a' using list comprehension
'''



basket=['apple', 'banana', 'orange', 'grape', 'kiwi']
my_fruit=['apple', 'banana', 'orange','pineapple','avocado']
print([fruit for fruit in my_fruit if fruit in basket and fruit.startswith('a')])