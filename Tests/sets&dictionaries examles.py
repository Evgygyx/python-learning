import pandas as pd

# initializing a set
set1 = {'A', 'B', 'C', 'D', 'E'}
ABCDE = ""
my_string = "ABCDE"
# initializing a dictionary
dictionary = {'A': [1], 'B': [2], 'C': [3], 'D': [4], 'E': [5]}
print(dictionary)

# using list() to create a list
list1 = list(set1)
list2 = list(dictionary)

# printing
print(list1)
print(list2)

df = pd.DataFrame(dictionary)
