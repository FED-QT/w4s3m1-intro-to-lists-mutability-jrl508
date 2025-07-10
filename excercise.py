# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

# Part 1 answer:
'''
 id(a) changed because integers are immutable so 
 adding to a would reassign it to another position in memory

 x is a list and is a mutable object therefor it does not require reassignment
 
 This showcases what kind of behavior to expect when working with variables and lists,
 especially in the case that b remained the same after a was 'changed' but y changed with x.

 '''

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    upper_names.append(n.upper())

# Task B: enumerate over upper_names
for idx, name in enumerate(upper_names, start=1):
       # your code here
       print(f'{idx}. {name}')

# Task C: demo two list methods
# 1. insert
names.insert(2,'ricardo')
print(names)
# 2. remove
names.remove('charlie')
print(names)
# 3. sort
names.sort()
print(names)