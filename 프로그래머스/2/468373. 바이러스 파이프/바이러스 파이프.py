from itertools import product
from collections import deque

def bfs(start, visited, pipe, graph):
    visited[start] = True
    
    while pipe:
        kind = pipe.pop()
        q = deque(i for i,v in enumerate(visited) if v)
            
        while q:
            v = q.popleft()
            for e,k in graph[v]:
                if not visited[e] and k==kind:
                    q.append(e)
                    visited[e] = True


def solution(n, infection, edges, k):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a,b,c in edges:
        graph[a].append([b,c])
        graph[b].append([a,c])  
    
    for i in (list(product([1,2,3], repeat=k))):
        visited = [False]*(n+1)
        bfs(infection, visited, list(i), graph)
        answer = max(answer, visited.count(True))
    
    return answer