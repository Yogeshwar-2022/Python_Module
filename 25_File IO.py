# Use open function to read the file 
# if mode is not mentioned it assumes r 

f = open('Sample.txt','r')
# data = f.read()
data = f.read(6) #reads first 6 characters in file 
print(data)
f.close()

f = open('Sample.txt','r')
data = f.readline()#reads first line 
print(data)
data = f.readline()#reads second line....and so on
print(data)
f.close()

f = open('Sample.txt','rb')
data = f.read() #reads in binary mode 
print(data)
f.close()

# Modes of opening a file

# r – open for reading

# w – open for writing

# a – open for appending

# + -> open for updating

# ‘rb’ will open for read in binary mode

# ‘rt’ will open for read in text mode

f = open('NewSample.txt','w')
f.write('NewSample file is being created by above command')
f.close()
f = open('NewSample.txt','a')
f.write('\nI am appending')
f.write('\nYour mum')
f.close()

with open('Sample.txt','r') as f:
    a = f.read()
    print(a)

# With statement
# The best way to open and close the file automatically is the “with” statement.
# There is no need to write f.close() as it is done automatically

