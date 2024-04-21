import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

weight = [-1] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    weight[v] = 0
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == False:
                weight[i] = weight[v] + 1
                if i == b:
                    return weight[i]
                queue.append(i)
                visited[i] = True
    return -1
    
print(bfs(a))