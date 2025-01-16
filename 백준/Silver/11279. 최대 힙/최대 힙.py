import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if not heap:
            print("0")
        else:
            tmp = heapq.heappop(heap)
            print(tmp[1])

    else:
        heapq.heappush(heap,(-x,x))