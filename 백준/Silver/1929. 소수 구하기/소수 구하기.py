# 우선 백만까지의 소수를 다 구할것임.

isErased = [0]* 1000001
isErased[1] = 1

i = 2
while i*i<=1000000:
    if isErased[i] == 0:
        # i는 소수
        for j in range(i*i, 1000000,i):
            isErased[j] = 1
    i+=1

m,n = map(int, input().split())
for i in range(m, n+1):
    if isErased[i] == 0:
        print(i)
