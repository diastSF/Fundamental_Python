# x = 5
# y = '5'

# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

#BATAS#

# nilai = 40
# if (nilai > 80) :
#     print('Good Job!')
# elif (nilai >= 60 and nilai <= 80) :
#     print('Good Job!')
# else :
#     print("Don't Give Up!")

#SOAL 1#

#CARA 1
# a = int(input('Masukkan angka : '))

# if (a % 2 == 0) :
#     print('Angka ' + str(a) + ' tergolong bilangan GENAP!')
# else :
#     print('Angka ' + str(a) + ' tergolong bilangan GANJIL!')

#CARA 2
# if ((a/2).is_integer()) :
#     print('Angka ' + str(a) + ' tergolong bilangan GENAP!')
# else :
#     print('Angka ' + str(a) + ' tergolong bilangan GANJIL!')

# CARA 3
# b = ['GENAP', 'GANJIL']

# print("Angka {} tergolong bilangan {}".format(a, b[a%2]))

#SOAL 2#

massa = int(input('Masukkan Massa (kg) : '))
tinggi = int(input('Masukkan Tinggi (cm) : '))
tinggi1 = tinggi / 100

print('Massa ' + str(massa) + ' kg & tinggi ' + str(tinggi1) + ' m ')

imt = massa / (tinggi1 ** 2)

if (imt < 18.5) :
    print('IMT = ' + str(imt) + ', BERAT BADAN KURANG!')
elif (imt >= 18.5 and imt <= 24.9) :
    print('IMT = ' + str(imt) + ', BERAT BADAN IDEAL!')
elif (imt >= 25.0 and imt <= 29.9) :
    print('IMT = ' + str(imt) + ', BERAT BADAN BERLEBIH!')
elif (imt >= 30.0 and imt <= 39.9) :
    print('IMT = ' + str(imt) + ', BERAT BADAN SANGAT BERLEBIH!')
else :
    print('IMT = ' + str(imt) + ', OBESITAS!')