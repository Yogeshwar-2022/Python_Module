# if, elif, else - ladder
a = input("An Integer :\n")
a = int(a)
b = "A is greater than 3"
c = "A is greater than 7"
d = "A is niether greater than 3 or 7"
if(a>3): 
    a = str(a)
    print(b.replace("A", a))
    a = int(a)
elif(a>7):
    a = str(a)
    print(c.replace("A",a))
    a = int(a)
else:
    a = str(a)
    print(d.replace("A",a))


# multiple if, elif, else - ladder
a = input("An Integer :\n")
a = int(a)
b = "A is greater than 3"
c = "A is greater than 7"
d = "A is niether greater than 3 or 7"

if(a>3): 
    a = str(a)
    print(b.replace("A", a))
    a = int(a)

if(a>7):
    a = str(a)
    print(c.replace("A",a))
    a = int(a)
else:
    a = str(a)
    print(d.replace("A",a))


#18+ age code (quick quiz)
a = int(input("enter your age :\n"))

if (a>18):
    print("age verification complete")
else:
    print("you are not allowed to enter this site")