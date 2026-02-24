import sys
input = sys.stdin.readline
import heapq

N, L = map(int, input().split())
window = list(map(int, input().split()))
D = [0]*N
h = []

for i in range(N):
    heapq.heappush(h, (window[i],i)) # value, idx
    while (h[0][1] < (i-L+1)):
        heapq.heappop(h)   
    D[i] = h[0][0]
    
print(*D)