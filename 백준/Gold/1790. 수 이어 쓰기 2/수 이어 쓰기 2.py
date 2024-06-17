import sys
input = sys.stdin.readline

N,k = map(int, input().split())

start = 0
digit = 1
nine = 9

while k > nine*digit:
    k -= nine*digit
    start += nine
    nine *= 10
    digit += 1
    
result = (start+1) + ((k-1)//digit)

if result>N: print(-1)
else: print(str(result)[(k-1)%digit])