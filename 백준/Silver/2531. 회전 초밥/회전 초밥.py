from collections import defaultdict


import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]
arr += arr[:k-1]

count = defaultdict(int)
unique = 0
res = 0

# 초기 윈도우 세팅
for i in range(k):
    if count[arr[i]] == 0:
        unique += 1
    count[arr[i]] += 1
    
res = unique + (1 if count[c]==0 else 0)

# 슬라이딩 시작
for i in range(1,N):
    # 제거할 초밥
    left = arr[i-1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    
    # 추가할 초밥
    right = arr[i+k-1]
    if count[right] == 0:
        unique += 1
    count[right] += 1
    
    tmp = unique + (1 if count[c]==0 else 0)
    res = max(res, tmp)
print(res)
