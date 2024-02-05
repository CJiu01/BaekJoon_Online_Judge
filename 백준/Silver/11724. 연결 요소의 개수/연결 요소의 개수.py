import sys
sys.setrecursionlimit(10**6)

user = sys.stdin.readline
n, m = map(int, user().split())

graph = [[] for i in range(n+1)]
for _ in range(m):
    user = sys.stdin.readline
    x, y = map(int, user().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in graph:
    i.sort()
    
result = 0 
visited = [False]*(n+1)

# dfs_ stack, recursive
def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
    return True

for i in range(1, n+1):
    if not visited[i]:
        if dfs(i)==True:
            result += 1
        
print(result)