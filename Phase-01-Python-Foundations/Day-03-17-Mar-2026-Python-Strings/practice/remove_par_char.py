'''
Write a Python program that takes a string and a character as input and removes all occurrences of that character from the string.'''


s = input("Enter a string: ") 
char = input("Enter the character to remove: ")
result = ''
for c in s:
    if c != char:
        result += c     
print("String after removing the character:", result)