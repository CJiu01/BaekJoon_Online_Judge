def GCD(a,b):
    while(b!=0):
        k=a%b
        a=b
        b=k
    return a

a,b = map(int,input().split())
gcd=GCD(a,b)
print(gcd)
print((a*b)//gcd)