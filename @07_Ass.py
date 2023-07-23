#PR01
# def maximum(num1,num2,num3):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3

# A = float(input("NUM1 = "))
# B = float(input("NUM2 = "))
# C = float(input("NUM3 = "))

# M = maximum(A,B,C)
# print(f"{M} is gresteat of all")

# PR02
# def CelToFahren(Cel):
#     Cel = float(Cel) 
#     Fahren = (Cel*(9/5)) + 32 
#     return Fahren

# Temp = input("tempreture in celcius :\n")
# print(str(CelToFahren(Temp)) + " Deg.Fahrenheit")

#PR03
# print("Hello ,", end =" <Exhale>")
# print(" Can you hear me .", end =" <Inhale>")
# print(" I was wondering to afterall these years you'd like meet", end ="\n<Verse2>\n")
# print("To Go Over ,", end =" <Exhale>")
# print(" Everything")

#PR04
# Sym = "null"
# NR = "null"
# def Pattern(Sym,NR):
#     for I in range(NR):
#         print(" "*(NR-I-1), end="")
#         print(f"{Sym}"*(2*I+1), end="")
#         print(" "*(NR-I-1))
#     return 

# Character = input("input a character you want pattern for = ")
# Rows = int(input("input number of rows for pattern = "))
# Pattern(Character,Rows)

#PR05
# A = "       you are my friend          "
# print(A)
# print(A.strip())

# def Remove_And_Strip(String,Word):
#     New_String = String.replace(Word,"")
#     return New_String.strip()

# B = input("Paste Your Sting : ")
# C = input("Paste Word you want to remove from string : ")
# print(Remove_And_Strip(B,C))

#PR06
# def InchesToCms(In):
#     In = float(In) 
#     Cm = In/2.54
#     return Cm

# I = input("input length in inches :\n")
# print(str(InchesToCms(I)) + " CentiMeters")

# PR07
# def TABLE(Num):
#     Table = 1
#     while Table<=10:
#         print(f"{Num} X {Table} = {Num*Table}")
#         Table = Table + 1
#     return

# N = int(input("Integer you want table for :\n"))
# TABLE(N)

# PR08
