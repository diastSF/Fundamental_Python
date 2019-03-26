# t = (1,[0,'test'], {'a1':True})

# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1] = 'mark'
# print(t[1])

# s = {1,2,4,3,2,3,'a',True, False}

# print(s)

# x = [1,2,3,4,5]
# x = [y *2 for y in x]
# print(x)

# arrManusia = [
#     {
#         'nama' : 'Diast',
#         'umur' : 25,
#         'pekerjaan' : 'freelance'
#     },
#     {
#         'nama':'Telo',
#         'umur':24,
#         'pekerjaan' :'dagang'
#     },
#     {
#         'nama':'Faisal',
#         'umur':26,
#         'pekerjaan' :'swasta'
#     }
# ]

# def Ceritakan(dataManusia):
#     return 'Namanya {}, dia berumur {}, dan pekerjaannya adalah {}'.format(dataManusia['nama']
#     ,dataManusia['umur'],dataManusia['pekerjaan'])

# arrCerita = (map(Ceritakan, arrManusia))

# print(arrCerita)
# for i in range(len(arrCerita)):
#     print('cerita {} : '. format(i+1))
#     print(arrCerita[i])

# def times2(num):
#     return num *2

# x = [ 1,2,3,4,5]
# x = list(map(times2, x))
# print(x)

# y = [1,2,3,4,5]
# y = list(map(lambda z: z*2, y))
# print(y)

# def genap(a):
#     return a%2 == 0

# listA = [1,2,3,4,5]
# listA = list(filter(genap, listA))
# print(listA)

# listB = [1,2,3,4,5]
# listB = list(filter(lambda num : num%2 == 0, listB))
# print(listB)

# numList = [1,2,3]
# index = 'x'

# check1 = index in numList
# check2 = 'x' in [ 'x', 'y', 'z']
# check3 = 3 in numList
# check4 = 5 in numList
# check5 = 'di' in 'diast'

# print(check1)
# print(check2)
# print(check3)
# print(check4)
# print(check5)

# newDict = { 'k' : 12}
# print(newDict)
# newDict['m'] = 13
# print(newDict)

# SOLVE IT! 1

namaList = ['Merdeka', 'Hellos', 'Sohib', 'Kari Ayam']
print(namaList)
cari = input('Search : ')

# CARA 1

# def searching(keyword, listdata):
#     return(list(filter(lambda x: keyword.lower() in x.lower(), listdata)))

# hasil = searching(cari,namaList)

# CARA 2

# def searching(x):
#     return cari.lower() in x.lower()

# hasil = list(filter(searching, namaList))

# CARA 3

hasil = list(filter(lambda x: cari.lower() in x.lower(), namaList))

print(hasil)