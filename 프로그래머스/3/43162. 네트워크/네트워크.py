from collections import deque

def bfs(v, visited, graph):
    q = deque([v])
    visited[v] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return

def solution(n, computers):
    answer = 0
    visited = [False]*n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, graph)
            answer += 1

    return answer