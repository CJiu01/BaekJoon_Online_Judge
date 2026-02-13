from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited, parents):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        parent = queue.popleft()
        
        for i in graph[parent]:
            if not visited[i]:
                parents[i] = parent
                queue.append(i)
                visited[i] = True
                
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
parents = [0]*(N+1)

for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited, parents)
    
for i in range(2, N+1):
    print(parents[i])