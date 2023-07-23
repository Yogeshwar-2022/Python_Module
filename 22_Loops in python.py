# While loop
i = 10
while i<20:
    print("yes "+ str(i))
    i = i+1 
# This will loop until the condition (i<10) is true ,
# if a condition is always true it will become a infinite loop
# for instance
        # i = 10
        # while i>=10:
        #     print("yes "+ str(i))
        #     i = i+1 

# quick quiz
i = 1
while i<51:
    print(str(i))
    i = i+1

i = 0
while i<5: 
    print('Arya')
    i = i+1

# quick quiz 01 
# printing contents of list
fruits = ["banana" , "mango" , "watermelon" ,"kiwi" ,"apple" ]
i = 0
while i<len(fruits):
    print(fruits[i])
    i=i+1

# For loop 
fruits = ["banana" , "mango" , "watermelon" ,"kiwi" ,"apple" ]
for fruit in fruits:
    print(fruit)

# Range 
for i in range(2, 8, 2): # (start , stop , step size)
    print(i)

# for loop with else 
for i in range(1,10):
    print(i)
else:
    print("for loop is now exhausted")

# break statement
for i in range(1,10):
    print(i)
    if i==5:
        break
else:                                 
    print("for loop is now exhausted")
    # Will not be executed since for was terminated before execution
    
# Continue statement
for i in range(1,10):
    if i==5:
        continue 
    print(i)        
else:                                 
    print("for loop is now exhausted")
    # Will be executed since for was not terminated before execution

# pass statements
for i in range(2, 8, 2): 
    pass
print("you have passed the for loop")
    