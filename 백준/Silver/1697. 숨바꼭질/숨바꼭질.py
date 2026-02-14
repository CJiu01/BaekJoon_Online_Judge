from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, visited):
    queue = deque([(start,0)])

    depth = 0
    while queue:
        v = queue.popleft()
        if (v[0]==K):
            return v[1]
        
        if (0<=v[0]-1<=100000):
            graph[v[0]].append(v[0]-1)
        if (0<=v[0]+1<=100000):
            graph[v[0]].append(v[0]+1)
        if (0<=v[0]*2<=100000):
            graph[v[0]].append(v[0]*2)
        
        for i in graph[v[0]]:
            if (not visited[i]):
                queue.append((i,v[1]+1))
                visited[i] = True
    
        
N, K = map(int, input().split())
visited = [False]*100001
visited[N] = True
graph = [[] for _ in range(100001)]

res = bfs(N, visited)
print(res)