import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

visited = [0] * (n+1)
order = 1

def dfs(v):
    global order
    visited[v] = order
    order += 1
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
    
dfs(r)
for i in range(1,n+1):
    print(visited[i])