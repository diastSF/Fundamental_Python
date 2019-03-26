print('\n---QUESTION 1---\n')

# Level 1
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

num = []
for a in range(2000,3201):
    if a%7 == 0 and a%5 > 0:
        num.append(str(a))
for b in num:
    print(b, end=',')

print('\n---QUESTION 2---\n')

# Level 1
# Question: Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 
# Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
numb = int(input())
print(fact(numb))

# num = int(input('masukkan angka: '))
# fact = []
# for a in range(num):
#     fact.append(num-a)
# x = 1
# for b in fact:
#     x *= b
# print(x)

print('\n---QUESTION 3---\n')

# Level 1
# Question:

# With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included) 
# and then the program should print the dictionary.

# Suppose the following input is supplied to the program: 8

# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# In case of input data being supplied to the question, 
# it should be assumed to be a console input. Consider use dict()

num = int(input('Masukkan Angka : '))

theDict = {}

for i in range(num):
    theDict[i+1] = (i+1)**2
    
print(theDict)


print('\n---QUESTION 4---\n')

# Level 1
# Question:

# Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:

# 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']

# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, 
# it should be assumed to be a console input. tuple() method can convert list to tuple

num = (input('Masukkan Angka : '))
print(num.split(','))
print(tuple(num.split(',')))

print('\n---QUESTION 5---\n')

# Level 1
# Question:

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()

strObj.getString()
strObj.printString()

print('\n---QUESTION 6---\n')

# Level 2
# Question:

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value 
# (for example, if the output received is 26.0, it should be printed as 26). 
# In case of input data being supplied to the question, 
# it should be assumed to be a console input.

import math
num = (input('Masukkan Angka : ')).split(',')
hasil = []
out = ''
for a, b in zip(num,range(len(num))):
    hasil.append(round(math.sqrt((2*50*int(a))/30)))
    out += '{}, '.format(str(hasil[b]))
print(out)

print('\n---QUESTION 7---\n')

# Level 2
# Question:
# Write a program which takes 2 digits, 
# X,Y as input and generates a 2-dimensional array.

# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.

# Example

# Suppose the following inputs are given to the program:
# 3,5

# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question, 
# it should be assumed to be a console input in a comma-separated form.

# a = input('Masukkan Angka: ')
# aList = a.split(',')
# outList = []
# for a in range(int(aList[0])):
#     tempList = []
#     for b in range(int(aList[1])):
#         if a == 0 :
#             tempList.append(0)
#         elif a > 0 :
#             tempList.append((outList[a-1][b])+b)
#     outList.append(tempList)
#     tempList = []
# print(outList)

a = input('Masukkan Angka: ')
aList = a.split(',')
multilist = [[0 for col in range(int(aList[1]))] for row in range(int(aList[0]))]

for row in range(int(aList[0])):
    for col in range(int(aList[1])):
        multilist[row][col]= row*col
        
print(multilist)

print('\n---QUESTION 8---\n')

# Level 2
# Question:

# Write a program that accepts a comma separated sequence of words as input 
# and prints the words in a comma-separated sequence after sorting them alphabetically. 

# Suppose the following input is supplied to the program: 
# without,hello,bag,world 

# Then the output should be: 
# bag,hello,without,world

# Hints:
# In case of input data being supplied to the question, 
# it should be assumed to be a console input.

word = (input()).split(',')
print(','.join(sorted(word)))