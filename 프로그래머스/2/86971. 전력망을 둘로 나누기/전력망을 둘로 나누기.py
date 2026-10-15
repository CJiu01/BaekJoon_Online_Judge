def dfs(v, visited, graph):
    visited[v] = True
    return sum([1] + [dfs(u, visited, graph) for u in graph[v] if not visited[u]])

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for (a,b) in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = n
    for wire in wires:
        v1,v2 = wire
        visited = [False]*(n+1)
        visited[v1] = True
        visited[v2] = True
        
        cnt = dfs(v1, visited, graph)
        answer = min(answer, abs(cnt-(n-cnt)))
    
    return answer