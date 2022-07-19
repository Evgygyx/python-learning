import random

random.randint(1,10)
print(random.randint(1,10))
print(random.random())

# Used random function
list = ['yes','no','maybe']
print(random.choice(list))

# Used indexes in list. There's a problem if length of the list changes
answer = random.randint(0,2)
print(list[answer])

# Used indexes in list. 2nd parameter of randint function dynamically changes range of indexes depends on of the list
answer = random.randint(0, len(list)-1)
print(list[answer])






