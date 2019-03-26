def fizzbuzz(x):
    for a in range(1, x+1):
        if (a%3 == 0 and a%5 ==  0):
            a = 'fizzbuzz'
        elif(a%3 == 0):
            a = 'fizz'
        elif (a%5 == 0):
            a = 'buzz'
        print(a)

print(fizzbuzz(20))

