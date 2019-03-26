n = 110
k = n
t = 0
plus = True

while(n>0):
    num = n % 10
    if(plus):
        t+=num
    else:
        t-=num
    n = int(n/10)
    plus=not(plus)

print("t = {}".format(t))
if(t % 11 == 0):
    print("{} is divisible by 11".format(k))
else :
    print("{} is not divisible by 11".format(k))
