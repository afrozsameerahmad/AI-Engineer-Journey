l=[1,2,3,[4,5]]

# we need to access 4 from this list 

print(l[3])
# it will give us [4,5] because it is a list inside a list and we need to access 4 from this list we need to do 
print(l[3][0])  # output: 4

# aslo we can access by using negative indexing
print(l[-1][-2])  # output: 4
# -1 means last item which is [4,5] and -2 means second last item which is 4 its concept of nested list 
#  and we can access items from nested list by using multiple indexing.





l1=[[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
# we need to acees 6 from this list 
print(l1[1]) # output: [[5, 6], [7, 8]] because it is a list inside a list and we need to access 6 from this list we need to do
print(l1[1][0]) # output: [5, 6] because it is a list inside a list and we need to access 6 from this list we need to do
print(l1[1][0][1]) # output: 6 because it is a list inside a list and we need to access 6 from this list we need to do this



# SLICING

l=[1,2,3,4,5]
print(l[1:4])  # output: [2, 3, 4] it start from  and fetch items n-1 last index is not included
print(l[:3])   # output: [1, 2, 3]
print(l[2:5])  # output: [3, 4, 5]
print(l[0:5:2])  # output: [1, 3, 5] it fetches every second item from the list

# in slicing we have three parameters start, stop and step
# start is the index from which we want to start slicing, stop is the index at which
# we want to stop slicing and step is the number of items we want to skip while slicing