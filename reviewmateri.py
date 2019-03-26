# t = (1,[0,'test'], {'a1' : True})

# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1] = 'mark'
# print(t[1])

# for i , j in zip(range(0,6,2),[3,2,6,1]):
#     print('ini i {} dan ini j {}'.format(i,j))

def times2(var):
    return var*2

print(times2(2))

print(lambda num: num*2)

listnum = [5,1,2,3,4]
listnum1 = list(map(lambda num: num * 2, listnum))
listnum2 = list(filter(lambda num: num % 2 == 0, listnum))
print(listnum1)
print(listnum2)

print(listnum.pop())
print(listnum)