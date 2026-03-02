import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
    
arr = arr+arr[:k-1]
sushi = []
res = 0
for i in range(N):
    cnt = len(set(arr[i:i+k]+[c]))
    res = max(cnt,res)
    
print(res)