from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(graph, x, y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    
    
    while queue:
        vector = queue.popleft()
        
        for i in range(4):
            tx = vector[0] + dx[i]
            ty = vector[1] + dy[i]

            if (0<=tx<M and 0<=ty<N):
                if ((graph[tx][ty]==1) and (not visited[tx][ty])):
                    queue.append((tx, ty))
                    visited[tx][ty] = True
                
    
T = int(input())

for p in range(T):
    M, N, K = map(int, input().split())
    visited = [[False]*N for _ in range(M)]
    graph = [[0]*N for _ in range(M)]
    
    for q in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(M):
        for j in range(N):
            if ((graph[i][j]==1) and (not visited[i][j])):
                bfs(graph, i, j, visited)
                result += 1

                
    print(result)