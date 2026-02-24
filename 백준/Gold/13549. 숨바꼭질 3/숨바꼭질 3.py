from collections import deque

def bfs(start):
    queue = deque([start])
    dist[start] = 0
    
    while queue:
        x = queue.popleft()
        if (x==k):
            return dist[x]
        
        for next in [x-1, x+1, x*2]:
            if (next<0 or next>100000):
                continue
            distance = 0
            if next == x*2:
                distance = dist[x]
            else:
                distance = dist[x]+1
                
                
            if (dist[next] <= distance):
                continue
            dist[next] = distance
            queue.append(next)

n,k = map(int, input().split())
dist = [int(1e9)]*100001
print(bfs(n))
