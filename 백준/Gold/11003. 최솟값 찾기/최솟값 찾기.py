import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
window = list(map(int, input().split()))
D = [0]*N
h = deque([0]) 
D[0] = window[0]

for i in range(1,N):
    if (h and h[0] < (i-L+1)):
        h.popleft()
    while (h and window[h[-1]]>window[i]):
        h.pop()
    
    h.append(i)
    D[i] = window[h[0]]
    
print(*D)