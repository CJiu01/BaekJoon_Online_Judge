from collections import deque
import sys

t= int(input())

for i in range(t):
    N,M = map(int, input().split())
    queue= deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    
    while queue:
        

        if queue[0]==max(queue):
            queue.popleft()
            count += 1
            if M==0:
                break
        else:
            v= queue.popleft()
            queue.append(v)
        M-=1
        
        if M<0:
            M=len(queue)-1
    print(count)