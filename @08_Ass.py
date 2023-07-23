# PR01

# with open('Poems.txt') as f :
#     t = f.read()
#     if 'twinkle' in t:
#         print('twinkle is present') 
#     else :
#         print('twinkle is absent')


# PR02

# def game():
#     a = int(input('Your Score : '))
#     return a

# Score = game()

# with open ('HighScore.txt') as f :
#     High_Score = f.read()

# if High_Score == '':
#     with open('HighScore.txt','w') as f:
#         f.write(str(Score))
# elif Score>High_Score :
#     with open('HighScore.txt','w') as f:
#         f.write(str(Score))

# PR03

# for i in range (2,21):
#     with open (f"Tables/Multiplication Table Of {i}.txt", 'w') as f:
#         for j in range (1,11):
#             f.write(f'{i} X {j} = {i*j}\n')

# PR04/05

# words = ['fuck','Fuck','mum','Mum','Shit','shit']
# with open('Sample.txt') as f :
#     content = f.read()

# for word in words:
#     content = content.replace(word,'****')
#     with open('Sample.txt','w') as f :
#         f.write(content)

# PR06/07

# content = True
# i=1
# with open('log.txt') as f :
#     while content:
        
#         content = f.readline()
#         # print(content)

#         if 'python' in content.lower() :
#             # print(content)
#             print(f'Python is present on line number {i}')
#         i+=1

# PR08

# with open('this.txt') as f :
#     content = f.read()

# with open('Copythis.txt','w') as f:
#     f.write(content)

# PR09

# file = 'this.txt'
# file2 = 'Copythis.txt'

# with open('this.txt') as f :
#     f1 = f.read()

# with open('Copythis.txt') as g :
#     f2 = g.read()

# if f1 == f2 :
#     print("the files are identical")
# else :
#     print("they aren't identical")

# PR10

# with open('Sample.txt','w') as g :
#     g.write('')

# PR11

# import os 

# New_Name = input("New name : ")
# OldName  = input("Actual file name : ")

# with open(OldName) as f :
#     content = f.read()

# with open(New_Name,'w') as f:
#     f.write(content)

# os.remove(OldName)


