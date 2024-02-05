from collections import deque
import sys

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
            
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        
        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    
input = sys.stdin.readline
n, m, v = map(int,input().split())

arr = []

graph = [[] for i in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

visited = [False]*(n+1)
dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited)
