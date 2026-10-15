def dfs(v, visited, graph):
    global res
    visited[v] = True
    res += 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)

    return res


def solution(n, wires):
    global res
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for (a,b) in wires:
        graph[a].append(b)
        graph[b].append(a)
  
    for wire in wires:
        v1,v2 = wire
        visited = [False]*(n+1)
        visited[v1] = True
        visited[v2] = True
        
        res = 0
        v1_res = dfs(v1, visited, graph)
        res = 0
        v2_res = dfs(v2, visited, graph)
        answer = min(answer, abs(v1_res - v2_res))
    
    return answer