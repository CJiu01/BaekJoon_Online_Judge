import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs_ depth first search
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i ,visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in graph:
    i.sort()

visited = [False]*(n+1)
result = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        result += 1
print(result)