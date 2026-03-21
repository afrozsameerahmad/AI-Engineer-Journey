# Write a python function that accepts a hyphen separated sequence of words as parameter and returns 
# the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_hyp_sep_words(s):
    words = s.split('-')
    sorted_words = sorted(words)
    return '-'.join(sorted_words)   
input_string = "banana-apple-cherry-date"
result = sort_hyp_sep_words(input_string)  
print(result) 

# explaination:
# 1. The function `sort_hyp_sep_words` takes a string `s`
# 2. It splits the string into a list of words using the `split` method with '-' as the separator.
# 3. The list of words is then sorted alphabetically using the `sorted` function.
# 4. Finally, the sorted list of words is joined back into a hyphen-separated string using the `join` method and returned.
# 5. The input string "banana-apple-cherry-date" is passed to the function, 
# and the sorted result "apple-banana-cherry-date" is printed.        
