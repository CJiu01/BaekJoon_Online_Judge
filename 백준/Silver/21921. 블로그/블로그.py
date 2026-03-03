import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]

for i in range(N):
    sum_value += arr[i]
    prefix_sum.append(sum_value)
    
res = 0
cnt = 0
for i in range(X,N+1):
    tmp = prefix_sum[i]-prefix_sum[i-X]
    if tmp>res:
        res = tmp
        cnt = 1
    elif tmp==res:
        cnt+=1

if res!=0:         
    print(res)
    print(cnt)
else:
    print("SAD")
    