# A = 12 
# B = 34

class Number : # Blue print to create object written in PascalCase
    def sum(self):
        return self.a + self.b 

num = Number() # Object Instatiation
num.a = 12 
num.b =34
s = num.sum()
print(s)

# PascalCase 
# camelCase

class RailwayForm :
    formType = 'RailwayForm'
    def printData(self):
        print(f'Name is self.{self.name}')
        print(f'Name is self.{self.train}')

harrysApplication = RailwayForm()
harrysApplication.name = 'Harry' 
harrysApplication.train = 'Rajdhani Express'
harrysApplication.printData()

# Game 

# class Remote:
#     pass

# class Player :
#     def moveright(self):
#         pass
#     def moveleft(self):
#         pass
#     def moveup(self):
#         pass 
#     def movedown(self):
#         pass

# remote1 = Remote()
# player1 = Player()

# if(remote1.isLeftPressed()):
#     player1.moveleft()

# Employee

class Employee :
    company = "Google"

harry = Employee()
rajni = Employee()
harry.salary = "300K"
rajni.salary = "300K"

print(harry.company)

Employee.company = "Yotube"

print(harry.company)
print(harry.salary)

# insatance class attribites 

class Employee :
    company = "Google"
    salary = "100"

harry = Employee()
rajni = Employee()
harry.salary = "300K" #creating instance attributes for salary , it is preffered 
rajni.salary = "300K"

print(harry.salary)

# Self - you can call any both instance attributes and attributed defined in class

class Employee :
    company= "Google"
    def getsalary(self): #if self isnt written it throws error as getsalary() it takes 0 positional arguments but 1 was given
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    def greeting(self) :
        print
        
        
harry = Employee()
harry.salary = 100 
harry.getsalary() # Empoyee.getsalary(harry) - same command

# Static Method

class Employee :
    company= "Google"
    def getsalary(self,signature ): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod #the code is not converted due to following syntax
    def greeting() :# adding self is important because 
        print("Good Moning ,Sir")

    @staticmethod 
    def time():
        print("The Time Is 9 AM in the morning")

harry = Employee()
harry.salary = 100000
harry.getsalary("Thanks!")
harry.greeting()
harry.time

# Constructor

class Employee :
    company= "Google"

    def __init__(self , name , salary , subunit ):
        self.name = name 
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getsalary(self,signature ): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod #the code is not converted due to following syntax
    def greeting() :# adding self is important because 
        print("Good Moning ,Sir")

    @staticmethod 
    def time():
        print("The Time Is 9 AM in the morning")

harry = Employee('Harry',1000,'YouTube')
# harry = Employee() # --> this throws an error required arguments shall be given 
harry.getdetails()


