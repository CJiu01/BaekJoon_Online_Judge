import sys

def fac(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

T = int(input())
bridge = []
for i in range(T):
    site_N, site_M = map(int, input().split())
    bridge.append(int(fac(site_M)/(fac(site_N)*fac(site_M-site_N))))

for i in bridge:
    print(i)