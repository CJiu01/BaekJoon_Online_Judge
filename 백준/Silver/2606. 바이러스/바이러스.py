import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
def dfs(v):
    global result
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            result += 1
            dfs(i)
    
dfs(1)
print(result)