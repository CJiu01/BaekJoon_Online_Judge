import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
window = list(map(int, input().split()))
D = [0]*N
h = deque([(window[0],0)]) # value, idx
D[0] = window[0]

for i in range(1,N):
    while (h and h[0][1] < (i-L+1)):
        h.popleft()
        
    if (h and h[-1][0]>window[i]):
        while (h and h[-1][0]>window[i]):
            h.pop()
    
    h.append((window[i], i))
    D[i] = h[0][0]
    
print(*D)