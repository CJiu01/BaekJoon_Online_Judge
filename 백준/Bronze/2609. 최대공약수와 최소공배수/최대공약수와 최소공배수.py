def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a

a,b = map(int, input().split())
res = gcd(a,b)
print(res)
print(a*b//res)