# Write a python program that takes a list as input and returns a new list with only unique elements from the original list.
l = [1, 2,3,3,3,3,4,5,5,6,7,8,9,9]
def unq_elm(l):
    unq_l = []
    for i in l:
        if i not in unq_l:
            unq_l.append(i)
    return unq_l    
print(unq_elm(l))