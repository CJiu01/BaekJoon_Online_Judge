from collections import deque

def bfs(v, visited, computers, n):
    q = deque([v])
    visited[v] = True
    
    while q:
        v = q.popleft()
        for i in range(n):
            if computers[v][i]==1 and not visited[i]:
                q.append(i)
                visited[i] = True
    return

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            answer += 1
    
    return answer