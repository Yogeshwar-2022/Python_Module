# PR01

class Programmer :
    company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self) :
        print(f"The name of company {self.company}")
        print(f"The name of programmer is {self.name}")
        print(f"The name of product is {self.product}")

harry = Programmer("Harry","Skype")
alka = Programmer('alka','GitHub')

harry.getInfo()
alka.getInfo()

# PR02

import math 
class calculator :
    def __init__(self,num) :
        self.number = num
    def square(self) :
        print(f"The square of {self.number} is {self.number **2}")
    def cube(self) :
        print(f"The cube of {self.number} is {self.number **3}")
    def square_root(self) :
        print(f"The square root of {self.number} is {math.sqrt(self.number)}")

num1 = float(input("Give number you want square cube and squrearoot of : ")) 
a = calculator(num1)
a.square()
a.cube()
a.square_root()

# PR03

class sample :
    a = 'Arya'

obj = sample()
obj.a = 0
print(sample.a)
print(obj.a)

# PR04

class calculator :
    def __init__(self,num) :
        self.number = num
    def square(self) :
        print(f"The square of {self.number} is {self.number **2}")
    def cube(self) :
        print(f"The cube of {self.number} is {self.number **3}")
    def square_root(self) :
        print(f"The square root of {self.number} is {math.sqrt(self.number)}")
    @staticmethod
    def greet():
        print("Hello There Welcome , This is calculator ")

num1 = float(input("Give number you want square cube and squrearoot of : ")) 
a = calculator(num1)
a.greet()
a.square()
a.cube()
a.square_root()

# PR05

class Train :

    def __init__(self,name,fare,seats) :
        self.name = name 
        self.fare = fare 
        self.seats = seats

    def getStatus(self):
        print(f"name of the train is {self.name}")
        print(f"seats available on the train are {self.seats}")

    def fareInfo(self):
        print(f"The Price of the ticket is : Rs. {self.fare}")

    def bookTicket(self):
            if self.seats > 0:
                print(f"Your ticket has been booked your seat number is : {self.seats}")
                self.seats = self.seats -1 
            else :
                print ("Sorry this train is full please try in Tatkal")
    
    def cancelTicket(self,seat_number):
        pass


intercity = Train("Intercity Express : 14015", 90 , 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()

# PR06

class sample :
    def __init__(slf, name) :
        slf.name = name

obj = sample("Harry")
print(obj.name)


