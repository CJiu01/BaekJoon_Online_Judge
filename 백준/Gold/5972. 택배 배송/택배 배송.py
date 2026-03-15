import heapq

def dijkstra(start,visited):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True
    
    while q:
        dist, now = heapq.heappop(q)
        if now==N:
            return distance[now]
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                visited[i[0]] = True
                heapq.heappush(q, (cost,i[0]))
        
    return


INF = int(1e9)
ans = INF
N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))
    
visited = [False]*(N+1)
print(dijkstra(1,visited))