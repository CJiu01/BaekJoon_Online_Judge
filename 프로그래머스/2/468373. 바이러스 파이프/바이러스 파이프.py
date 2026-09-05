from itertools import product
from collections import deque

def bfs(start, visited, pipe, graph):
    
    
    visited[start] = True
    
    while pipe:
        kind = pipe.pop()
        q = deque([])

        for a,b in enumerate(visited):
            if not b:
                continue
            q.append(a)
            
        while q:
            v = q.popleft()
            
            for i in graph[v]:
                e,k = i[0],i[1]
                if not visited[e] and k==kind:
                    q.append(e)
                    visited[e] = True


def solution(n, infection, edges, k):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for e in edges:
        graph[e[0]].append([e[1],e[2]])
        graph[e[1]].append([e[0],e[2]])  
    
    for i in (list(product([1,2,3], repeat=k))):
        visited = [False]*(n+1)
        bfs(infection, visited, list(i), graph)
        answer = max(answer, visited.count(True))
    
    return answer