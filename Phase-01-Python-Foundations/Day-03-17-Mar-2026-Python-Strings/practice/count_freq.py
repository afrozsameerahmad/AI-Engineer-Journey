'''
count the frequency of particuler character in a string

'''
s = input("Enter a string: ")
char = input("Enter the character to count: ")

count = 0
for c in s:
    if c == char:
        count += 1

print(f"Frequency of '{char}' in the string is: {count}")