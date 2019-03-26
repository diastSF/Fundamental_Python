arr = [6,5,3,1,8,7,2,4]

# def Ascending(x,y):
#     return x-y

# for a in range(len(arr)-1):
#     for b in range(a+1 , len(arr)):
#         hasil1 = Ascending(arr[a], arr[b])
#         if (hasil > 0):
#             temp = arr[a]
#             arr[a] = arr[b]
#             arr[b] = temp

# print(arr)
for z in range(len(arr)-1):
    for x in range(len(arr)-1):
        if(arr[x] < arr[x+1]):
            arr[x], arr[x+1] = arr[x+1], arr[x]


print('hasilnya : {}'.format(arr))
