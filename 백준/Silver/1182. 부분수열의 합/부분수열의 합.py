from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1,n+1):
    sub = list(combinations(arr, i))
    for a in sub:
        if (sum(a)==s):
            cnt += 1     
print(cnt)