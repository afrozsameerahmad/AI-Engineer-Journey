# Sample String - I am Sameer Ahmad Currently Pursuing Master's in Data Science and AI from BBD University, Lucknow. 
# Expected output- no.of uppercase letters- 
# no.of lowercase letters-
s = "I am Sameer Ahmad Currently Pursuing Master's in Data Science and AI from BBD University, Lucknow."
def count_upper_lower(s):
    upper=0
    lower=0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper,lower
upper,lower = count_upper_lower(s)
print("no.of uppercase letters-",upper)
print("no.of lowercase letters-",lower)

