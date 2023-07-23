B = set()

# adding value to a set
B.add("Aryan")
print(B)
B.add(False)
print(B)

B.add("Aryan")
print(B)

B.add((2,3,5)) #Tuple
print(B)

# Finding length of set 
print(len(B))

# # removes value from set
# B.remove("Aryan")
# print(B)

# # Remove arbitrary value from set and return it
# print(B.pop())
# print(B)

# # Emptying the set
# B.clear()
# print(B)

# Union of sets 
C = {4,None,3.0}
print(B.union(C))

# Intersection of sets
print(B.intersection(C))
C.add('''Aryan''')
print(B.intersection(C))

