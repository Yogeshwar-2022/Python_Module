Name = "Arya"
Greeting = "Sup, "

#Concatenating
print(Greeting + Name)
A = Greeting + Name
print(type(A)) 

#Str Slicing 
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])

print(Name[-4])
print(Name[-3])
print(Name[-2])
print(Name[-1])

print(Name[0:1])
print(Name[0:2])
print(Name[0:3])
print(Name[1:2])
print(Name[1:3])

print(Name[:3]) # Same as 0:3
print(Name[1:]) # Same as 1:3

print(Name[-3:-1]) # Same as 1:3
print(Name[-4:-1]) # Same as 1:4

# Slicing with skip value 
Name = "Beatrice"
print(Name[0:9])
print(Name[0::2])
