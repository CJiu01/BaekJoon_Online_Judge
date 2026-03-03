import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

current = sum(arr[:X])
res = current
cnt = 1

for i in range(1,N-X+1):
    current += arr[i+X-1]
    current -= arr[i-1]
    
    if current>res:
        res = current
        cnt = 1
    elif current==res:
        cnt+=1

if res!=0:         
    print(res)
    print(cnt)
else:
    print("SAD")