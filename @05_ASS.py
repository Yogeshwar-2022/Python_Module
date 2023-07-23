# # PR01
# a = int(input("give me number1 :\n"))
# b = int(input("give me number2 :\n"))
# c = int(input("give me number3 :\n"))
# d = int(input("give me number4 :\n"))
# if a>b and a>c and a>d:
#     a = str(a)
#     A = "a is the greatest number"
#     print(A.replace("a", a))
#     a = int(a)
# elif b>a and b>c and b>d:
#     b = str(b)
#     A = "b is the greatest number"
#     print(A.replace("b", b))
#     b = int(b)
# elif c>b and c>a and c>d:
#     c = str(c)
#     A = "c is the greatest number"
#     print(A.replace("c", c))
#     c = int(c)
# elif d>b and d>a and d>b:
#     d = str(d)
#     A = "d is the greatest number"
#     print(A.replace("d", d))

# # PR01,01
# a = int(input("give me number1 :\n"))
# b = int(input("give me number2 :\n"))
# c = int(input("give me number3 :\n"))
# d = int(input("give me number4 :\n"))
# if a>d:
#     F1 = a
# else:
#     F1 = d

# if b>c:
#     F2 = b
# else:
#     F2 = c

# if F1>F2:
#     A = "F1 is greatest number"
#     F1 = str(F1)
#     print(A.replace("F1",F1))
# else:
#     A = "F2 is greatest number"
#     F2 = str(F2)
#     print(A.replace("F2",F2))   

# PR02 
# A = input("students's name :\n")

# S1 = input("\nSub1 name :\n")
# S2 = input("Sub2 name :\n") 
# S3 = input("Sub3 name :\n")

# p = "\n% marks in sub1 :\n"
# p = p.replace("sub1",S1)
# q = "% marks in sub2 :\n"
# q = q.replace("sub2",S2)
# r = "% marks in sub3 :\n"
# r = r.replace("sub3",S3)

# Sub1 = input(p)
# Sub1 = int(Sub1)
# Sub2 = input(q)
# Sub2 = int(Sub2)
# Sub3 = input(r)
# Sub3 = int(Sub3)

# if Sub1>33 and Sub1<=100 and Sub2<=100 and Sub3<=100 :
#     a = "\nA has passed in sub1"
#     a = a.replace("A",A)
#     print(a.replace("sub1",S1))
# elif Sub1>100:
#     X = "\nPLEASE ENTER % MARKS OF STUDENT IN SUB1"
#     print(X.replace("SUB1",S1))
# else:
#     a = "\nA has failed in sub1"
#     a = a.replace("A",A)
#     print(a.replace("sub1",S1))
    
# if Sub2>33 and Sub2<=100 and Sub1<=100 and Sub3<=100:
#     b = "A has passed in sub2"
#     b = b.replace("A",A)
#     print(b.replace("sub2",S2))
# elif Sub1>100:
#     X = "\nPLEASE ENTER % MARKS OF STUDENT IN SUB1"
#     print(X.replace("SUB1",S1))
# elif Sub2>100:
#     Y = "PLEASE ENTER % MARKS OF STUDENT IN SUB2"
#     print(Y.replace("SUB2",S2))
# else:
#     b = "A has failed in sub2"
#     b = b.replace("A",A)
#     print(b.replace("sub2",S2))

# if Sub3>33 and Sub3<=100 and Sub2<=100 and Sub1<=100 :
#     c = "A has passed in sub3"
#     c = c.replace("A",A)
#     print(c.replace("sub3",S3))
# elif Sub1>100:
#     X = "\nPLEASE ENTER % MARKS OF STUDENT IN SUB1"
#     print(X.replace("SUB1",S1))
# elif Sub2>100:
#     Y = "PLEASE ENTER % MARKS OF STUDENT IN SUB2"
#     print(Y.replace("SUB2",S2))
# elif Sub3>100:
#     Z = "PLEASE ENTER % MARKS OF STUDENT IN SUB3"
#     print(Z.replace("SUB3",S3))
# else:
#     c = "A has failed in sub3"
#     c = c.replace("A",A)
#     print(c.replace("sub3",S3))

# if (Sub1+Sub2+Sub3)>120 and (Sub1+Sub2+Sub3)<=300 and Sub1<100 and Sub2<100 and Sub3<100 :
#     d = "\nA has passed"
#     print(d.replace('A',A))
# elif Sub1>100 or Sub2>100 or Sub3>100 or (Sub1+Sub2+Sub3)>300:
#     print("\nPLEASE ENTER % MARKS OF STUDENT")
# else:
#     d = "\nA has failed"
#     print(d.replace("A",A))

#PR02
# Sub1 = int(input("input marks % for subject1 :\n"))
# Sub2 = int(input("input marks % for subject2 :\n"))
# Sub3 = int(input("input marks % for subject3 :\n"))
# if Sub1<33 or Sub2<33 or Sub3<33:
#     print("you have failed because you have less than 33% in one of the subject ")
# elif (Sub2+Sub2+Sub3)/3>40:
#     print("you passed with flying colors")
# else:
#     print("you have failed due to less aggregate than 40%")

# PR04
# Comment = input("Comment:\n")
# if ('make a lot of money' in Comment):
#     Spam = True

# if ('click this' in Comment):
#     Spam = True

# if ('subscribe this' in Comment):
#     Spam = True
# else:
#     Spam = False

# if(Spam):
#     print("this comment was deleted")
# else:
#     print(Comment)

# PR05
# Username = input("Username :\n")
# A = int(len(Username))
# if A>10 :
#     print("Too long")
# else:
#     print("Username : "+Username )

# PR06
# Names = ['Luna Rush','Caitlyn Rowland','Davis Dyer','Anderson Vincent','Daisy Tanner']
# Name = input("Enter name you want to find in the list :\n")
# if Name in Names :
#     print("given name is present in the list")
# else:
#     print('given name is not present in the list')

# PR07
# Marks = int(input("Enter your marks:\n"))
# print("\nYour Grade is:")
# if Marks>=90 and Marks<=100:
#     print("Ex")
# elif Marks>=80:
#     print("A")
# elif Marks>=70:
#     print("B")
# elif Marks>=60:
#     print("C")
# elif Marks>=50:
#     print("D")
# elif Marks>=40:
#     print("E")
# else:
#     print("Fail")

# PR08
# Post = input("Your Post:\n")
# if "Harry" in Post or "HARRY" in Post :
#     Harry = True
# else:
#     Harry = False

# if Harry is True:
#     print("Post tagged as Harry")
# else:
#     print("No tags assigned")
