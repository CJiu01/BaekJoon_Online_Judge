from collections import deque

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
    
    
n, m, v = map(int,input().split())

arr = []
for i in range(m):
        arr.append(list(map(int, input().split())))

graph = [[] for i in range(n+1)]

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(n+1):
    graph[i].sort()


visited = [False]*(n+1)
dfs(graph, v, visited)
print()
visited_bfs = [False]*(n+1)
bfs(graph, v, visited_bfs)
print('')
