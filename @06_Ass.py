# # PR01 (f string)
# Num = int(input("Enter the number you want a multiplication table for :\n"))
# for Table in range(1,11):
#     # print(str(Num) + " X " + str(Table) + " = " + str(Num*Table))
#     print(f"{Num} X {Table} = {Num*Table}")

# # PR02
# Names = ["Arya" , "Sohan" , "Sachin" , "Rahul"]
# for Name in Names:
#     if Name.startswith("S"):
#         print(f"Hello {Name}")

# # PR04
# Num = int(input("Enter a number to check weather its prime or not :\n"))
# prime = True

# for I in range(2,Num):
#     if Num % I == 0 and Num != 2 :
#         prime = False
#         break

# if prime :
#     print(f"{str(Num)} is a prime number")
# else:
#     print(f"{str(Num)} is not a prime number")

# # PR06
# Num = int(input("Enter a number you want to find ! of :\n"))
# factorial = 1
# for I in range(1 , Num+1):
#     factorial = factorial * I 
#     # Value of variable factorial is changing when multiplied with I 

# print(f"factorial of {Num} is {factorial}")

# # PR07
# Sym = input("input object you want pattern of:\n" )
# NR = int(input(f"Input number of rows of {Sym} pattern :\n"))
# for I in range(NR+1):
#     print(f"{Sym}"*I)

# # PR08
# Sym = input("input object you want pattern of:\n" )
# NR = int(input(f"Input number of rows of {Sym} pattern :\n"))
# for I in range(NR):
#     print(" "*(NR-I-1), end="")
#     print(f"{Sym}"*(2*I+1), end="")
#     print(" "*(NR-I-1))

# Sym = input("input object you want pattern of:\n" )
# NR = int(input(f"Input number of rows of {Sym} pattern :\n"))
# for I in range(NR):
#     print(" "*(NR-I-1) + f"{Sym}"*(2*I+1) + " "*(NR-I-1))

# # PR03
Num = int(input("Enter the number you want a multiplication table for :\n"))
Table = 1
while Table<=10:
    print(f"{Num} X {Table} = {Num*Table}")
    Table = Table + 1

# # PR09
# Sym = input("input object you want pattern of:\n" )
# NR = int(input(f"Input number of rows of {Sym} pattern :\n"))
# print(f"{Sym*NR}")
# for I in range(NR-2):
#     print(Sym+" "*(NR-2)+Sym)
# print(f"{Sym*NR}")

# # PR10
# Num = int(input("Enter the number you want a reverse multiplication table for :\n"))
# Table = 10
# while Table>0:
#     print(f"{Num} X {Table} = {Num*Table}")
#     Table = Table - 1 

# # PR05
Num = int(input("Enter the number :\n"))


