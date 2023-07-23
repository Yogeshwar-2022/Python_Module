# funtion
def average(Marks):
    average = (int(sum(Marks))/len(Marks))
    return average

Marks1 = [22,23,43,60]
average1 = average(Marks1)
print(average1)

Marks2 = [22,27,49,70]
average2 = average(Marks2)
print(average2)

# quick quiz
def greetings(Name): # User defined function
    greetings = print(f"good morning ,{Name}") # built in function
    return greetings
Name1 = input("Enter username :\n")
greetings(Name1)



def greeting(Name = "Stranger"): # Assigning Default Paramter Value
    greeting = print(f"good morning ,{Name}") 
    return greeting

greeting()
