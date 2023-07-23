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

print(type(myDict))

print(myDict["Lexis"])
print(myDict["L1"])
print(myDict[1])

print(myDict['''L1'''][3])
print(myDict['T1'][0])

print(myDict['''nestedDict1'''])
print(myDict['''nestedDict1''']["pix"])

myDict['''L1'''] = [5,25,50]
print(myDict["L1"])