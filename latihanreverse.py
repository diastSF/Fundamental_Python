import math

# arr = [1,2,3]

# # cara 1
# temp = arr[0]
# arr[0] = arr[1]
# arr[1] = temp

# # cara 2
# arr[0], arr[1] = arr[1], arr[0]

# print(arr)

# a = 5; b = 3; c = 2
# a,b,c = 5,3,2

# a = [1, 2, 3]

# # temp = a[0]
# # a[0] = a[2]
# # a[0] = temp

# def reverseA(x):
#     hasil = a[0], a[1], a[2] = a[2], a[1], a[0]
#     return hasil


# print(reverseA(a))

def reverseA(theList):
    for i, j in zip(
        range(0, math.floor(len(theList)/2)),
        range(len(theList)-1, math.ceil(len(theList)/2)-1, -1)
    ) :
        theList[i], theList[j] = theList[j], theList[i]
    return theList

def reverseB(theList):
    for k in range(0, math.floor(len(theList)/2)):
        theList[k], theList[len(theList)-1-k] = theList[len(theList) -1-k], theList[k]

    return theList

print(reverseA([1,2,3,4,5,6,7,8,9]))
print(reverseB([1,2,3,4,5,6,7,8,9]))