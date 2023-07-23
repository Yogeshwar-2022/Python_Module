myDict = {
    "Lexis": "all the words of a language",
    "path": "a route or track",
    '''L1''': ["Apples",3.14,5,True,None],
    'T1': (22,"Arya"),
    'nestedDict1': { "pix" : "pictures",
                     "pixie" : "a small imaginary person"
                    },
    1: 2
         }

# Dictionary methods 
print(myDict.keys())
print(type(myDict.keys()))

print(myDict.values())
print(type(myDict.values()))

print(myDict.items())
print(type(myDict.items()))
print(myDict['nestedDict1'].items())
print(type(myDict.items()))

UpdateDict = {'Lovely': "billie ellish",
              '''Let Me Love You''': "Dj Snake"}
myDict.update(UpdateDict)
print(myDict)

# *** VVIP ***
print(myDict.get(1))
print(myDict[1])
'''BUT'''
print(myDict.get(0))   # Prints none 
print(myDict[0])       # Throws an error 
# Hence both commands are diffrent


# Typecasting

# print(list(myDict.keys()))
# D = list(myDict.keys())
# print(type(D))

# print(list(myDict.values()))
# E = list(myDict.values())
# print(type(E))

# print(list(myDict.items()))
# F = list(myDict.items())
# print(type(F))
