def listFibo(x):
    fibo = []
    for a in range (x):
        if (a < 2):
            fibo.append(1)
        else :
            fibo.append(fibo[a-1] + fibo[a-2])
    return fibo

inputUser = int(input('input fibo : '))

hasil = listFibo(inputUser)
print(hasil)
if (len(hasil) > 0):
    print("Output = {}".format(hasil[-1]))
else :
    print('Output = None')