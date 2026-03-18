
'''

Print all programming languages that contain the letter 'P' using list comprehension.

'''

languages=['Python', 'Java', 'C++', 'JavaScript', 'PHP', 'Ruby', 'Swift', 'Go', 'Kotlin', 'Rust']

print([languages for languages  in languages if languages.startswith('P')])